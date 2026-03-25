const ApiClient = require("../http/ApiClient")

class HealthApi {

  static check() {
    return ApiClient.request({
      method: "GET",
      url: "/health"
    })
  }

}

module.exports = HealthApi