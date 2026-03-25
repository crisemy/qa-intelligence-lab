const { getConfig, updateConfig } = require('../config/fault.config');

exports.getFaultConfig = (req, res) => {
  res.json(getConfig());
};

exports.updateFaultConfig = (req, res) => {
  updateConfig(req.body);
  res.json(getConfig());
};

exports.disable = (req, res) => {
  updateConfig({
    enabled: false,
    errorProbability: 0,
    latencyMs: 0
});

res.status(200).json({ message: 'Fault disabled' });
};