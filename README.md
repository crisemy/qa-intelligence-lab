# QA Intelligence Lab

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38%2B-FF4B4B)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A resilience testing and experimentation platform that combines:

* QA automation
* Chaos engineering
* Experiment-driven testing
* Data analysis
* Interactive dashboards
* Performance & Load Testing

## Overview

QA Intelligence Lab is an experimental resilience testing microservice designed to simulate controlled failures and latency conditions in automated testing environments.

The system acts as a **System Under Test (SUT)** for resilience validation using automated testing frameworks and CI/CD pipelines and performance testing tools, focusing on experimental QA engineering, reliability analysis, and future data-driven system stability modeling.

---

# Project Structure

The project is composed of three experimental components:

1. **Resilience Testing Microservice (Backend System)**
2. **Cypress Resilience Testing Framework**
3. **CI Pipeline Integration with Jenkins**
4. **Experiment Engine**
5. **Data Analysis**
6. **Streamlit Dashboard**
7. **Performance Testing with k6**
8. **Component 9: ML Layer**
9. **Component 8: Data Platform**

Together, these components simulate a complete **experimental QA + SRE + Data platform**.

---

# How to Run the System

The system is **hybrid**:
```bash
| Component | Runs |
|----------|------|
| Microservice | Local (Node.js) |
| k6 | Docker |
| Jenkins | Docker |
```
## Step 1: Start the Microservice
```bash
cd component-1-resilience-microservice
npm install
node server.js
```

Expected Output:
```bash
QA Intelligence Lab running on port 3000
```

Test:
```bash
curl http://localhost:3000/health
```

## Step 2: Run Performance Tests (k6)
```bash
docker-compose run k6 run scripts/baseline.js
OR
docker-compose run k6 run scripts/load.js
```

Important Networking Detail. k6 runs inside Docker, so it must call:
```bash
http://host.docker.internal:3000
```

# Objectives

* Simulate probabilistic system failures
* Inject artificial latency
* Measure operational impact
* Generate structured data for resilience experimentation
* Validate automated resilience tests in a CI environment
* Evaluate system performance under load
* Generate datasets for predictive modeling

---

# Architecture

Technologies used:

* Node.js
* Express.js
* SQLite
* Cypress
* Jenkins
* Docker
* k6
* Streamlit

Architecture principles:

* Modular middleware-based design
* Centralized error handling
* In-memory observability layer
* Runtime-configurable fault injection
* CI-driven automated testing
* Load-driven experimentation

---

# Component 1 — Resilience Testing Microservice

The backend service simulates unstable system behavior in a controlled and configurable way.

It exposes endpoints that allow runtime modification of system fault conditions.

## Health Endpoint
```bash
curl http://localhost:3000/health
{"status":"UP","database":"CONNECTED","timestamp":"2026-04-20T18:24:00.474Z"}

GET /health # Returns the system status and database connectivity information.
```

---

## Fault Injection

GET /fault
POST /fault

This endpoint allows runtime configuration of failure parameters.

Example configuration:

```bash
{
  "enabled": true,
  "errorProbability": 0.5,
  "latencyMs": 3000
}
```

This configuration simulates:

* 50% probabilistic service failures
* 3 seconds of artificial latency

These parameters allow controlled resilience experiments.

---

## Metrics Endpoint

GET /metrics

This endpoint exposes runtime metrics:

* Total requests
* Total errors
* Error rate (%)
* Average response time

These metrics enable basic observability for resilience experimentation.

---

# Component 2 — Cypress Resilience Testing Framework

A Cypress-based testing framework was developed to validate the system under different operational conditions.

The framework executes automated tests against the backend microservice.

Example test scenarios include:

* System remains operational when faults are disabled
* Deterministic failure simulation when fault injection is enabled
* Verification of API behavior under unstable conditions

This framework acts as the **experimental validation layer** of the system.

---

# Component 3 — CI Integration with Jenkins

The testing framework is integrated with **Jenkins running inside Docker**, enabling automated execution of resilience tests in a CI environment.

Jenkins executes Cypress using the official Docker image:

```bash
cypress/included:15.11.0
```

The backend service runs locally on the host machine, while Jenkins triggers the tests through a containerized Cypress environment.

To enable communication between containers and the host system, the pipeline uses:

```bash
http://host.docker.internal:3000
```

This setup simulates a simplified **CI/CD resilience testing pipeline**.

---

