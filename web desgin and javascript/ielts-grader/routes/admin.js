const express = require('express');
const adminRouter = express.Router();

const { client } = require('../db/queries');

//get all submissions
adminRouter.get('/', (req, res, next) => {
  client.query(`SELECT * FROM submissions ORDER BY emailed ASC`, (err, submissions) => {
    if(err) {
      next(err);
    } else {
      if(req.get('Referer')) { 
        res.render('pages/admin', { submissions : submissions.rows })
      } else {
        res.sendStatus(401);
      }
    }
  })
});

module.exports = adminRouter;