# BMAD Marketing Team Framework

> **AI-driven marketing automation system that applies software development methodologies to marketing operations**

The BMAD (https://github.com/bmadcode/BMAD-METHOD) Framework enables data-driven marketing decisions through intelligent automation and cross-functional collaboration, supporting both Greenfield (new initiatives) and Brownfield (optimization) marketing scenarios.

There is a korean version: [korean version](./README-ko.md)

## 🚀 Quick Start

### 1. Choose Your Marketing Team Approach

The BMAD framework provides **AI-powered marketing agents** that work as an integrated team:

```bash
# Activate marketing agents individually
@brand-marketer    # Sofia - Brand Marketing Strategist 🎨
@media-buyer       # Marcus - Performance Marketing Specialist 📊
@marketing-analyst # Elena - Marketing Data Analyst 📈
@marketing-designer # Maya - Creative Marketing Designer 🎨
```

### 2. Identify Your Business Type

Use our business type analysis to determine your configuration:

```bash
# Review available business types
cat config/business_types.yaml
```

**Answer these key questions:**

- How does your company primarily make money?
- Who are your primary customers (B2B/B2C)?
- How long is your typical sales cycle?
- What are your most important conversion events?

### 3. Start with Your Marketing Team

The four AI agents work together as an integrated marketing team:

| Agent                 | Name      | Role                             | Primary Commands                                               |
| --------------------- | --------- | -------------------------------- | -------------------------------------------------------------- |
| `@brand-marketer`     | Sofia 🎨  | Brand Marketing Strategist       | `*brand-strategy`, `*content-calendar`, `*brand-launch`        |
| `@media-buyer`        | Marcus 📊 | Performance Marketing Specialist | `*campaign-plan`, `*campaign-optimize`, `*audience-analysis`   |
| `@marketing-analyst`  | Elena 📈  | Marketing Data Analyst           | `*analytics-report`, `*data-analysis`, `*attribution-modeling` |
| `@marketing-designer` | Maya 🎨   | Creative Marketing Designer      | `*design-brief`, `*creative-review`, `*asset-optimization`     |

## 🤖 Marketing Agents Guide

### 🎨 Brand Marketing Strategist (@brand-marketer)

**Sofia** helps with brand strategy, content marketing, and customer journey design.

**Key Commands:**

- `*brand-strategy` - Develop comprehensive brand positioning and messaging
- `*brand-analysis` - Analyze current brand perception and competitive landscape
- `*content-calendar` - Create strategic content planning aligned with objectives
- `*brand-launch` - Execute systematic brand launch process
- `*competitive-research` - Deep competitive analysis for positioning

**Example Usage:**

```bash
@brand-marketer
*brand-strategy SaaS B2B "enterprise security software"

# 브랜드 전략을 개발해 주세요 (Korean example)
@brand-marketer
*brand-strategy
```

### 📊 Performance Marketing Specialist (@media-buyer)

**Marcus** optimizes paid campaigns, manages budgets, and improves ROAS.

**Key Commands:**

- `*campaign-plan` - Develop comprehensive paid advertising strategy
- `*campaign-optimize` - Analyze and optimize existing campaign performance
- `*audience-analysis` - Research and develop target audience segments
- `*attribution-setup` - Implement tracking and attribution modeling
- `*budget-planning` - Create strategic budget allocation plans

**Example Usage:**

```bash
@media-buyer
*campaign-plan "Q4 Holiday Campaign" ecommerce 50000 "increase_sales"

# Facebook 캠페인을 최적화해 주세요 (Korean example)
@media-buyer
*campaign-optimize
```

### 📈 Marketing Data Analyst (@marketing-analyst)

**Elena** transforms data into actionable insights and builds performance dashboards.

**Key Commands:**

- `*analytics-report` - Generate comprehensive marketing performance reports
- `*data-analysis` - Conduct deep-dive analysis on specific questions
- `*attribution-modeling` - Build and optimize attribution models
- `*dashboard-setup` - Design and implement performance dashboards
- `*predictive-analysis` - Create forecasting models for key metrics

**Example Usage:**

```bash
@marketing-analyst
*analytics-report "monthly" "Q3_2024" "saas_b2b"

# ROI 분석 리포트를 만들어 주세요 (Korean example)
@marketing-analyst
*analytics-report
```

### 🎨 Creative Marketing Designer (@marketing-designer)

**Maya** creates high-converting creative assets and optimizes visual performance.

**Key Commands:**

- `*design-brief` - Create comprehensive design briefs for projects
- `*creative-review` - Systematic review of creative assets for optimization
- `*design-system` - Develop brand-consistent design systems
- `*creative-testing` - Design and analyze A/B test variations
- `*asset-optimization` - Optimize existing creative assets for performance

**Example Usage:**

```bash
@marketing-designer
*design-brief "Facebook Ads" "Holiday Campaign" "ecommerce"

# 광고 크리에이티브를 디자인해 주세요 (Korean example)
@marketing-designer
*design-brief
```

## 🔄 Team Collaboration Workflows

### Integrated Marketing Campaign Example

```bash
# 1. Brand Strategy (Sofia)
@brand-marketer
*brand-strategy "New Product Launch" "SaaS B2B"

# 2. Campaign Planning (Marcus)
@media-buyer
*campaign-plan "Product Launch Campaign" saas_b2b 25000 "generate_leads"

# 3. Creative Development (Maya)
@marketing-designer
*design-brief "Landing Page" "Product Launch" "saas_b2b"

# 4. Performance Setup (Elena)
@marketing-analyst
*attribution-setup "saas_b2b" "trial_signup,demo_request" "first_touch"

# 5. Campaign Launch & Optimization Loop
@media-buyer
*campaign-optimize "launch_campaign" "week_1" "improve_cac"

@marketing-analyst
*analytics-report "weekly" "campaign_week_1" "saas_b2b"
```

### Cross-Agent Communication

The agents are designed to work together:

- **Brand → Media**: Sofia provides messaging that Marcus uses in campaigns
- **Media → Analyst**: Marcus shares performance data that Elena analyzes
- **Analyst → Designer**: Elena provides insights that Maya uses for optimization
- **Designer → Media**: Maya creates assets that Marcus tests and optimizes

## 📋 Project Structure

```
BMAD-for-marketing/
├── .bmad-core/                  # Hidden agent system
│   ├── agents/                  # AI marketing team agents
│   │   ├── brand-marketer.md    # Sofia - Brand strategist
│   │   ├── media-buyer.md       # Marcus - Performance marketer
│   │   ├── marketing-analyst.md # Elena - Data analyst
│   │   └── marketing-designer.md # Maya - Creative designer
│   ├── tasks/                   # Agent task definitions
│   ├── templates/               # Document templates
│   ├── checklists/             # Quality assurance
│   └── data/                   # Shared data resources
├── docs/
│   ├── prd.md                  # Product Requirements Document
│   ├── epics/                  # Epic definitions
│   ├── stories/                # User stories
│   ├── workflows/              # Process documentation
│   └── project-planning/       # Planning artifacts
├── scripts/
│   ├── test_ga4_integration.py    # GA4 API testing
│   ├── supermetrics_pipeline.py   # Data consolidation
│   ├── generate_insights.py       # AI-driven analysis
│   ├── automated_reporter.py      # Weekly reporting
│   ├── advanced_automation.py     # Smart budget allocation
│   └── prediction_api.py          # Predictive analytics API
├── config/
│   └── business_types.yaml        # Business type configurations
├── notebooks/
│   └── train_predictive_model.ipynb # ML model training
└── README.md                      # This file
```

## 🛠️ Implementation Guide

### Phase 1: Foundation (Weeks 1-4)

**Goal**: Set up your AI marketing team and basic workflows

1. **Team Setup** (Week 1)

   ```bash
   # Test your marketing agents
   @brand-marketer
   *help

   @media-buyer
   *help

   @marketing-analyst
   *help

   @marketing-designer
   *help
   ```

2. **Business Context Assessment** (Week 2)

   ```bash
   # Use our kickoff materials
   open docs/project-planning/kickoff-presentation.md
   open docs/project-planning/role-assignments.md

   # Let Sofia help with brand analysis
   @brand-marketer
   *brand-analysis "YourCompany" "saas_b2b" "competitive_analysis"
   ```

3. **Data Integration Planning** (Week 3)

   ```bash
   # Review integration strategy
   open docs/project-planning/data-integration-plan.md

   # Set up tracking with Elena
   @marketing-analyst
   *attribution-setup
   ```

4. **Workflow Documentation** (Week 4)
   ```bash
   # Study the workflows
   open docs/workflows/Greenfield-Workflow.md
   open docs/workflows/Brownfield-Workflow.md
   open docs/workflows/Prompt-Library.md
   ```

### Phase 2: Integration (Weeks 5-8)

**Goal**: Connect data sources and test agent workflows

1. **Campaign Planning with Marcus**

   ```bash
   @media-buyer
   *campaign-plan "Test Campaign" "your_business_type" 5000 "test_tracking"
   ```

2. **Creative Development with Maya**

   ```bash
   @marketing-designer
   *design-brief "Test Ads" "Test Campaign" "your_business_type"
   ```

3. **Performance Monitoring with Elena**
   ```bash
   @marketing-analyst
   *dashboard-setup "marketing_team" "cac,roas,conversion_rate" "daily"
   ```

### Phase 3: Optimization (Weeks 9-12)

**Goal**: Implement AI-driven insights and optimization

1. **Performance Analysis Loop**

   ```bash
   # Weekly performance review
   @marketing-analyst
   *analytics-report "weekly" "current_week" "your_business_type"

   # Campaign optimization
   @media-buyer
   *campaign-optimize "current_campaigns" "weekly" "improve_roas"

   # Creative optimization
   @marketing-designer
   *asset-optimization "current_creatives" "performance_data" "increase_ctr"
   ```

2. **Brand Development**

   ```bash
   # Content strategy development
   @brand-marketer
   *content-calendar "monthly" "your_business_type" "awareness,consideration,conversion"
   ```

3. **Predictive Analytics**
   ```bash
   # Advanced forecasting
   @marketing-analyst
   *predictive-analysis "lead_generation" "30_days" "spend,seasonality,competition"
   ```

### Phase 4: Scaling (Weeks 13-16)

**Goal**: Expand capabilities and establish continuous improvement

1. **Advanced Campaign Management**

   ```bash
   # Multi-channel strategy
   @media-buyer
   *channel-strategy "omnichannel" "facebook,google,linkedin" "enterprise_b2b"
   ```

2. **Comprehensive Brand Building**

   ```bash
   # Brand system development
   @brand-marketer
   *story-framework "customer_journey" "enterprise_personas" "thought_leadership"
   ```

3. **Design System Scaling**

   ```bash
   # Scalable creative system
   @marketing-designer
   *design-system "YourBrand" "saas_b2b" "web,mobile,social,email"
   ```

## 🎯 Business Type Quick Setup

### For SaaS B2B Companies

```bash
# Quick setup for SaaS B2B
@brand-marketer
*brand-strategy "YourSaaS" "enterprise_software" "saas_b2b"

@media-buyer
*campaign-plan "Lead Generation" "saas_b2b" 20000 "demo_requests"

@marketing-analyst
*attribution-setup "saas_b2b" "trial_signup,demo_request,purchase" "multi_touch"

@marketing-designer
*design-brief "Landing Pages" "Lead Gen Campaign" "saas_b2b"
```

### For E-commerce Companies

```bash
# Quick setup for E-commerce
@brand-marketer
*brand-analysis "YourStore" "ecommerce" "brand_positioning"

@media-buyer
*campaign-plan "Holiday Sales" "ecommerce" 50000 "purchase_conversions"

@marketing-analyst
*dashboard-setup "ecommerce_team" "roas,aov,conversion_rate,cart_abandonment" "realtime"

@marketing-designer
*creative-testing "product_ads" "current_creatives" "holiday_budget"
```

### For Other Business Types

Refer to `config/business_types.yaml` for complete configurations including:

- Marketplace platforms
- Mobile apps
- Subscription commerce
- Media & content
- Local businesses
- Education & training

## 🔧 Advanced Team Features

### Korean Language Support

All marketing agents support Korean interactions:

```bash
# Korean example - 브랜드 전략 개발
@brand-marketer
새로운 제품의 브랜드 전략을 만들어 주세요

# Korean example - 캠페인 최적화
@media-buyer
Facebook 광고 성과가 좋지 않아요. 최적화 방법을 알려주세요

# Korean example - 데이터 분석
@marketing-analyst
지난 달 마케팅 성과를 분석해 주세요

# Korean example - 디자인 개선
@marketing-designer
현재 광고 크리에이티브의 성과를 개선하고 싶어요
```

### Agent Collaboration Patterns

**Campaign Launch Pattern:**

```bash
# 1. Strategy → 2. Planning → 3. Creative → 4. Analytics → 5. Optimization
@brand-marketer → @media-buyer → @marketing-designer → @marketing-analyst → @media-buyer
```

**Optimization Pattern:**

```bash
# 1. Analysis → 2. Insights → 3. Creative → 4. Testing → 5. Scaling
@marketing-analyst → @media-buyer → @marketing-designer → @media-buyer → @brand-marketer
```

**Brand Development Pattern:**

```bash
# 1. Brand Strategy → 2. Content → 3. Creative System → 4. Performance
@brand-marketer → @brand-marketer → @marketing-designer → @marketing-analyst
```

## 📊 Key Performance Indicators

### Agent-Specific Metrics

- **Sofia (Brand)**: Brand awareness lift, content engagement rates, brand sentiment improvement
- **Marcus (Media)**: CAC reduction, ROAS improvement, attribution accuracy, budget efficiency
- **Elena (Analyst)**: Data accuracy rate, insight implementation rate, forecast accuracy
- **Maya (Designer)**: Creative performance improvement, A/B test win rate, conversion rate optimization

### Business Impact Metrics

- Overall marketing ROI improvement
- Customer acquisition cost reduction
- Customer lifetime value increase
- Revenue attribution accuracy
- Campaign launch speed improvement
- Cross-team collaboration efficiency

## 🤖 Agent Command Reference

### Complete Command List

**Brand Marketer (@brand-marketer) - Sofia 🎨**

```bash
*brand-analysis      # Comprehensive brand analysis
*brand-strategy      # Brand positioning and messaging
*content-calendar    # Strategic content planning
*brand-launch        # Brand launch execution
*competitive-research # Competitive analysis
*content-strategy    # Content strategy development
*brand-audit        # Brand audit and assessment
*voice-tone         # Brand voice guidelines
*story-framework    # Brand storytelling
*social-strategy    # Social media strategy
*brand-metrics      # Brand performance tracking
```

**Media Buyer (@media-buyer) - Marcus 📊**

```bash
*campaign-plan      # Campaign strategy development
*campaign-optimize  # Performance optimization
*audience-analysis  # Audience research and targeting
*creative-testing   # A/B testing setup
*attribution-setup  # Tracking implementation
*budget-planning    # Budget allocation strategy
*channel-strategy   # Multi-channel planning
*bid-optimization   # Bidding strategy optimization
*conversion-audit   # Conversion tracking audit
*competitor-analysis # Competitive advertising analysis
*performance-report # Performance reporting
```

**Marketing Analyst (@marketing-analyst) - Elena 📈**

```bash
*analytics-report   # Comprehensive reporting
*data-analysis      # Deep-dive analysis
*attribution-modeling # Attribution model development
*predictive-analysis # Forecasting and prediction
*dashboard-setup    # Performance dashboard creation
*customer-segmentation # Customer analysis
*cohort-analysis    # Retention analysis
*ab-test-analysis   # Statistical test analysis
*funnel-analysis    # Conversion funnel optimization
*roi-analysis       # ROI measurement
*competitive-analysis # Market analysis
*data-integration   # Data source integration
```

**Marketing Designer (@marketing-designer) - Maya 🎨**

```bash
*design-brief       # Creative project planning
*creative-review    # Asset review and optimization
*design-system      # Design system development
*creative-testing   # Design A/B testing
*asset-optimization # Creative performance optimization
*create-creative    # Creative asset development
*landing-page-design # Landing page optimization
*brand-assets       # Brand material creation
*email-design       # Email template design
*social-media-design # Social creative development
*ad-creative        # Advertising creative design
*mobile-optimization # Mobile design optimization
```

## 🔄 Workflows

### Greenfield Workflow (New Initiatives)

1. **Brand Foundation** (`@brand-marketer *brand-strategy`)
2. **Market Research** (`@marketing-analyst *competitive-analysis`)
3. **Campaign Strategy** (`@media-buyer *campaign-plan`)
4. **Creative Development** (`@marketing-designer *design-brief`)
5. **Performance Setup** (`@marketing-analyst *attribution-setup`)
6. **Campaign Launch** (`@media-buyer *campaign-plan`)
7. **Performance Monitoring** (`@marketing-analyst *analytics-report`)
8. **Optimization Loop** (All agents collaborating)

### Brownfield Workflow (Optimization)

1. **Performance Analysis** (`@marketing-analyst *analytics-report`)
2. **Gap Identification** (`@media-buyer *campaign-optimize`)
3. **Creative Optimization** (`@marketing-designer *asset-optimization`)
4. **Testing Strategy** (`@marketing-designer *creative-testing`)
5. **Implementation** (`@media-buyer *campaign-optimize`)
6. **Results Analysis** (`@marketing-analyst *data-analysis`)
7. **Scaling Strategy** (`@brand-marketer *brand-metrics`)

## 📝 Documentation

### Essential Documents

- **[PRD](docs/prd.md)**: Complete product requirements
- **[Workflows](docs/workflows/)**: Detailed process guides
- **[Prompt Library](docs/workflows/Prompt-Library.md)**: Role-specific AI prompts
- **[Business Types](config/business_types.yaml)**: Configuration for different business models

### Agent Documentation

- **[Agent Guide](.bmad-core/agents/)**: Individual agent definitions and capabilities
- **[Task Library](.bmad-core/tasks/)**: Executable workflows and methodologies
- **[Template Library](.bmad-core/templates/)**: Document and planning templates
- **[Checklist Library](.bmad-core/checklists/)**: Quality assurance and review processes

### Planning Materials

- **[Kickoff Presentation](docs/project-planning/kickoff-presentation.md)**: Project introduction
- **[Role Assignments](docs/project-planning/role-assignments.md)**: Team structure
- **[Integration Plan](docs/project-planning/data-integration-plan.md)**: Technical setup
- **[Continuous Improvement](docs/project-planning/continuous-improvement-process.md)**: Enhancement framework

## 🚨 Troubleshooting

### Agent Issues

**Agent Not Responding**

```bash
# Check agent activation
@brand-marketer
*help

# Try exit and reactivate
@brand-marketer
*exit
@brand-marketer
```

**Korean Language Issues**

```bash
# Agents automatically detect Korean and respond in Korean
# Test with simple Korean greeting
@brand-marketer
안녕하세요
```

**Command Not Found**

```bash
# Check available commands
@media-buyer
*help

# Use flexible command matching
@media-buyer
캠페인 최적화 도움이 필요해요
```

### Technical Issues

**Data Integration Fails**

```bash
# Check credentials
ls -la path/to/your/credentials.json

# Verify property ID
echo $GA4_PROPERTY_ID
```

**Performance Issues**

```bash
# Check system resources
# Ensure only necessary agents are active
@agent-name
*exit
```

## 🤝 Contributing

### Continuous Improvement Process

1. Submit improvement ideas to the backlog
2. Monthly retrospectives with AI marketing team
3. Quarterly strategic assessments
4. Implementation and measurement cycles

### Adding New Marketing Capabilities

1. Study existing agent patterns in `.bmad-core/agents/`
2. Create new tasks in `.bmad-core/tasks/`
3. Add templates in `.bmad-core/templates/`
4. Test with your marketing use case
5. Submit as an improvement

## 📞 Support

### Team Communication

- **Primary Channel**: Slack `#bmad-marketing-project`
- **Agent Support**: Use `*help` command with any agent
- **Documentation**: `docs/` directory and `.bmad-core/` system
- **Meetings**: Scheduled via calendar with notes in `docs/project-planning`

### Best Practices

- Start each session by activating the agents you need
- Use `*help` to see available commands for each agent
- Leverage Korean language support for Korean-speaking team members
- Follow documented workflows for complex marketing projects
- Conduct regular performance reviews with Elena (`@marketing-analyst`)
- Maintain brand consistency through Sofia (`@brand-marketer`)

---

**Built with the BMAD Method** | **Version 2.0** | **AI Marketing Team Ready**

> Transform your marketing operations with AI-powered team collaboration and proven strategic frameworks.
