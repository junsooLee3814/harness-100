# 02. 투자 프로세스 플로차트 — SMB투자파트너스

> **면책 문구**: 본 문서는 내부 업무 가이드이며 법적 효력을 갖지 않음.
> **작성 기준**: `01_document_analysis.md` 기반 초안. 모든 항목 **[현장 검증 필요]**.
> **작성일**: 2026-06-25 | **문서 버전**: v0.1 (초안)

---

## 1. Level 0 — 전체 투자 프로세스 맵

> SMB투자파트너스 5단계 투자 전 과정 고수준 개요도. GO/NO-GO 분기 및 반려·보류 경로 포함.

```mermaid
flowchart TD
    START([딜 유입\nIB·브로커·자체발굴]) --> S1

    subgraph S1["① 투자요청 접수\n1~5 영업일"]
        A1[IM·재무제표 수령]
        A2[1차 적합성 필터링]
        A3[NDA 체결]
        A4[딜 로그 등록 & 심사역 배정]
        A1 --> A2 --> A3 --> A4
    end

    A4 --> DEC1{GO / NO-GO\n팀장 승인}
    DEC1 -- "NO-GO\n즉시 반려" --> REJ1([반려 통보\n사유 기록])
    DEC1 -- "예외\n대표이사 승인" --> S2
    DEC1 -- GO --> S2

    subgraph S2["② 예비심사\n5~17 영업일"]
        B1[재무·신용 분석]
        B2[Valuation 예비 산정]
        B3[예비심사 보고서 작성]
        B4[팀장 보고]
        B5[LOI / Term Sheet 발송]
        B1 --> B2 --> B3 --> B4 --> B5
    end

    B5 --> DEC2{GO / NO-GO\n팀장 결재}
    DEC2 -- "NO-GO\n예비심사 종결" --> REJ2([반려 또는 보류])
    DEC2 -- GO --> S3

    subgraph S3["③ 본심사 — DD & IC\n4~8주"]
        C1[DD 팀 구성 & Data Room 요청]
        C2[재무·법무·세무·사업 DD]
        C3[최종 Valuation & 투자구조 확정]
        C4[IC Memo 작성]
        C5[IC 투자심의위원회 개최]
        C1 --> C2 --> C3 --> C4 --> C5
    end

    C5 --> DEC3{IC 결의\n과반수 찬성}
    DEC3 -- "부결" --> REJ3([투자 부결\n의사록 기록])
    DEC3 -- "조건부 승인" --> COND[조건 충족 확인\n팀장 재확인]
    COND --> S4
    DEC3 -- "승인" --> S4

    subgraph S4["④ 투자 집행 — Closing\n2~6주"]
        D1[투자계약서 초안 & 협상]
        D2[선행조건CP 충족 확인]
        D3[계약서 서명 Signing]
        D4[담보 설정 등기]
        D5[자금 집행 Closing]
        D6[사후 등기·공시 & 장부 등록]
        D1 --> D2 --> D3 --> D4 --> D5 --> D6
    end

    D6 --> DEC4{클로징 체크리스트\n전 항목 완료?}
    DEC4 -- "미완료" --> D2
    DEC4 -- "완료" --> S5

    subgraph S5["⑤ 사후관리 & EXIT\n통상 3~7년"]
        E1[정기 재무보고 수령]
        E2[Covenant 모니터링]
        E3[Valuation 업데이트]
        E4[이벤트 모니터링]
        E5[EXIT 전략 수립]
        E6[EXIT 실행]
        E1 --> E2 --> E3 --> E4 --> E5 --> E6
    end

    E4 -- "Covenant 위반\n조기경보" --> EMRG[긴급 EXIT\n워크아웃·Put Option]
    E6 --> END([투자 회수 완료\nLP 정산 & 성과 보고])
    EMRG --> END

    style REJ1 fill:#ffcccc,stroke:#cc0000
    style REJ2 fill:#ffcccc,stroke:#cc0000
    style REJ3 fill:#ffcccc,stroke:#cc0000
    style EMRG fill:#ffe0b2,stroke:#e65100
    style END fill:#c8e6c9,stroke:#2e7d32
    style START fill:#e3f2fd,stroke:#1565c0
```

