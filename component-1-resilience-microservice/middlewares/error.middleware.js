const { incrementErrors } = require('../metrics/metrics.store');

const errorMiddleware = (err, req, res, next) => {
    incrementErrors(); 
    
    console.error('Global Error Handler:', err);

    res.status(err.status || 500).json({
        status: 'ERROR',
        message: err.message || 'Internal Server Error'
    });
};

module.exports = errorMiddleware;