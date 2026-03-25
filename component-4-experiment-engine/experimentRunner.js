// This file defines the configuration for different experiment scenarios, including their names, error probabilities, and latency in milliseconds. Each scenario represents a different level of failure that can be simulated in the experiment engine.

const axios = require("axios");
const fs = require("fs");
const generateExperiments = require("./experimentGenerator");

const BASE_URL = "http://localhost:3000";

const EXPERIMENT_COUNT = 1000; // There's a parallel pool of 10, so this will run 100 batches of 10 experiments each, which should be manageable in terms of time and resource usage 
                               // while still providing a comprehensive dataset for training the model.
const PARALLEL_POOL = 10;

async function runExperiment(exp) {

  await axios.post(`${BASE_URL}/fault`, {
    enabled: true,
    errorProbability: exp.errorProbability,
    latencyMs: exp.latencyMs
  });

  let errors = 0;

  for (let i = 0; i < 50; i++) {
    try {
      await axios.get(`${BASE_URL}/health`);
    } catch {
      errors++;
    }
  }

  const metrics = await axios.get(`${BASE_URL}/metrics`);

  return {
    experiment: exp.name,
    errorProbability: exp.errorProbability,
    latencyMs: exp.latencyMs,
    totalRequests: metrics.data.totalRequests,
    errors,
    errorRate: errors / 50,
    avgResponseTime: metrics.data.avgResponseTime
  };
}

async function runAll() {

  const experiments = generateExperiments(EXPERIMENT_COUNT);

  const results = [];

  for (let i = 0; i < experiments.length; i += PARALLEL_POOL) {

    const batch = experiments.slice(i, i + PARALLEL_POOL);

    console.log(`Running batch ${i} - ${i + batch.length}`);

    const batchResults = await Promise.all(
      batch.map(exp => runExperiment(exp))
    );

    results.push(...batchResults);

  }

  fs.writeFileSync(
    "./dataset/experiments.json",
    JSON.stringify(results, null, 2)
  );

  console.log("Dataset generated:", results.length);
}

runAll();