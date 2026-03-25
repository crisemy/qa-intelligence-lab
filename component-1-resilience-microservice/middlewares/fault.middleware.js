const { getConfig } = require('../config/fault.config');

const faultMiddleware = async (req, res, next) => {
  
  if (req.path.startsWith('/fault') || req.path.startsWith('/metrics')) {
    return next();
  }
  
const config = getConfig();
  
  if (!config.enabled) {
    return next();
  }

  // Latency injection
  if (config.latencyMs > 0) {
    await new Promise(resolve => setTimeout(resolve, config.latencyMs));
  }

  // Error injection
  if (Math.random() < config.errorProbability) {
    const error = new Error('Injected failure');
    error.status = 500;
    return next(error);
  }

  next();
};

module.exports = faultMiddleware;