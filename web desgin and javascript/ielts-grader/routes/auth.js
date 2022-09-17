const express = require('express');
const authRouter = express.Router();
const bcrypt = require('bcrypt');
const safeCompare = require('safe-compare');

const { client } = require('../db/queries');

//userValidator
const userValidator = (req, res, next) => {
  const username = req.body.username;

  const userCheck = safeCompare(username, 'cmstorrsfox')

  if(!userCheck) {
    res.render('pages/auth', {authorised : false, errorMessage : 'incorrect username or password', loginButton: "Log in"});
  } else {
    next();
  }
};

//get users and show page
authRouter.get('/', (req, res, next) => {
  res.render('pages/auth', {authorised : false, errorMessage : '', loginButton: "Log in" })
});

//check credentials
authRouter.post('/', userValidator, (req, res, next) => {
  const plainTextPassword = req.body.plainTextPassword;

  client.query(`SELECT * from users`, (err, hash) => {
    if(err) {
      next(err)
    } else {
      bcrypt.compare(plainTextPassword, hash.rows[0].password, function(err, result) {
        if(result) {
          res.redirect('/admin') 
        } else if(err) {
          next(err)
        } else {
          res.render('pages/auth', {authorised : false, errorMessage : 'incorrect username or password', loginButton: "Log in"});
        }
      })
    }
  })
})


//create new user
authRouter.post('/:new-user', (req, res, next) => {
  const username = req.body.username;
  const plainTextPassword = req.body.plainTextPassword;
  const saltRounds = 10;

  bcrypt.genSalt(saltRounds, function(err, salt) {
    bcrypt.hash(plainTextPassword, salt, function(err, hash) {
      if(err) {
        console.log(err);
      } else {
        client.query(`INSERT INTO users(username, password)
        VALUES('${username}', '${hash}')`, function(err) {
          if(err) {
            next(err);
          } else {
            res.send('user added')
          }
        });
      }
    });
  });

});




module.exports = authRouter;