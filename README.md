# BMAD Marketing Team Framework

> **AI-driven marketing automation system that applies software development methodologies to marketing operations**

The BMAD (Brand, Media, Analyst, Designer) Framework enables data-driven marketing decisions through intelligent automation and cross-functional collaboration, supporting both Greenfield (new initiatives) and Brownfield (optimization) marketing scenarios.

There is a korean version: [korean version](./README-ko.md)

## 🚀 Quick Start

### 1. Identify Your Business Type

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

### 2. Set Up Your Team

Assign team members to the four core BMAD roles:

| Role                                     | Responsibilities                                    | Key Skills                                                 |
| ---------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| **Brand Marketer (B)**                   | Brand strategy, content marketing, customer journey | Strategic thinking, storytelling, brand management         |
| **Media Buyer/Performance Marketer (M)** | Paid campaigns, budget optimization, ROI/ROAS       | Analytical skills, platform expertise, data interpretation |
| **Analyst (A)**                          | Data analysis, reporting, forecasting, integration  | Technical skills, statistical analysis, data visualization |
| **Designer (D)**                         | Visual assets, A/B testing, UX optimization         | Design skills, user experience, creative testing           |

### 3. Configure Your Data Sources

Set up integrations based on your business type:

```bash
# Review integration requirements for your business type
python scripts/test_ga4_integration.py
python scripts/supermetrics_pipeline.py
```

### 4. Start with a Workflow

Choose your approach:

- **Greenfield**: New product launches, market expansion
- **Brownfield**: Existing campaign optimization, performance improvement

## 📋 Project Structure

```
BMAD-for-marketing/
├── docs/
│   ├── prd.md                     # Product Requirements Document
│   ├── epics/                     # Epic definitions
│   ├── stories/                   # User stories
│   ├── workflows/                 # Process documentation
│   └── project-planning/          # Planning artifacts
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

**Goal**: Establish team structure and basic workflows

1. **Business Context Assessment** (Week 1)

   ```bash
   # Use our kickoff materials
   open docs/project-planning/kickoff-presentation.md
   open docs/project-planning/role-assignments.md
   ```

2. **Data Integration Planning** (Week 2)

   ```bash
   # Review integration strategy
   open docs/project-planning/data-integration-plan.md
   ```

3. **Workflow Documentation** (Week 3-4)
   ```bash
   # Study the workflows
   open docs/workflows/Greenfield-Workflow.md
   open docs/workflows/Brownfield-Workflow.md
   open docs/workflows/Prompt-Library.md
   ```

### Phase 2: Integration (Weeks 5-8)

**Goal**: Connect data sources and test workflows

1. **GA4 Integration Testing**

   ```bash
   # Set up environment variables
   export GA4_PROPERTY_ID="your-property-id"
   export GA4_CREDENTIALS_PATH="path/to/credentials.json"

   # Test the connection
   python scripts/test_ga4_integration.py
   ```

2. **Supermetrics Pipeline Setup**

   ```bash
   # Configure API credentials
   export SUPERMETRICS_API_KEY="your-api-key"
   export SUPERMETRICS_QUERY_ID="your-query-id"

   # Run the pipeline
   python scripts/supermetrics_pipeline.py
   ```

3. **Cross-role Workflow Testing**
   ```bash
   # Follow the test plan
   open docs/project-planning/workflow-test-plan.md
   ```

### Phase 3: Optimization (Weeks 9-12)

**Goal**: Implement AI-driven insights and automation

1. **AI Insight Generation**

   ```bash
   # Generate insights from your data
   python scripts/generate_insights.py

   # Review generated insights
   cat generated_insights.json
   ```

2. **Automated Reporting**

   ```bash
   # Set up weekly reporting
   python scripts/automated_reporter.py

   # Check the generated report
   open weekly_report.html
   ```

3. **Predictive Model Training**
   ```bash
   # Train your first model
   jupyter notebook notebooks/train_predictive_model.ipynb
   ```

### Phase 4: Scaling (Weeks 13-16)

**Goal**: Expand capabilities and establish continuous improvement

1. **Multi-Business Type Support**

   ```bash
   # Test with different business types
   python scripts/advanced_automation.py
   ```

2. **Predictive Analytics API**

   ```bash
   # Start the prediction service
   python scripts/prediction_api.py

   # Test the API
   curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"spend": 100, "ctr": 0.02}'
   ```

3. **Continuous Improvement Process**
   ```bash
   # Review the improvement framework
   open docs/project-planning/continuous-improvement-process.md
   ```

## 🎯 Business Type Quick Setup

### For SaaS B2B Companies

```yaml
# Your focus metrics
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)
- Churn Rate

# Required integrations
- Google Analytics 4
- CRM (Salesforce, HubSpot)
- Marketing automation platform
- Product analytics (Mixpanel, Amplitude)
```

### For E-commerce Companies

```yaml
# Your focus metrics
- Return on Ad Spend (ROAS)
- Average Order Value (AOV)
- Conversion Rate
- Cart Abandonment Rate

