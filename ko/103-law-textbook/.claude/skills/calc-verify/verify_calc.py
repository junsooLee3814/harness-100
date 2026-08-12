# -*- coding: utf-8 -*-
"""
verify_calc.py — 교재 계산 사례 기계 검산기

사용:
    python verify_calc.py <cases.json> [--allow-warnings]

원리: 사례를 inputs + steps(수식·기대값)로 정의하면, 안전한 산술 평가기(AST 화이트리스트,
eval/exec 미사용)로 재계산해 기대값·본문 표기값과 대조한다.
교재의 계산 오류는 독자의 의사결정 오류가 된다 — 사람 검산을 대체하지 않되, 그 전에 기계가 거른다.

종료 코드: 0 통과 / 1 입력 오류 / 2 검산 불일치 / 3 경고(기준연도 누락 등)
"""
import sys
import json
import ast
import operator as op

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print(f"[WARN] {msg}", file=sys.stderr)


# ---------------- 안전 산술 평가기 (AST 화이트리스트 — eval/exec 없음)
_BIN = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
        ast.FloorDiv: op.floordiv, ast.Mod: op.mod, ast.Pow: op.pow}
_UNARY = {ast.UAdd: op.pos, ast.USub: op.neg}
_FUNCS = {"min": min, "max": max, "round": round, "abs": abs, "int": int}


def safe_eval(expr, names):
    """산술식만 허용. 변수는 names 딕셔너리에서만."""
    def _ev(node):
        if isinstance(node, ast.Expression):
            return _ev(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"숫자 외 상수 금지: {node.value!r}")
        if isinstance(node, ast.Name):
            if node.id in names:
                return names[node.id]
            raise ValueError(f"미정의 변수: {node.id}")
        if isinstance(node, ast.BinOp) and type(node.op) in _BIN:
            l, r = _ev(node.left), _ev(node.right)
            if isinstance(node.op, ast.Pow) and (abs(r) > 100 or abs(l) > 10**9):
                raise ValueError(f"지수 연산 상한 초과: {l} ** {r}")
            return _BIN[type(node.op)](l, r)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
            return _UNARY[type(node.op)](_ev(node.operand))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in _FUNCS and not node.keywords:
                return _FUNCS[node.func.id](*[_ev(a) for a in node.args])
            raise ValueError(f"허용되지 않은 함수: {getattr(node.func, 'id', '?')}")
        if isinstance(node, ast.IfExp):  # a if cond else b — 구간 분기용
            return _ev(node.body) if _ev(node.test) else _ev(node.orelse)
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            cmp_ops = {ast.Lt: op.lt, ast.LtE: op.le, ast.Gt: op.gt,
                       ast.GtE: op.ge, ast.Eq: op.eq, ast.NotEq: op.ne}
            if type(node.ops[0]) in cmp_ops:
                return cmp_ops[type(node.ops[0])](_ev(node.left), _ev(node.comparators[0]))
        raise ValueError(f"허용되지 않은 구문: {ast.dump(node)[:60]}")
    return _ev(ast.parse(expr, mode="eval"))


def validate_brackets(brackets):
    """구간표 구조 검증 — 잘못 짠 구간표로 검산 도장을 받는 것을 막는다 (#2).
    요건: 상한 오름차순, null(무한)은 마지막 1개만, 세율 0~1, 누진공제 ≥ 0·비감소."""
    if not isinstance(brackets, list) or not brackets:
        raise ValueError("brackets 비어 있음")
    prev_upper = None
    for i, row in enumerate(brackets):
        if not (isinstance(row, list) and len(row) == 3):
            raise ValueError(f"brackets[{i}] 형식 오류 — [상한, 세율, 누진공제]")
        upper, rate, ded = row
        if upper is None:
            if i != len(brackets) - 1:
                raise ValueError(f"brackets[{i}] null 상한은 마지막 구간에만 허용")
        else:
            if not isinstance(upper, (int, float)) or upper <= 0:
                raise ValueError(f"brackets[{i}] 상한이 양수가 아님: {upper}")
            if prev_upper is not None and upper <= prev_upper:
                raise ValueError(f"brackets[{i}] 상한이 오름차순 아님: {prev_upper} → {upper}")
            prev_upper = upper
        if not isinstance(rate, (int, float)) or not (0 <= rate <= 1):
            raise ValueError(f"brackets[{i}] 세율이 0~1 범위 아님: {rate}")
        if not isinstance(ded, (int, float)) or ded < 0:
            raise ValueError(f"brackets[{i}] 누진공제가 음수: {ded}")
    if brackets[-1][0] is not None:
        raise ValueError("마지막 구간의 상한은 null(무한)이어야 함")


