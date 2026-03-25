const ApiClient = require("../http/ApiClient");

class FaultApi {

  static enable(config) {
    return ApiClient.request({
      method: "POST",
      url: "/fault",
      body: config
    });
  }

  static disable() {
    return ApiClient.request({
      method: "DELETE",
      url: "/fault"
    });
  }

}

module.exports = FaultApi;