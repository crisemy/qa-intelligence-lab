-- =========================
-- Functional Domain
-- =========================

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS issues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT CHECK(status IN ('OPEN','IN_PROGRESS','CLOSED')) DEFAULT 'OPEN',
    owner_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS issue_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_id INTEGER,
    old_status TEXT,
    new_status TEXT,
    changed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(issue_id) REFERENCES issues(id)
);

-- =========================
-- Experimental Domain
-- =========================

CREATE TABLE IF NOT EXISTS synthetic_commits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commit_id TEXT NOT NULL UNIQUE,
    risk_profile TEXT NOT NULL,
    files_changed TEXT,
    lines_added INTEGER,
    lines_deleted INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS test_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id TEXT NOT NULL UNIQUE,
    module TEXT NOT NULL,
    estimated_duration INTEGER
);

CREATE TABLE IF NOT EXISTS test_executions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commit_id TEXT NOT NULL,
    test_id TEXT NOT NULL,
    duration_ms INTEGER,
    result TEXT CHECK(result IN ('PASS','FAIL')),
    executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(commit_id) REFERENCES synthetic_commits(commit_id),
    FOREIGN KEY(test_id) REFERENCES test_catalog(test_id)
);

CREATE TABLE IF NOT EXISTS build_summary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commit_id TEXT NOT NULL,
    total_tests INTEGER,
    failed_tests INTEGER,
    total_duration_ms INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(commit_id) REFERENCES synthetic_commits(commit_id)
);