def progressive_tax(base, brackets):
    """누진세율 계산 — brackets: [[상한 또는 null, 세율, 누진공제], ...]
    방식(누진공제): 해당 구간의 base*세율 - 누진공제"""
    validate_brackets(brackets)
    if base < 0:
        raise ValueError(f"과세표준이 음수({base:,.0f}) — 공제 과대 여부를 확인하십시오. "
                         "0 하한이 의도라면 expr에 max(..., 0)을 명시할 것")
    for upper, rate, deduction in brackets:
        if upper is None or base <= upper:
            return base * rate - deduction
    raise ValueError("과세표준이 모든 구간을 초과")


def run_case(case, idx):
    cid = case.get("id", f"case{idx}")
    errors = []
    if "기준연도" not in case:
        warn(f"{cid}: '기준연도' 누락 — 세율·공제의 기준 시행연도를 명시하십시오")
    names = dict(case.get("inputs", {}))
    for k, v in list(names.items()):
        if not isinstance(v, (int, float)):
            errors.append(f"inputs.{k} 가 숫자가 아님: {v!r}")
    if errors:
        return cid, errors

    for i, step in enumerate(case.get("steps", []), start=1):
        sname = step.get("name", f"step{i}")
        try:
            if "누진세율" in step:  # {"누진세율": {"base": "과세표준", "brackets": [...]}}
                spec = step["누진세율"]
                base = names[spec["base"]] if isinstance(spec["base"], str) else spec["base"]
                got = progressive_tax(base, spec["brackets"])
            else:
                got = safe_eval(step["expr"], names)
        except Exception as e:
            errors.append(f"{sname}: 계산 실패 — {e}")
            continue
        if sname in case.get("inputs", {}):
            warn(f"{cid}/{sname}: step 이름이 inputs 키를 덮어씁니다 — 이름을 바꾸십시오")
        names[sname] = got
        if "expected" in step:
            exp = step["expected"]
            tol = step.get("tolerance", 0)
            if tol and exp and abs(tol) > abs(exp) * 0.001:
                warn(f"{cid}/{sname}: tolerance {tol:,} 가 기대값의 0.1%를 초과 — "
                     f"오차 은폐 위험. 사유를 명시하십시오")
            if abs(got - exp) > tol:
                errors.append(f"{sname}: 기대 {exp:,} vs 계산 {got:,.2f} (허용오차 {tol})")
            elif tol:
                print(f"  (tol={tol:,} 적용: {sname})")

    if "본문_표기값" in case:
        step_names = {st.get("name", f"step{i}")
                      for i, st in enumerate(case.get("steps", []), start=1)}
        final_name = case.get("최종단계") or (case["steps"][-1].get("name", f"step{len(case['steps'])}")
                                              if case.get("steps") else None)
        exp = case["본문_표기값"]
        if not isinstance(exp, (int, float)):
            errors.append(f"본문_표기값이 숫자가 아님: {exp!r}")
        elif final_name not in step_names:
            # inputs 키를 가리키면 계산 0회로 '통과'하는 우회로가 되므로 반드시 산출명이어야 한다 (#4)
            errors.append(f"최종단계 '{final_name}' 가 steps 산출명이 아님 — 검산 우회 금지")
        elif final_name in names:
            got = names[final_name]
            tol = case.get("tolerance", 0)
            if tol and exp and abs(tol) > abs(exp) * 0.001:
                warn(f"{cid}: 본문 대조 tolerance {tol:,} 가 표기값의 0.1% 초과 — 오차 은폐 위험")
            if abs(got - exp) > tol:
                errors.append(f"본문 표기값 {exp:,} vs 검산 {got:,.2f} — 본문 수치를 정정하십시오")
        else:
            errors.append("본문_표기값 대조 불가 — 최종단계 계산이 실패했습니다")
    else:
        warn(f"{cid}: '본문_표기값' 없음 — 본문과의 대조가 생략됩니다")
    return cid, errors


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_warn = "--allow-warnings" in sys.argv
    if not argv:
        print("Usage: python verify_calc.py <cases.json> [--allow-warnings]", file=sys.stderr)
        sys.exit(1)
    try:
        with open(argv[0], "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] 입력 json 없음: {argv[0]}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"[ERROR] json 파싱 실패: {e}", file=sys.stderr)
        sys.exit(1)
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        print("[ERROR] cases[] 가 필요합니다. cases.sample.json 참조.", file=sys.stderr)
        sys.exit(1)

    total_err = 0
    for i, case in enumerate(cases, start=1):
        cid, errors = run_case(case, i)
        if errors:
            total_err += len(errors)
            print(f"FAIL {cid}:")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"PASS {cid}")
    print(f"cases={len(cases)} failures={total_err} warnings={len(WARNINGS)}")
    if total_err:
        sys.exit(2)
    if WARNINGS and not allow_warn:
        print("[FAIL] 경고가 있어 실패로 처리합니다. 수정하거나 --allow-warnings + 사유 명시.",
              file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
