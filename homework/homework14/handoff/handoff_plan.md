# Carvana Project Handoff Plan

1. **Staging Validation**: Deploy scraping and ingestion code to staging; run daily batch in shadow mode for 3 days.  
2. **Canary Release**: Activate model service for 10% of requests with full monitoring enabled; observe for 48 hours.  
3. **Full Production Rollout**: Gradually increase traffic in 25% increments every 24 hours, verifying key metrics at each step.  
4. **Rollback Criteria**: Auto-rollback if ingestion success rate < 95% for 15 min, p95 latency > 500 ms for 10 min, or rolling MAE > 1.0 USD for 1 hour.  
5. **Retraining Schedule**: Weekly at 02:00 UTC if MAE > 0.5 or R² < 0.8 triggers retraining pipeline.  
6. **Alerts & Runbook Links**:  
   - **Data Ingestion Failures**: `/docs/runbooks/ingestion-failure.md`  
   - **Model Drift**: `/docs/runbooks/model-drift.md`  
   - **System Outages**: `/docs/runbooks/system-outage.md`  
7. **Maintenance Handoffs**:  
   - Day-to-day ingestion monitoring by Data Engineering on-call.  
   - Model retraining and performance checks by ML Engineering weekly rotation.  
   - Infrastructure scaling and incident response by Platform Operations.  
8. **Documentation**: All pipelines, alert definitions, and dashboards documented in `/docs/deployment/carvana/` directory.