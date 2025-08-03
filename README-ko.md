# BMAD 마케팅 팀 프레임워크

> **마케팅 운영에 소프트웨어 개발 방법론을 적용한 AI 기반 마케팅 자동화 시스템**

BMAD (Brand, Media, Analyst, Designer) 프레임워크는 지능형 자동화와 팀 간 협업을 통해 데이터 기반의 마케팅 의사결정을 가능하게 하며, Greenfield(새로운 이니셔티브)와 Brownfield(기존 최적화) 마케팅 시나리오를 모두 지원합니다.

## 🚀 빠른 시작

### 1. 비즈니스 유형 식별

비즈니스 유형 분석을 통해 설정을 결정하세요:

```bash
# 사용 가능한 비즈니스 유형 검토
cat config/business_types.yaml
```

**다음 핵심 질문에 답하세요:**

- 회사는 주로 어떻게 수익을 창출하나요?
- 주요 고객은 누구인가요 (B2B/B2C)?
- 일반적인 영업 사이클은 얼마나 긴가요?
- 가장 중요한 전환 이벤트는 무엇인가요?

### 2. 팀 구성

네 가지 핵심 BMAD 역할에 팀원을 배정하세요:

| 역할                                  | 책임                                  | 핵심 스킬                                     |
| ------------------------------------- | ------------------------------------- | --------------------------------------------- |
| **브랜드 마케터 (B)**                 | 브랜드 전략, 콘텐츠 마케팅, 고객 여정 | 전략적 사고, 스토리텔링, 브랜드 관리          |
| **미디어 바이어/퍼포먼스 마케터 (M)** | 유료 캠페인, 예산 최적화, ROI/ROAS    | 분석 능력, 플랫폼 전문성, 데이터 해석         |
| **애널리스트 (A)**                    | 데이터 분석, 리포팅, 예측, 통합       | 기술적 능력, 통계 분석, 데이터 시각화         |
| **디자이너 (D)**                      | 시각적 자산, A/B 테스팅, UX 최적화    | 디자인 스킬, 사용자 경험, 크리에이티브 테스팅 |

### 3. 데이터 소스 구성

비즈니스 유형에 따라 통합을 설정하세요:

```bash
# 비즈니스 유형별 통합 요구사항 검토
python scripts/test_ga4_integration.py
python scripts/supermetrics_pipeline.py
```

### 4. 워크플로우로 시작

접근 방식을 선택하세요:

- **Greenfield**: 신제품 출시, 시장 확장
- **Brownfield**: 기존 캠페인 최적화, 성과 개선

## 📋 프로젝트 구조

```
BMAD-for-marketing/
├── docs/
│   ├── prd.md                     # 제품 요구사항 문서
│   ├── epics/                     # 에픽 정의
│   ├── stories/                   # 사용자 스토리
│   ├── workflows/                 # 프로세스 문서
│   └── project-planning/          # 계획 산출물
├── scripts/
│   ├── test_ga4_integration.py    # GA4 API 테스팅
│   ├── supermetrics_pipeline.py   # 데이터 통합
│   ├── generate_insights.py       # AI 기반 분석
│   ├── automated_reporter.py      # 주간 리포팅
│   ├── advanced_automation.py     # 스마트 예산 배분
│   └── prediction_api.py          # 예측 분석 API
├── config/
│   └── business_types.yaml        # 비즈니스 유형 설정
├── notebooks/
│   └── train_predictive_model.ipynb # ML 모델 훈련
└── README.md                      # 이 파일
```

## 🛠️ 구현 가이드

### 1단계: 기반 구축 (1-4주)

**목표**: 팀 구조와 기본 워크플로우 구축

1. **비즈니스 컨텍스트 평가** (1주차)

   ```bash
   # 킥오프 자료 사용
   open docs/project-planning/kickoff-presentation.md
   open docs/project-planning/role-assignments.md
   ```

2. **데이터 통합 계획** (2주차)

   ```bash
   # 통합 전략 검토
   open docs/project-planning/data-integration-plan.md
   ```

3. **워크플로우 문서화** (3-4주차)
   ```bash
   # 워크플로우 학습
   open docs/workflows/Greenfield-Workflow.md
   open docs/workflows/Brownfield-Workflow.md
   open docs/workflows/Prompt-Library.md
   ```

### 2단계: 통합 (5-8주)

**목표**: 데이터 소스 연결 및 워크플로우 테스트