---

## 2. Level 1 — 단계별 상세 플로차트

### 2-1. 단계 1: 투자요청 접수 (Deal Sourcing & Intake)

```mermaid
flowchart TD
    IN1([딜 유입\nIB / 브로커 / 소개인 / 자체발굴]) --> T1_1

    subgraph GRP_ADM["어드민 / 비서"]
        T1_1[투자제안서 IM 수령\n회사소개서·재무제표·등기부 등]
        T1_2[서류 등록 & 수령 확인]
        T1_1 --> T1_2
    end

    T1_2 --> T1_3

    subgraph GRP_JR["심사역 (Deal Screener)"]
        T1_3[1차 적합성 스크리닝\n업종제한·최소규모·법적결격]
        T1_4[소개인 수수료 조건 확인\nFinder's Fee 비율·지급방식]
        T1_5[예비 투자 조건 범위 확인\n규모·만기·금리·전환조건]
        T1_3 --> T1_4 --> T1_5
    end

    T1_5 --> DEC_1A{1차 필터 통과?}
    DEC_1A -- "NO\n배제업종·규모미달·결격" --> OUT1A([즉시 반려\n사유 기록 후 통보])
    DEC_1A -- "예외 케이스" --> T1_EX[대표이사 예외 승인 검토]
    T1_EX --> DEC_1B{대표이사 승인?}
    DEC_1B -- "부결" --> OUT1A
    DEC_1B -- "승인" --> T1_6
    DEC_1A -- "통과" --> T1_6

    subgraph GRP_JR2["심사역 (Deal Screener)"]
        T1_6[NDA 초안 작성 & 발송]
        T1_7[쌍방 NDA 서명 완료]
        T1_8[딜 로그 CRM 등록\n기업 기본정보 입력]
        T1_6 --> T1_7 --> T1_8
    end

    subgraph GRP_TL["팀장"]
        T1_9[담당 심사역 배정\n업종·경험 고려]
        T1_10[1차 스크리닝 체크리스트 승인]
        T1_9 --> T1_10
    end

    T1_8 --> T1_9
    T1_10 --> OUT1B([예비심사 단계 진입])

    style OUT1A fill:#ffcccc,stroke:#cc0000
    style OUT1B fill:#c8e6c9,stroke:#2e7d32
    style IN1 fill:#e3f2fd,stroke:#1565c0
```

**산출 문서**: NDA 체결본 / 딜 접수 등록 시트 / 1차 스크리닝 체크리스트
**소요기간**: 접수~NDA 체결 1~3 영업일 / 접수~담당자 배정 3~5 영업일

---

### 2-2. 단계 2: 예비심사 (Preliminary Review)

