function generateExperiments(count = 30) {

  const experiments = [];

  for (let i = 0; i < count; i++) {

    experiments.push({
      name: `exp_${i}`,
      errorProbability: Math.random() * 0.8,
      latencyMs: Math.floor(Math.random() * 800)
    });

  }

  return experiments;
}

module.exports = generateExperiments;