# Required integrations
- Google Analytics 4 Enhanced Ecommerce
- Shopify/WooCommerce
- Email marketing platforms
- Social media advertising
```

### For Other Business Types

Refer to `config/business_types.yaml` for complete configurations including:

- Marketplace platforms
- Mobile apps
- Subscription commerce
- Media & content
- Local businesses
- Education & training

## 🔧 Advanced Features

### Smart Budget Allocation

The framework can automatically suggest budget reallocations based on performance:

```bash
# Run advanced automation
python scripts/advanced_automation.py
```

### Predictive Analytics

Deploy ML models to forecast key metrics:

```bash
# Start the prediction API
python scripts/prediction_api.py

# Make predictions
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"spend": 250, "ctr": 0.025}'
```

### Multi-language Support

The framework supports Korean language interactions. When team members communicate in Korean, AI agents will respond in Korean.

## 📊 Key Performance Indicators

### Team Performance Metrics

- **Brand Marketer**: Brand awareness lift, content engagement rates
- **Media Buyer**: CAC reduction, ROAS improvement, attribution accuracy
- **Analyst**: Data accuracy rate, insight implementation rate, forecast accuracy
- **Designer**: Creative performance improvement, A/B test win rate

### Business Impact Metrics

- Overall marketing ROI improvement
- Customer acquisition cost reduction
- Customer lifetime value increase
- Revenue attribution accuracy

## 🤖 AI-Powered Prompts

Each role has access to specialized AI prompts. Examples:

### Brand Marketer

```
"Analyze current brand perception data from [Source] and provide three recommendations for our positioning strategy as a [Business Type] targeting [Target Market]."
```

### Media Buyer

```
"Given a target CAC of $[Target] for a [Business Type], analyze our current ad spend and recommend budget reallocation to optimize for this goal."
```

### Analyst

```
"Analyze our GA4 data for the last quarter and identify the top 3 traffic sources that lead to conversions."
```

### Designer

```
"Create two new design variations for an ad creative to A/B test on [Platform]. The current CTR is [Current CTR]."
```

## 🔄 Workflows

### Greenfield Workflow (New Initiatives)

1. **Business Context Analysis** → 2. **Market Research** → 3. **Brand Strategy** → 4. **Channel Strategy** → 5. **Creative Development** → 6. **Campaign Launch** → 7. **Performance Monitoring** → 8. **Optimization Loop**

### Brownfield Workflow (Optimization)

1. **Current State Analysis** → 2. **Performance Gap Identification** → 3. **Optimization Hypothesis** → 4. **Test Planning & Execution** → 5. **Results Analysis** → 6. **Implementation & Scaling** → 7. **Continuous Monitoring**

## 📝 Documentation

### Essential Documents

- **[PRD](docs/prd.md)**: Complete product requirements
- **[Workflows](docs/workflows/)**: Detailed process guides
- **[Prompt Library](docs/workflows/Prompt-Library.md)**: Role-specific AI prompts
- **[Business Types](config/business_types.yaml)**: Configuration for different business models

### Planning Materials

- **[Kickoff Presentation](docs/project-planning/kickoff-presentation.md)**: Project introduction
- **[Role Assignments](docs/project-planning/role-assignments.md)**: Team structure
- **[Integration Plan](docs/project-planning/data-integration-plan.md)**: Technical setup
- **[Continuous Improvement](docs/project-planning/continuous-improvement-process.md)**: Enhancement framework

## 🚨 Troubleshooting

### Common Issues

**GA4 Integration Fails**

```bash
# Check credentials
ls -la path/to/your/credentials.json

# Verify property ID
echo $GA4_PROPERTY_ID
```

**Supermetrics Pipeline Errors**

```bash
# Check API key
echo $SUPERMETRICS_API_KEY

# Review error logs in the script output
```

**Model Training Issues**

```bash
# Install required packages
pip install pandas scikit-learn joblib

# Check data format in the notebook
```

## 🤝 Contributing

### Continuous Improvement Process

1. Submit improvement ideas to the backlog
2. Monthly retrospectives and reviews
3. Quarterly strategic assessments
4. Implementation and measurement cycles

### Adding New Business Types

1. Study the `business_type_analysis` framework
2. Define primary metrics and integrations
3. Create role-specific prompts
4. Test with your use case
5. Submit as an improvement

## 📞 Support

### Team Communication

- **Primary Channel**: Slack `#bmad-marketing-project`
- **Documentation**: `docs/` directory
- **Meetings**: Scheduled via calendar with notes in `docs/project-planning`

### Best Practices

- Follow the documented workflows
- Use role-specific prompts consistently
- Review analytics weekly
- Conduct monthly retrospectives
- Maintain documentation updates

---

**Built with the BMAD Method** | **Version 1.0** | **Ready for Production**

> Transform your marketing operations with AI-driven intelligence and proven collaborative frameworks.