# Component 4 — Experiment Engine

Responsible for generating resilience experiments. The engine:

* Injects failure configurations
* Executes repeated health checks
* Collects runtime metrics
* Generates experiment datasets

Output:
```bash
experiments.json
```

---

# Component 5 — Data Analysis

A Jupyter Notebook environment used to analyze experiment results. Typical analysis includes:

* Error rate distribution
* Latency vs failure correlation
* Response time statistics

---

# Component 6 — Streamlit Dashboard

An interactive dashboard used to visualize the dataset generated by the experiment engine. Provides:

* Resilience metrics overview
* Interactive plots
* Experiment exploration

---

# Component 7 — Load Testing with k6

This component introduces load and stress testing capabilities.
Test Types: Baseline Test

File:
```bash
scripts/baseline.js
```

Characteristics:

* Fixed VUs
* Constant load
* Measures normal system behavior

Load Test: 
```bash
scripts/load.js
```

Characteristics:

* Ramp-up / peak / ramp-down
* Stress testing
* SLA validation via thresholds

Example Thresholds:
```bash
thresholds: {
  http_req_duration: ['p(95)<2000'],
  http_req_failed: ['rate<0.1'],
}   
```
If exceeded:
```bash
thresholds have been crossed
```
---

## Component 8 — Data Platform

The Data Platform component is responsible for managing and processing data generated during resilience and load testing. It includes:

### Features
- **Database Initialization**: Scripts to set up the database schema and seed data.
- **Data Ingestion**: Python scripts to parse and ingest k6 results into the database.
- **Data Analysis**: Tools to analyze and visualize test results.

### Key Files
- `db/init.sql`: Initializes the database schema.
- `db/schema.sql`: Defines the database structure.
- `ingestion/config.py`: Configuration for data ingestion.
- `ingestion/db_client.py`: Database client for interacting with the database.
- `ingestion/parse_k6_results.py`: Parses k6 results and inserts them into the database.

### Usage
1. Initialize the database:
   ```bash
   python ingestion/db_client.py --init
   ```
2. Parse and ingest k6 results:
   ```bash
   python ingestion/parse_k6_results.py --file results/load-test.json
   ```

This component ensures that all test data is stored and processed efficiently for further analysis.

---

## Component 9  — ML Layer

### Overview
The ML Layer introduces machine learning capabilities to the observability pipeline. It includes:
- Feature engineering from k6 metrics.
- Dataset aggregation over multiple runs.
- A baseline ML model for classification or regression.
- A failure prediction system.
- An automated training pipeline.

### New Scripts
- `feature_engineering.py`: Extracts features from k6 metrics.
- `dataset_aggregation.py`: Aggregates datasets from multiple load test runs.
- `baseline_model.py`: Trains a baseline ML model.
- `failure_prediction.py`: Predicts failures using the trained model.
- `training_pipeline.py`: Automates the ML training pipeline.
- `streamlit_app.py`: A Streamlit app to visualize classification reports.

### Installation
To set up the environment, install the required Python packages:
```bash
pip install pandas scikit-learn
```

### Usage
1. Run the training pipeline:
   ```bash
   python training_pipeline.py
   ```
2. Launch the Streamlit app to view results:
   ```bash
   streamlit run component-9-ML-layer/streamlit_app.py
   ```

---

## Intelligence Lab Architecture
```bash
QAIntelligenceLab
│
├─ component-1-resilience-microservice
├─ component-2-cypress-testing-framework
├─ component-3-ci-pipeline
├─ component-4-experiment-engine
├─ component-5-data-science-analysis
├─ component-6-dashboard
├─ component-7-load-testing
├─ component-8-data-platform
├─ component-9-ML-layer
```
---
## Data Flow

![Data Flow](./images/data_flow.png "Data Flow Diagram")

# Experimental Use Case

The system enables:

* Resilience testing
* Performance testing
* Fault injection experiments
* Dataset generation for ML

---

# Roadmap

Future extensions may include:

* Automated metrics persistence
* Large-scale resilience test execution
* Dataset generation for reliability modeling
* Machine learning experiments for anomaly detection
* Predictive modeling of system instability

# Author

Cristian N.

QA Engineer with 20+ years of experience in software testing and automation.

MSc Candidate in Data Science & Artificial Intelligence.

Research interests include:

* Experimental QA engineering
* QA Architecture
* Reliability testing
* AI-assisted quality assurance
* Data-driven software stability analysis