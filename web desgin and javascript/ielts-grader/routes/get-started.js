const express = require('express');
const getStartedRouter = express.Router();

getStartedRouter.get('/', (req, res, next) => {
  res.render('pages/get-started');
})

module.exports = getStartedRouter;