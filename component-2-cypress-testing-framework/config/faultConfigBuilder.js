class FaultConfigBuilder {
  constructor() {
    this.config = {
      enabled: true,
      errorProbability: 0.5,
      latencyMs: 3000
    };
  }

  withEnabled(value) {
    this.config.enabled = value;
    return this;
  }

  withErrorProbability(value) {
    this.config.errorProbability = value;
    return this;
  }

  withLatency(ms) {
    this.config.latencyMs = ms;
    return this;
  }

  build() {
    return { ...this.config };
  }
}

module.exports = FaultConfigBuilder;