1. **GA4 통합 테스팅**

   ```bash
   # 환경 변수 설정
   export GA4_PROPERTY_ID="your-property-id"
   export GA4_CREDENTIALS_PATH="path/to/credentials.json"

   # 연결 테스트
   python scripts/test_ga4_integration.py
   ```

2. **Supermetrics 파이프라인 설정**

   ```bash
   # API 자격증명 설정
   export SUPERMETRICS_API_KEY="your-api-key"
   export SUPERMETRICS_QUERY_ID="your-query-id"

   # 파이프라인 실행
   python scripts/supermetrics_pipeline.py
   ```

3. **교차 역할 워크플로우 테스팅**
   ```bash
   # 테스트 계획 따르기
   open docs/project-planning/workflow-test-plan.md
   ```

### 3단계: 최적화 (9-12주)

**목표**: AI 기반 인사이트 및 자동화 구현

1. **AI 인사이트 생성**

   ```bash
   # 데이터에서 인사이트 생성
   python scripts/generate_insights.py

   # 생성된 인사이트 검토
   cat generated_insights.json
   ```

2. **자동 리포팅**

   ```bash
   # 주간 리포팅 설정
   python scripts/automated_reporter.py

   # 생성된 리포트 확인
   open weekly_report.html
   ```

3. **예측 모델 훈련**
   ```bash
   # 첫 번째 모델 훈련
   jupyter notebook notebooks/train_predictive_model.ipynb
   ```

### 4단계: 확장 (13-16주)

**목표**: 기능 확장 및 지속적 개선 체계 구축

1. **다중 비즈니스 유형 지원**

   ```bash
   # 다양한 비즈니스 유형으로 테스트
   python scripts/advanced_automation.py
   ```

2. **예측 분석 API**

   ```bash
   # 예측 서비스 시작
   python scripts/prediction_api.py

   # API 테스트
   curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"spend": 100, "ctr": 0.02}'
   ```

3. **지속적 개선 프로세스**
   ```bash
   # 개선 프레임워크 검토
   open docs/project-planning/continuous-improvement-process.md
   ```

## 🎯 비즈니스 유형별 빠른 설정

### SaaS B2B 회사용

```yaml
# 집중 지표
- 월간 반복 수익 (MRR)
- 고객 획득 비용 (CAC)
- 고객 생애 가치 (CLV)
- 이탈률

# 필수 통합
- Google Analytics 4
- CRM (Salesforce, HubSpot)
- 마케팅 자동화 플랫폼
- 제품 분석 (Mixpanel, Amplitude)
```

### 이커머스 회사용

```yaml
# 집중 지표
- 광고 투자 수익률 (ROAS)
- 평균 주문 가치 (AOV)
- 전환율
- 장바구니 이탈률

# 필수 통합
- Google Analytics 4 Enhanced Ecommerce
- Shopify/WooCommerce
- 이메일 마케팅 플랫폼
- 소셜 미디어 광고
```

### 기타 비즈니스 유형

다음을 포함한 완전한 설정은 `config/business_types.yaml`을 참조하세요:

- 마켓플레이스 플랫폼
- 모바일 앱
- 구독 커머스
- 미디어 & 콘텐츠
- 로컬 비즈니스
- 교육 & 훈련

## 🔧 고급 기능

### 스마트 예산 배분

프레임워크는 성과를 기반으로 예산 재배분을 자동으로 제안할 수 있습니다:

```bash
# 고급 자동화 실행
python scripts/advanced_automation.py
```

### 예측 분석

핵심 지표를 예측하는 ML 모델을 배포하세요:

```bash
# 예측 API 시작
python scripts/prediction_api.py

# 예측 만들기
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"spend": 250, "ctr": 0.025}'
```

### 다국어 지원

프레임워크는 한국어 상호작용을 지원합니다. 팀원이 한국어로 소통하면 AI 에이전트가 한국어로 응답합니다.

## 📊 핵심 성과 지표

### 팀 성과 지표

- **브랜드 마케터**: 브랜드 인지도 향상, 콘텐츠 참여율
- **미디어 바이어**: CAC 감소, ROAS 개선, 어트리뷰션 정확도
- **애널리스트**: 데이터 정확도율, 인사이트 구현율, 예측 정확도
- **디자이너**: 크리에이티브 성과 개선, A/B 테스트 승률

### 비즈니스 임팩트 지표

