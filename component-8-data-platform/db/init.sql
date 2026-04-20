-- ================================
-- QA Intelligence Lab - Data Platform Schema
-- ================================

-- 1. Load tests metadata
CREATE TABLE IF NOT EXISTS load_tests (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    test_type VARCHAR(50) NOT NULL
);

-- 2. Aggregated metrics (ML-ready)
CREATE TABLE IF NOT EXISTS metrics (
    test_id UUID REFERENCES load_tests(id),
    avg_response_time FLOAT,
    p95 FLOAT,
    error_rate FLOAT,
    throughput FLOAT,
    total_requests INT,
    total_errors INT
);

-- 3. Fault configuration (context for ML)
CREATE TABLE IF NOT EXISTS fault_config (
    test_id UUID REFERENCES load_tests(id),
    error_probability FLOAT,
    latency_ms INT
);

-- 4. Optional RAW data (future ML / time series)
CREATE TABLE IF NOT EXISTS raw_k6_events (
    id SERIAL PRIMARY KEY,
    test_id UUID,
    timestamp TIMESTAMP,
    metric VARCHAR(50),
    value FLOAT,
    status INT
);