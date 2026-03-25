const frameworkConfig = {
  api: {
    baseUrl: Cypress.config("baseUrl"),
    defaultTimeout: 10000,
  },
  resilience: {
    defaultRetries: 5,
  }
}

module.exports = frameworkConfig