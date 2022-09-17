const express = require('express');
const formRouter = express.Router();
const { client }  = require('../db/queries');

formRouter.get('/', (req, res, next) => {
  res.render('submit')
});

formRouter.post('/', (req, res, next) => {
  const title = req.body.title;
  const content = req.body.content;
  const name = req.body.name;
  const backgroundImg = req.body.background_img;
  const font = req.body.font;
  const red = req.body.red;
  const green = req.body.green;
  const blue = req.body.blue;

  client.query(`INSERT INTO submissions (title, content, name, background_img, font, red, green, blue)
  VALUES ('${title}', '${content}', '${name}', '${backgroundImg}', '${font}', '${red}', '${green}', '${blue}')`,
  function(err) {
    if(err) {
      next(err);
    } else {
      res.redirect('/')
    }
  })
})

module.exports = formRouter;