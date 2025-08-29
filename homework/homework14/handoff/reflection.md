# Stage 14 Deployment & Monitoring Reflection for Carvana Project

## Risks if Deployed
The Carvana data pipeline and modeling system face multiple deployment risks. **API failures** (Finnhub or yFinance) could disrupt data ingestion, resulting in stale or missing price series. **HTML structure changes** on scraped sites (Yahoo Finance, Finviz) may break scraping, leading to incomplete or incorrect feature data. **Feature drift** can occur as market conditions evolve, causing model degradation. **High latency** in real-time data fetches could violate SLA, impacting downstream dashboards. **Social media anomalies** (viral events) may skew sentiment-derived features, producing false signals.

## Monitoring Metrics Across Layers
**Data Layer:**
- **Ingestion success rate**: threshold > 98% daily; alerts to Data Engineering upon failure.  
- **Freshness lag**: max 30 min; triggers PagerDuty if exceeded.  
- **Schema validation**: hash changes detected; alert to ML Engineering.

**Model Layer:**
- **Rolling MAE (7-day)** < 0.5 USD; if > 0.5 triggers retraining.  
- **R² score (weekly)** > 0.8; alerts sent to ML Engineering.  
- **Prediction distribution drift** (KL divergence > 0.3); triggers investigation.

**System Layer:**
- **p95 API latency** < 300 ms; on-call notification if > 300 ms.  
- **Error rate** < 1%; escalates to Platform Operations.  
- **Job success rate** for nightly ETL > 99%.

**Business Layer:**
- **Forecast accuracy** deviation < 5%; alert Business Analyst on degradation.  
- **Dashboard usage** (daily active users) > 50; notify Analytics lead if < 50.

## Ownership & Handoffs
- **Data Engineering** owns data pipelines, ingestion alerts, and schema checks.  
- **ML Engineering** responsible for model performance monitoring, drift detection, and retraining pipelines (weekly scheduled retrain or triggered by metric breaches).  
- **Platform Operations** manages system stability, latency/quota alerts, and ETL job monitoring.  
- **Business Analysts** review forecast accuracy and dashboard engagement weekly.  

**Incident Escalation:**  
1. Automated alert → primary on-call (team-specific).  
2. If unresolved in 15 min, escalate to secondary owner.  
3. Critical failures notified to Project Lead and Business Stakeholder.  

All runbooks, SLAs, and rollback procedures reside in `/docs/deployment/` and are linked from the company wiki.