- 전체 마케팅 ROI 개선
- 고객 획득 비용 감소
- 고객 생애 가치 증가
- 수익 어트리뷰션 정확도

## 🤖 AI 기반 프롬프트

각 역할은 전문화된 AI 프롬프트에 접근할 수 있습니다. 예시:

### 브랜드 마케터

```
"[소스]의 현재 브랜드 인식 데이터를 분석하고 [타겟 시장]을 대상으로 하는 [비즈니스 유형]의 포지셔닝 전략에 대한 세 가지 추천사항을 제공하세요."
```

### 미디어 바이어

```
"[비즈니스 유형]의 목표 CAC $[타겟]을 고려하여 현재 광고 지출을 분석하고 이 목표를 최적화하기 위한 예산 재배분을 추천하세요."
```

### 애널리스트

```
"지난 분기 GA4 데이터를 분석하고 전환으로 이어지는 상위 3개 트래픽 소스를 식별하세요."
```

### 디자이너

```
"[플랫폼]에서 A/B 테스트할 광고 크리에이티브의 두 가지 새로운 디자인 변형을 만드세요. 현재 CTR은 [현재 CTR]입니다."
```

## 🔄 워크플로우

### Greenfield 워크플로우 (새로운 이니셔티브)

1. **비즈니스 컨텍스트 분석** → 2. **시장 조사** → 3. **브랜드 전략** → 4. **채널 전략** → 5. **크리에이티브 개발** → 6. **캠페인 론칭** → 7. **성과 모니터링** → 8. **최적화 루프**

### Brownfield 워크플로우 (최적화)

1. **현재 상태 분석** → 2. **성과 격차 식별** → 3. **최적화 가설** → 4. **테스트 계획 & 실행** → 5. **결과 분석** → 6. **구현 & 확장** → 7. **지속적 모니터링**

## 📝 문서

### 필수 문서

- **[PRD](docs/prd.md)**: 완전한 제품 요구사항
- **[워크플로우](docs/workflows/)**: 상세한 프로세스 가이드
- **[프롬프트 라이브러리](docs/workflows/Prompt-Library.md)**: 역할별 AI 프롬프트
- **[비즈니스 유형](config/business_types.yaml)**: 다양한 비즈니스 모델을 위한 설정

### 계획 자료

- **[킥오프 프레젠테이션](docs/project-planning/kickoff-presentation.md)**: 프로젝트 소개
- **[역할 배정](docs/project-planning/role-assignments.md)**: 팀 구조
- **[통합 계획](docs/project-planning/data-integration-plan.md)**: 기술적 설정
- **[지속적 개선](docs/project-planning/continuous-improvement-process.md)**: 향상 프레임워크

## 🚨 문제 해결

### 일반적인 문제

**GA4 통합 실패**

```bash
# 자격증명 확인
ls -la path/to/your/credentials.json

# 속성 ID 확인
echo $GA4_PROPERTY_ID
```

**Supermetrics 파이프라인 오류**

```bash
# API 키 확인
echo $SUPERMETRICS_API_KEY

# 스크립트 출력의 오류 로그 검토
```

**모델 훈련 문제**

```bash
# 필요한 패키지 설치
pip install pandas scikit-learn joblib

# 노트북에서 데이터 형식 확인
```

## 🤝 기여하기

### 지속적 개선 프로세스

1. 백로그에 개선 아이디어 제출
2. 월간 회고 및 검토
3. 분기별 전략적 평가
4. 구현 및 측정 사이클

### 새로운 비즈니스 유형 추가

1. `business_type_analysis` 프레임워크 연구
2. 주요 지표 및 통합 정의
3. 역할별 프롬프트 생성
4. 사용 사례로 테스트
5. 개선사항으로 제출

## 📞 지원

### 팀 커뮤니케이션

- **주요 채널**: Slack `#bmad-marketing-project`
- **문서**: `docs/` 디렉토리
- **회의**: 캘린더를 통해 예약, `docs/project-planning`에 회의록

### 모범 사례

- 문서화된 워크플로우 따르기
- 역할별 프롬프트 일관되게 사용
- 주간 분석 검토
- 월간 회고 실시
- 문서 업데이트 유지

---

**BMAD 메서드로 구축** | **버전 1.0** | **프로덕션 준비 완료**

> AI 기반 인텔리전스와 검증된 협업 프레임워크로 마케팅 운영을 혁신하세요.
