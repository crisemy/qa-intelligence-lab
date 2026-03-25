let metrics = {
  totalRequests: 0,
  totalErrors: 0,
  totalResponseTime: 0
};

module.exports = {
  incrementRequests: () => metrics.totalRequests++,
  incrementErrors: () => metrics.totalErrors++,
  addResponseTime: (time) => metrics.totalResponseTime += time,
  getMetrics: () => metrics
};