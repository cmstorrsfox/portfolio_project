const express = require('express');
const faqRouter = express.Router();


faqRouter.get('/', (req, res, next) => {
  res.render('pages/faqs');
});

module.exports = faqRouter;