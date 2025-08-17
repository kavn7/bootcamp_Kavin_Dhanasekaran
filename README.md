# Bootcamp Repository 
## Folder Structure
- **homework/** → All homework contributions will be submitted here. 
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to GitHub. 
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading. 
## Project Folder Rules
- Keep project files organized and clearly named. 
 # Optimizing Social Media Activity to predict Market Anomalies: A Case Study of Carvana, Inc. 
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement 
- Carvana, Inc. (CVNA) has seen a significant increase in its share price from its early years to now, drawing notable attention from major institutional investors and market participants. This growth in visibility has made Carvana a closely watched stock, with high daily trading volumes and volatile price swings. This project examines how routine social media activity, such as daily post volume and engagement metrics related to Carvana, affects its stock market behavior, particularly in detecting market irregularities like abnormal returns and volatility spikes. Understanding and quantitatively leveraging this connection is important because it can offer traders and analysts early warning signs of market-moving events. By utilizing optimization algorithms like Genetic Algorithms or Particle Swarm Optimization, the project aims to find the best combination of social media and stock market features that enhances the early detection of these anomalies.
## Stakeholder & User 
- The primary stakeholders include retail and institutional investors, financial analysts, and data scientists focused on US equities and alternative data sources, while the end users are quantitative analysts and portfolio managers who integrate predictive signals into trading and risk frameworks; the solution is applied within daily trading analysis to inform buy/sell decisions or volatility hedging, with a next-day prediction horizon guiding actionable insights.
## Useful Answer & Decision 
- This project develops an optimized machine learning model, enhanced by metaheuristic algorithms, to predict and classify days with potential stock anomalies for Carvana, using key social media and stock features as leading indicators; the model’s performance will be evaluated through precision and recall, and supported by visual analytic reports that highlight the most influential features driving anomaly detection.
## Assumptions & Constraint
-  Daily historical stock price and volume data for Carvana is available and reliable via Yahoo Finance.
-  Aggregated daily social media activity metrics (post counts, engagement) mentioning Carvana can be collected without using natural language processing.
-  Analysis will use daily frequency data; intraday data is out of scope.
-  Adherence to data use policies from social media platforms and financial data providers is ensured.
## Known Unknowns / Risks 
- The strength and consistency of the relationship between social media activity and Carvana’s stock anomalies may vary over time and market conditions.
- Potential contamination of social media data by irrelevant content may introduce noise; feature selection and data cleaning are necessary.
- Limited occurrence of extreme anomaly events could lead to model overfitting, requiring rigorous validation.
- Unmodeled external factors (macroeconomic news, industry trends) may affect anomaly occurrence and challenge prediction accuracy.
## Lifecycle Mapping 
- Goal: Establish a quantifiable link between Carvana’s daily social media activity and stock market anomalies to enable improved predictive insights.
- Deliverable: Detailed problem definition document outlining project scope, stakeholder roles, desired outputs, key assumptions, risk factors, and alignment of goals to project stages.

# Project Objective
- To Quantify the impact of routine daily social media activities related to Carvana, Inc. on its stock market behavior.
- To Collect and analyze historical stock price, volume data, and aggregated social media metrics without using NLP.
- To Identify patterns and signals in social media activity that correlate with market anomalies like abnormal returns and volatility spikes.
- To Use optimization algorithms (e.g., Genetic Algorithm, Particle Swarm Optimization) to select the most predictive combination of features and Develop a predictive model to detect market anomalies with improved accuracy.
- To Deliver a comprehensive report validating how everyday social media actions can have a considerable macroscopic effect on financial market movements.
