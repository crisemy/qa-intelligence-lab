const HealthApi = require("../../infrastructure/api/HealthApi")

class HealthService {

  static check() {
    return HealthApi.check()
  }

}

module.exports = HealthService