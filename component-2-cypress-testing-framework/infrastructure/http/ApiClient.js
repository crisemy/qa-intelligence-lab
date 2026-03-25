const frameworkConfig = require("../../config/frameworkConfig")

class ApiClient {

  static request({ method, url, body, failOnStatusCode = false }) {
    return cy.request({
      method,
      url: `${frameworkConfig.api.baseUrl}${url}`,
      body,
      failOnStatusCode,
      timeout: frameworkConfig.api.defaultTimeout
    })
  }

}

module.exports = ApiClient