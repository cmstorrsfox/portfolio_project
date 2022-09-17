const express = require('express');
const aboutUsRouter = express.Router();

aboutUsRouter.get('/', (req, res, next) => {
  res.render('pages/about-us');
})

module.exports = aboutUsRouter;