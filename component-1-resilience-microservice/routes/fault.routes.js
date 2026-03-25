const express = require('express');
const router = express.Router();
const faultController = require('../controllers/fault.controller');

router.post('/', faultController.updateFaultConfig);
router.delete('/', faultController.disable);
router.get('/', faultController.getFaultConfig);

module.exports = router;