```mermaid
flowchart TD
    IN2([단계 1 완료\nNDA·딜 로그·IM 수령]) --> T2_1

    subgraph GRP_JR["심사역"]
        T2_1[기업 개요 분석\n사업모델·시장포지션·경쟁사]
        T2_2[재무 지표 분석\n매출성장·EBITDA·부채비율·이자보상]
        T2_3[신용·법적 리스크 스크리닝\nCB·NICE·KCB 조회·소송·가압류]
        T2_4[투자 구조 검토\nCB·BW·RCPS·대출 혼합]
        T2_5[Valuation 예비 산정\nEV/EBITDA·PER·DCF]
        T2_6[예비심사 보고서 작성\n2~5페이지]
        T2_1 --> T2_2 --> T2_3 --> T2_4 --> T2_5 --> T2_6
    end

    T2_3 -- "이해충돌 발견" --> T2_CO[준법감시인 즉시 보고\n심사역 배제]
    T2_3 -- "분식회계 정황" --> T2_FR[즉각 중단\n준법감시인 보고]

    T2_6 --> T2_7

    subgraph GRP_TL["팀장"]
        T2_7[예비심사 보고서 검토]
        T2_8[GO / NO-GO 결재]
        T2_7 --> T2_8
    end

    T2_8 -- "NO-GO\n투자매력도 부족" --> OUT2A([예비심사 종결\n반려 통보])
    T2_8 -- "GO" --> T2_9

    subgraph GRP_JR2["심사역 + 준법감시인(필요시)"]
        T2_9[LOI / Term Sheet 초안 작성]
        T2_10[기업 측 발송 & 협의]
        T2_11[펀드 여유 재원 확인\nDD 예산 승인 요청]
        T2_9 --> T2_10 --> T2_11
    end

    T2_10 -- "현장 방문 선택" --> T2_OPT[현장 방문 미팅\n대표이사·CFO 면담]
    T2_OPT --> T2_11

    T2_11 --> DEC_2{LOI 서명 수령 &\nDD 예산 승인?}
    DEC_2 -- "협의 불가\n기업 측 거부" --> OUT2B([보류 또는 반려])
    DEC_2 -- "완료" --> OUT2C([본심사 단계 진입])

    style OUT2A fill:#ffcccc,stroke:#cc0000
    style OUT2B fill:#fff3e0,stroke:#e65100
    style OUT2C fill:#c8e6c9,stroke:#2e7d32
    style IN2 fill:#e3f2fd,stroke:#1565c0
    style T2_CO fill:#ffe0b2,stroke:#e65100
    style T2_FR fill:#ffcccc,stroke:#cc0000
```

**산출 문서**: 예비심사 보고서 / 재무 분석 워크시트(Excel) / LOI·Term Sheet 초안 / GO/NO-GO 결재 기록
**소요기간**: 자료 수집~예비심사 보고서 5~10 영업일 / LOI 발송~기업 회신 3~7 영업일

---

### 2-3. 단계 3: 본심사 — 실사(DD) 및 IC 결의

```mermaid
flowchart TD
    IN3([단계 2 완료\nLOI 서명본 수령]) --> T3_1

    subgraph GRP_DD["DD 팀 (심사역 총괄 + 외부 전문가)"]
        T3_1[DD 팀 구성\n재무·법무·세무·기술 각 담당 지정]
        T3_2[DD 체크리스트 발송\nData Room 요청서 전달]
        T3_3A[재무 DD\n3~5개년 재무제표·정상화 EBITDA]
        T3_3B[법무 DD\n계약·소송·IP·노무·환경]
        T3_3C[세무 DD\n법인세·부가세·이전가격·세무조사]
        T3_3D[사업·시장 DD\n고객·공급자 인터뷰·시장규모]
        T3_1 --> T3_2
        T3_2 --> T3_3A & T3_3B & T3_3C & T3_3D
    end

    T3_3A & T3_3B & T3_3C & T3_3D --> T3_4

    subgraph GRP_JR["심사역 + 팀장"]
        T3_4[DD 결과 통합 & 최종 Valuation 산정\nAdjusted EBITDA 기반]
        T3_5[투자 구조 확정\nCB·BW·RCPS 발행조건·담보·Covenant]
        T3_6[IC Pre-Memo / Full IC Memo 작성]
        T3_4 --> T3_5 --> T3_6
    end

    subgraph GRP_COMP["준법감시인"]
        T3_7[IC 참관 & 규정 준수 확인\n의견서 제출]
    end

    T3_6 --> T3_7

    subgraph GRP_IC["투자심의위원회 IC"]
        T3_8[IC 개최\n대표이사 포함 3인 이상]
        T3_9[안건 심의 & 투표]
        T3_10[결의 의사록 작성\n찬반 수·사유 명문화]
        T3_8 --> T3_9 --> T3_10
    end

    T3_7 --> T3_8
    T3_10 --> DEC_3{IC 결의 결과}

    DEC_3 -- "부결\nIC 과반수 반대" --> OUT3A([투자 부결\n의사록 기록·기업 통보])
    DEC_3 -- "조건부 승인\n추가 조건 부여" --> T3_COND[조건 충족 이행\n팀장 확인]
    T3_COND --> DEC_3B{조건 충족 완료?}
    DEC_3B -- "미충족" --> OUT3B([재심사 또는 부결])
    DEC_3B -- "충족" --> OUT3C([투자 집행 단계 진입])
    DEC_3 -- "승인" --> OUT3C

    style OUT3A fill:#ffcccc,stroke:#cc0000
    style OUT3B fill:#fff3e0,stroke:#e65100
    style OUT3C fill:#c8e6c9,stroke:#2e7d32
    style IN3 fill:#e3f2fd,stroke:#1565c0
```

