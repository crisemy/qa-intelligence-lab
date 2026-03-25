const db = require('./database');

// Seed users
const insertUser = db.prepare(`
  INSERT OR IGNORE INTO users (username, email, password)
  VALUES (?, ?, ?)
`);

insertUser.run('admin', 'admin@test.com', 'password');
insertUser.run('user1', 'user1@test.com', 'password');
insertUser.run('user2', 'user2@test.com', 'password');

// Seed issues
const insertIssue = db.prepare(`
  INSERT INTO issues (title, description, status, owner_id)
  VALUES (?, ?, ?, ?)
`);

insertIssue.run('Login bug', 'Cannot login with valid credentials', 'OPEN', 1);
insertIssue.run('Search not returning results', 'Search endpoint inconsistent', 'IN_PROGRESS', 2);
insertIssue.run('Report latency', 'Reporting endpoint slow response', 'OPEN', 1);

// Seed test catalog (VERY IMPORTANT for ML alignment)
const insertTest = db.prepare(`
  INSERT OR IGNORE INTO test_catalog (test_id, module, estimated_duration)
  VALUES (?, ?, ?)
`);

insertTest.run('T_AUTH_LOGIN_VALID', 'AUTH', 300);
insertTest.run('T_AUTH_LOGIN_INVALID', 'AUTH', 250);
insertTest.run('T_USERS_CREATE', 'USERS', 400);
insertTest.run('T_ISSUES_CREATE', 'ISSUES', 500);
insertTest.run('T_SEARCH_FILTER_STATUS', 'SEARCH', 450);
insertTest.run('T_REPORT_SUMMARY', 'REPORTING', 350);

console.log("Database seeded successfully.");