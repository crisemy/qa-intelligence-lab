// Define different experiment configurations with varying error probabilities and latencies to simulate different failure scenarios in the experiment engine.

function generateExperiments() {

  const experiments = [];

  const probabilities = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9];
  const latencies = [0,100,200,300,400,500,600,700,800,900,1000];

  for (const p of probabilities) {
    for (const l of latencies) {

      experiments.push({
        name: `p${p}_l${l}`,
        errorProbability: p,
        latencyMs: l
      });

    }
  }

  return experiments;
}

module.exports = generateExperiments();