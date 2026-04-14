CREATE TABLE load_tests (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP,
    vus INT,
    duration_seconds INT,
    test_type VARCHAR(50)
);

CREATE TABLE fault_config (
    test_id UUID REFERENCES load_tests(id),
    error_probability FLOAT,
    latency_ms INT
);

CREATE TABLE metrics (
    test_id UUID REFERENCES load_tests(id),
    avg_response_time FLOAT,
    p95 FLOAT,
    error_rate FLOAT,
    throughput FLOAT
);