**산출 문서**: DD 결과 요약 보고서 / IC Pre-Memo·Full IC Memo / IC 결의 의사록 / 확정 Term Sheet
**소요기간**: DD 착수~완료 2~6주 / IC 자료 작성~IC 개최 3~7 영업일 / 전체 4~8주

---

### 2-4. 단계 4: 투자 집행 (Closing)

```mermaid
flowchart TD
    IN4([단계 3 완료\nIC 결의 의사록 & 확정 Term Sheet]) --> T4_1

    subgraph GRP_LAWYER["심사역 + 외부 법무법인"]
        T4_1[투자계약서 초안 작성\nCB인수계약·BW인수계약·SHA]
        T4_2[기업 측 법무대리인과 협상\nNegotiation]
        T4_1 --> T4_2
    end

    T4_2 --> T4_3

    subgraph GRP_CP["심사역 + 준법감시인"]
        T4_3[선행조건 CP 충족 확인\n이사회결의·감사인확인·담보설정]
        T4_4[AML·KYC 자금 출처 확인\n의심거래 시 FIU 보고]
        T4_3 --> T4_4
    end

    T4_4 --> DEC_4A{CP 전 항목 충족?}
    DEC_4A -- "미충족\n기업 측 지연" --> T4_DELAY[Closing 연기 협의\n허용 기간 내 재확인]
    T4_DELAY --> DEC_4A

    DEC_4A -- "충족" --> T4_5

    subgraph GRP_CEO["대표이사 최종 승인"]
        T4_5[최종 계약서 서명 Signing\n대표이사 인감·공증·법무사 확인]
    end

    T4_5 --> T4_6

    subgraph GRP_REG["심사역 + 법무사"]
        T4_6[담보 설정 등기\n근저당권·질권]
        T4_7[CB·BW 발행 등기\n법인등기부 기재]
        T4_6 --> T4_7
    end

    T4_7 --> T4_8

    subgraph GRP_FUND["대표이사 (자금 집행 승인)"]
        T4_8[자금 집행 Closing\n계좌이체·에스크로 해제]
        T4_9[투자 후 등기·금융당국 보고]
        T4_8 --> T4_9
    end

    T4_9 --> T4_10

    subgraph GRP_JR["심사역"]
        T4_10[내부 포트폴리오 장부 등록]
        T4_11[소개인 수수료 Finder's Fee 지급\n세금계산서·원천징수 처리]
        T4_12[클로징 체크리스트 완료본 서명]
        T4_10 --> T4_11 --> T4_12
    end

    T4_12 --> OUT4([사후관리 단계 진입])

    style OUT4 fill:#c8e6c9,stroke:#2e7d32
    style IN4 fill:#e3f2fd,stroke:#1565c0
```

**산출 문서**: 투자계약서 서명본 / 근저당권·질권 설정 등기필증 / CB·BW 증권 원본 / 자금 집행 확인서 / 클로징 체크리스트 완료본
**소요기간**: 계약서 초안~서명 2~4주 / 서명~자금 집행 3~10 영업일

---

### 2-5. 단계 5: 사후관리 (Portfolio Monitoring & EXIT)

