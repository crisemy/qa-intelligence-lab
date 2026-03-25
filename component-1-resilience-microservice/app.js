const express = require('express');
const healthRoutes = require('./routes/health.routes');
const loggerMiddleware = require('./middlewares/logger.middleware');
const errorMiddleware = require('./middlewares/error.middleware');
const faultMiddleware = require('./middlewares/fault.middleware');
const faultRoutes = require('./routes/fault.routes');
const metricsMiddleware = require('./middlewares/metrics.middleware');
const metricsRoutes = require('./routes/metrics.routes');

const app = express();

app.use(express.json());
app.use(loggerMiddleware);
app.use(metricsMiddleware);
app.use(faultMiddleware);

app.use('/health', healthRoutes);
app.use('/fault', faultRoutes);
app.use('/metrics', metricsRoutes);

// Global error handler
app.use(errorMiddleware);

module.exports = app;