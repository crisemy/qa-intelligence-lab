const { incrementRequests, addResponseTime } = require('../metrics/metrics.store');

const metricsMiddleware = (req, res, next) => {
  const start = Date.now();

  incrementRequests();

  res.on('finish', () => {
    const duration = Date.now() - start;
    addResponseTime(duration);
  });

  next();
};

module.exports = metricsMiddleware;