```mermaid
flowchart TD
    IN5([단계 4 완료\n투자 집행 완료]) --> T5_1

    subgraph GRP_MON["심사역 (포트폴리오 매니저) — 정기 사이클"]
        T5_1[정기 재무보고 수령\n월별·분기별 재무제표]
        T5_2[Covenant 모니터링\nDSCR·부채비율 분기 점검]
        T5_3[Valuation 업데이트\n반기·연간 공정가치 평가]
        T5_4[현장 방문 Site Visit\n연 1~2회 경영진 면담]
        T5_1 --> T5_2 --> T5_3 --> T5_4 --> T5_1
    end

    T5_2 -- "Covenant 위반 감지" --> DEC_5A{위반 수준}
    DEC_5A -- "경미한 위반" --> T5_WARN[경고 및 시정 요구\n준법감시인 보고]
    T5_WARN --> T5_2
    DEC_5A -- "중대 위반\nDSCR 기준 이하" --> T5_EMRG[긴급 EXIT 프로세스 개시\n워크아웃·Put Option 행사]

    T5_4 -- "중요 이벤트\n연체·소송·대표이사 변경" --> T5_EVENT[이벤트 모니터링 & 대응\nIC 보고]

    subgraph GRP_EXIT["심사역 + IC + 외부 전문가"]
        T5_5[EXIT 전략 수립\nIPO·M&A·CB전환·조기상환 시나리오]
        T5_6[IC EXIT 결의\n방식 및 타이밍 승인]
        T5_7[EXIT 실행\n주식매각·CB전환매각·만기상환]
        T5_5 --> T5_6 --> T5_7
    end

    T5_3 --> T5_5
    T5_EMRG --> T5_7

    subgraph GRP_RPT["팀장 + 대표이사"]
        T5_8[LP 정기 보고서 작성\nIRR·MoM 계산]
        T5_9[분배금 지급 처리]
        T5_10[투자 회수 정산서 작성]
        T5_8 --> T5_9 --> T5_10
    end

    T5_7 --> T5_8
    T5_10 --> OUT5([투자 회수 완료\n딜 종결 기록 보관])

    style OUT5 fill:#c8e6c9,stroke:#2e7d32
    style IN5 fill:#e3f2fd,stroke:#1565c0
    style T5_EMRG fill:#ffcccc,stroke:#cc0000
    style T5_EVENT fill:#ffe0b2,stroke:#e65100
```

**산출 문서**: 포트폴리오 모니터링 보고서(분기) / Covenant 점검표(분기) / Valuation 업데이트 보고서(반기) / EXIT 검토 보고서 / LP 정기 보고서 / 투자 회수 정산서
**소요기간**: 모니터링 주기 월 1회(재무) / 분기 1회(Covenant) / EXIT 준비~완료 3개월~1년 이상

---

## 3. RACI 매트릭스

> 역할 정의: **심사역** = 담당 심사역(Deal Screener·포트폴리오 매니저) / **팀장** = 투자팀장 / **IC** = 투자심의위원회 / **준법** = 준법감시인 / **대표** = 대표이사 / **외부** = 외부 법무·회계·세무 전문가
>
> **R** = Responsible(실행) | **A** = Accountable(책임) | **C** = Consulted(자문) | **I** = Informed(통보)

