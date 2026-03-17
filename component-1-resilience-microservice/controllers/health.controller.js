const db = require('../db/database');

exports.getHealth = (req, res) => {
  try {
    // simple DB check
    const row = db.prepare('SELECT 1 as ok').get();

    res.status(200).json({
      status: 'UP',
      database: row ? 'CONNECTED' : 'DISCONNECTED',
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    res.status(500).json({
      status: 'DOWN',
      error: error.message
    });
  }
};