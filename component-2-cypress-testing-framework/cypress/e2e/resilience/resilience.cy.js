const FaultConfigBuilder = require("../../../testingFramework/config/faultConfigBuilder");
const HealthService = require("../../../testingFramework/domain/services/HealthService");
const FaultService = require("../../../testingFramework/domain/services/FaultService");

describe("Health Resilience", () => {

  beforeEach(() => {
    // Garantiza estado limpio antes de cada test
    return FaultService.disable();
  });

  afterEach(() => {
    // Protección extra por si un test falla
    return FaultService.disable();
  });

  it("should remain UP when fault disabled", () => {
    // Redundante pero explícito (mejor práctica E2E)
    return FaultService.disable().then(() => {
      return HealthService.check().then((response) => {
        expect(response.body.status).to.equal("UP");
      });
    });
  });

  it("should simulate deterministic failure", () => {

    const faultConfig = new FaultConfigBuilder()
      .withEnabled(true)
      .withErrorProbability(1)   // 100% error
      .withLatency(3000)
      .build();

    return FaultService.enable(faultConfig).then(() => {
      return HealthService.check().then((response) => {
        expect(response.body.status).to.equal("ERROR");
      });
    });
  });

});