| # | 주요 활동 | 심사역 | 팀장 | IC | 준법 | 대표 | 외부 |
|---|----------|:------:|:----:|:--:|:----:|:----:|:----:|
| **[단계 1] 투자요청 접수** |
| 1-1 | 딜 소싱 채널 관리 | R | A | - | I | I | - |
| 1-2 | IM·재무제표 등 서류 수령 | R | A | - | - | - | - |
| 1-3 | 1차 적합성 필터링 | R | A | - | C | - | - |
| 1-4 | NDA 체결 | R | A | - | C | I | - |
| 1-5 | 딜 로그 CRM 등록 | R | A | - | - | - | - |
| 1-6 | 담당 심사역 배정 | C | R/A | - | - | I | - |
| 1-7 | 소개인 수수료 조건 확인 | R | A | - | C | I | - |
| **[단계 2] 예비심사** |
| 2-1 | 재무 지표 분석 | R | C | - | - | - | C |
| 2-2 | 신용·법적 리스크 스크리닝 | R | C | - | C | - | C |
| 2-3 | 투자 구조 검토 | R | C | - | C | - | C |
| 2-4 | Valuation 예비 산정 | R | C | I | - | - | C |
| 2-5 | 예비심사 보고서 작성 | R | A | - | - | - | - |
| 2-6 | 팀장 GO/NO-GO 결재 | C | R/A | I | C | - | - |
| 2-7 | LOI / Term Sheet 초안 작성 | R | A | - | C | - | C |
| 2-8 | 펀드 여유 재원 확인 | C | R | I | - | A | - |
| 2-9 | DD 예산 승인 요청 | R | C | - | - | A | - |
| **[단계 3] 본심사 — DD & IC** |
| 3-1 | DD 팀 구성 | R | A | I | C | - | C |
| 3-2 | 재무 DD | R | C | I | - | - | R/C |
| 3-3 | 법무 DD | R | C | I | C | - | R |
| 3-4 | 세무 DD | R | C | I | - | - | R |
| 3-5 | 사업·시장 DD | R | C | I | - | - | C |
| 3-6 | 최종 Valuation 산정 | R | C | C | - | - | C |
| 3-7 | 투자 구조 확정 | R | A | C | C | - | C |
| 3-8 | IC Memo 작성 | R | A | - | - | - | - |
| 3-9 | IC 개최 및 안건 심의 | C | C | R/A | C | R | - |
| 3-10 | IC 결의 의사록 작성 | C | C | R/A | C | I | - |
| 3-11 | 투자 조건부 승인 조건 이행 확인 | R | A | I | C | - | - |
| **[단계 4] 투자 집행** |
| 4-1 | 투자계약서 초안 작성 | R | C | - | C | - | R |
| 4-2 | 계약 협상 | R | A | I | C | - | R |
| 4-3 | 선행조건 CP 충족 확인 | R | A | - | C | - | C |
| 4-4 | AML·KYC 자금 출처 확인 | R | C | - | R/A | - | - |
| 4-5 | 최종 계약서 서명 Signing | R | A | I | C | R/A | C |
| 4-6 | 담보 설정 등기 | R | C | - | C | - | R |
| 4-7 | CB·BW 발행 등기 | R | C | I | C | - | R |
| 4-8 | 자금 집행 Closing | R | A | I | C | R/A | - |
| 4-9 | 내부 포트폴리오 장부 등록 | R | A | I | - | - | - |
| 4-10 | 소개인 수수료 지급 | R | A | - | C | I | - |
| **[단계 5] 사후관리 & EXIT** |
| 5-1 | 정기 재무보고 수령 & 검토 | R | I | - | - | - | - |
| 5-2 | Covenant 모니터링 | R | A | I | C | - | - |
| 5-3 | Valuation 업데이트 | R | A | I | - | - | R |
| 5-4 | 현장 방문 Site Visit | R | C | - | - | I | - |
| 5-5 | 이벤트 모니터링 & 이상징후 대응 | R | A | C | C | I | - |
| 5-6 | Covenant 위반 대응 | R | A | C | R/C | I | C |
| 5-7 | EXIT 전략 수립 | R | A | C | C | I | C |
| 5-8 | EXIT IC 결의 | C | C | R/A | C | R | - |
| 5-9 | EXIT 실행 | R | A | I | C | I | R |
| 5-10 | LP 정기 보고서 작성 | R | A | I | C | R/A | - |
| 5-11 | 투자 회수 정산서 작성 | R | A | I | C | I | C |

---

## 4. 예외 흐름 다이어그램

### 4-1. 투자 반려 프로세스

