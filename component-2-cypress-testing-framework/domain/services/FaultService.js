const FaultApi = require("../../infrastructure/api/FaultApi")

class FaultService {

  static enable(config) {
    return FaultApi.enable(config)
  }

  static disable() {
    return FaultApi.disable()
  }

}

module.exports = FaultService