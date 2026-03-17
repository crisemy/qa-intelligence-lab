const express = require('express');
const router = express.Router();
const { getMetrics } = require('../metrics/metrics.store');

router.get('/', (req, res) => {
  const metrics = getMetrics();

  const averageResponseTime =
    metrics.totalRequests === 0
      ? 0
      : metrics.totalResponseTime / metrics.totalRequests;

  const errorRate =
    metrics.totalRequests === 0
      ? 0
      : (metrics.totalErrors / metrics.totalRequests) * 100;

  res.json({
    totalRequests: metrics.totalRequests,
    totalErrors: metrics.totalErrors,
    errorRate: errorRate.toFixed(2) + '%',
    averageResponseTime: averageResponseTime.toFixed(2) + ' ms'
  });
});

module.exports = router;