```mermaid
flowchart TD
    TRIG([반려 트리거 발생]) --> DEC_REJ{반려 발생 단계}

    DEC_REJ -- "단계 1\n1차 필터 미통과" --> REJ1_1[심사역: 반려 사유 체크리스트 작성]
    REJ1_1 --> REJ_COMMON

    DEC_REJ -- "단계 2\n팀장 NO-GO 결재" --> REJ2_1[팀장: 예비심사 종결 결재]
    REJ2_1 --> REJ2_2[심사역: 반려 사유 보고서 작성]
    REJ2_2 --> REJ_COMMON

    DEC_REJ -- "단계 3\nIC 부결" --> REJ3_1[IC: 부결 의사록 작성\n찬반 수 및 사유 명문화]
    REJ3_1 --> REJ3_2[팀장: IC 결의 결과 확인]
    REJ3_2 --> REJ_COMMON

    subgraph REJ_COMMON["공통 반려 처리 절차"]
        R1[딜 로그 CRM에 반려 상태 업데이트]
        R2[기업 측 반려 통보\n서면 또는 이메일]
        R3[반려 사유 기록 보관\n내부 문서화]
        R4[소개인 통보\n해당 시]
        R1 --> R2 --> R3 --> R4
    end

    R4 --> DEC_RECON{향후 재검토 가능성?}
    DEC_RECON -- "없음" --> CLOSE([딜 종결 기록 보관])
    DEC_RECON -- "있음\n조건 개선 시 재접수 가능" --> STANDBY([보류 상태 유지\n재접수 시 단계 1부터])

    style TRIG fill:#ffcccc,stroke:#cc0000
    style CLOSE fill:#e0e0e0,stroke:#757575
    style STANDBY fill:#fff3e0,stroke:#e65100
```

---

### 4-2. 보류 / 재심사 프로세스

```mermaid
flowchart TD
    TRIG2([보류 트리거 발생]) --> DEC_HOLD{보류 사유}

    DEC_HOLD -- "기업 측\n핵심 정보 미제출" --> H1[심사역: 추가 자료 요청 공문 발송]
    H1 --> WAIT1{자료 제출 기한\n내 회신?}
    WAIT1 -- "제출" --> RESUME([해당 단계 재개])
    WAIT1 -- "미제출 (기한 초과)" --> REJECT([반려 처리])

    DEC_HOLD -- "IC 조건부 승인\n추가 조건 부여" --> H2[심사역: 조건 이행 계획서 작성]
    H2 --> H3[기업 측 조건 이행]
    H3 --> WAIT2{팀장 조건 충족\n확인?}
    WAIT2 -- "충족" --> EXEC([집행 단계 진입])
    WAIT2 -- "미충족\n기한 내" --> H3
    WAIT2 -- "미충족\n기한 초과" --> IC_REVOTE[IC 재결의 상정\n부결 또는 조건 변경]

    DEC_HOLD -- "DD 중단\n기업 요청·비용 분쟁" --> H4[팀장·준법감시인 협의\nDD 비용 부담 결정]
    H4 --> WAIT3{협의 결과}
    WAIT3 -- "DD 재개" --> RESUME
    WAIT3 -- "협의 결렬" --> REJECT

    IC_REVOTE --> DEC_IC2{IC 재결의 결과}
    DEC_IC2 -- "승인" --> EXEC
    DEC_IC2 -- "부결" --> REJECT

    style TRIG2 fill:#fff3e0,stroke:#e65100
    style REJECT fill:#ffcccc,stroke:#cc0000
    style RESUME fill:#c8e6c9,stroke:#2e7d32
    style EXEC fill:#c8e6c9,stroke:#2e7d32
```

---

### 4-3. 긴급 EXIT 프로세스

