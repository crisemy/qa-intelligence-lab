let faultConfig = {
  enabled: true,
  errorProbability: 0.5,   // 0 to 1
  latencyMs: 3000
};

module.exports = {
  getConfig: () => faultConfig,
  updateConfig: (newConfig) => {
    faultConfig = { ...faultConfig, ...newConfig };
  }
};