```mermaid
flowchart TD
    ALERT([조기경보 신호 감지]) --> DEC_EMRG{트리거 유형}

    DEC_EMRG -- "Covenant 위반\nDSCR 기준 이하·부채비율 초과" --> E1
    DEC_EMRG -- "대표이사 변경\n경영권 분쟁" --> E1
    DEC_EMRG -- "사업 급격 악화\n매출 30% 이상 급감" --> E1
    DEC_EMRG -- "Put Option 행사 요건 충족" --> E1

    subgraph GRP_IMMED["즉각 대응 (D+1 이내)"]
        E1[심사역: 이상 징후 기록 & 팀장 즉시 보고]
        E2[준법감시인 보고]
        E3[대표이사 보고]
        E1 --> E2 --> E3
    end

    E3 --> E4

    subgraph GRP_ASSESS["긴급 평가 (D+3 이내)"]
        E4[심사역·외부 법무: 계약상 권리 검토\nPut Option·기한이익 상실 조항]
        E5[현장 방문 긴급 실시\n경영진 면담]
        E6[회수 시나리오 긴급 평가\n담보 가치 재산정]
        E4 --> E5 --> E6
    end

    E6 --> DEC_E1{회수 가능성 판단}

    DEC_E1 -- "협력적 해결 가능" --> E7[밸류업 지원 & 워크아웃 협의\n추가 담보·이자율 조정]
    E7 --> WAIT_E{워크아웃 결과}
    WAIT_E -- "정상화" --> NORMAL([정상 사후관리 복귀])
    WAIT_E -- "실패" --> E8

    DEC_E1 -- "즉시 회수 필요" --> E8

    subgraph GRP_IC_EMRG["긴급 IC 개최"]
        E8[긴급 IC 소집\n EXIT 방식 결의]
        E9[대표이사 최종 승인]
        E8 --> E9
    end

    E9 --> DEC_E2{EXIT 방식}

    DEC_E2 -- "조기상환 청구" --> EXIT1[Put Option 행사 통보\n원리금 상환 청구]
    DEC_E2 -- "담보 실행" --> EXIT2[근저당권·질권 실행\n법적 절차 개시]
    DEC_E2 -- "협상 매각" --> EXIT3[M&A 주선\n외부 IB 활용]

    EXIT1 & EXIT2 & EXIT3 --> FINAL[투자 회수 정산\nIRR·손익 계산]
    FINAL --> LP_RPT[LP 특별 보고\n손실 발생 시 즉시 통보]
    LP_RPT --> END_E([긴급 EXIT 종결\n법적·세무 후속 처리])

    style ALERT fill:#ffcccc,stroke:#cc0000
    style END_E fill:#e0e0e0,stroke:#757575
    style NORMAL fill:#c8e6c9,stroke:#2e7d32
    style E8 fill:#ffe0b2,stroke:#e65100
```

---

## 5. 참고: 단계별 소요기간 요약

| 단계 | 최단 | 일반 | 최장 |
|------|------|------|------|
| ① 투자요청 접수 | 1 영업일 | 3~5 영업일 | 10 영업일 |
| ② 예비심사 | 5 영업일 | 10~17 영업일 | 4주 |
| ③ 본심사 — DD & IC | 2주 | 4~6주 | 8주 |
| ④ 투자 집행 | 3주 | 4~6주 | 3개월 |
| ⑤ 사후관리 (투자기간) | 1년 | 3~5년 | 7년 이상 |
| **① ~ ④ 접수~클로징** | **6주** | **12~16주** | **6개월 이상** |

---

## 6. 다이어그램 렌더링 안내

- 본 문서의 Mermaid 코드는 **Mermaid v10+** 기준으로 작성됨.
- 렌더링 환경: GitHub Markdown / Obsidian (Mermaid 플러그인) / VS Code (Markdown Preview Mermaid Support) / [mermaid.live](https://mermaid.live)
- 단일 다이어그램 노드 수: Level 0 = 20개 이하 / Level 1 각 단계 = 15~18개 수준으로 복잡도 관리.
- `subgraph` 레이블에 줄바꿈이 포함된 경우 일부 렌더러에서 `\n` 대신 실제 줄바꿈이 필요할 수 있음 **[렌더러 호환성 현장 검증 필요]**.

---

*본 문서는 `01_document_analysis.md` 기반으로 작성된 초안입니다. 모든 플로차트 및 RACI는 SMB투자파트너스 현장 실무진 검토 후 수정·확정되어야 합니다.*
*면책 문구: 본 매뉴얼은 내부 업무 가이드이며 법적 효력을 갖지 않음.*
