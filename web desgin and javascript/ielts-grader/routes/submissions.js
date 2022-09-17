const express = require('express');
const submissionsRouter = express.Router();
const { client } = require('../db/queries');
const methodOverride = require('method-override');

submissionsRouter.use(methodOverride('_method'));

submissionsRouter.param('id', (req, res, next, id) => {
  client.query(`SELECT * FROM submissions WHERE id = ${id}`, (err, user) => {
    if(err) {
      next(err);
    } else if (user) {
      req.user = user;
      next();
    } else {
      res.sendStatus(404);
    }
  })
});

const submissionValidator = (req, res, next, err) => {
  const firstName = req.body.firstName;
  const lastName = req.body.lastName;
  const email = req.body.email;
  const taskType = req.body.taskType;

  if(!firstName || !lastName || !taskType || !email) {
    res.sendStatus(400);
    console.log(err)
  } else {
    next();
  }
};

submissionsRouter.post('/', submissionValidator, (req, res, next) => {
  const firstName = req.body.firstName;
  const lastName = req.body.lastName;
  const email = req.body.email;
  const writingTaskOne = req.body.writingTaskOne;
  const writingTaskTwo = req.body.writingTaskTwo;
  const taskType = req.body.taskType;
  const emailed = req.body.emailed || 0;
  const datetime = req.body.datetime;
  
  client.query(`INSERT INTO submissions (type, first_name, last_name, email, writing_task_1, writing_task_2, emailed, datetime)
          VALUES 
          ('${taskType}', 
            '${firstName}', 
            '${lastName}', 
            '${email}', 
            '${writingTaskOne}', 
            '${writingTaskTwo}',
            '${emailed}',
            '${datetime}'
          )`,
          function(err) {
            if(err) {
              next(err);
            } else {
              client.query(`SELECT * FROM submissions WHERE id = LASTVAL()`, (err, submission) => {
                if(err) {
                  next(err);
                } else {
                  res.status(201).render('pages/submission-info', { submission : submission.rows })
                }
              })
            }
          });
});

submissionsRouter.put('/:id', submissionValidator, (req, res, next) => {
  const firstName = req.body.firstName;
  const lastName = req.body.lastName;
  const email = req.body.email;
  const writingTaskOne = req.body.writingTaskOne;
  const writingTaskTwo = req.body.writingTaskTwo;
  const taskType = req.body.taskType;
  const emailed = req.body.emailed;
  const datetime = req.body.datetime;
  
  client.query(`UPDATE submissions
          SET first_name = '${firstName}', last_name = '${lastName}', email = '${email}', writing_task_1 = '${writingTaskOne}', writing_task_2 = '${writingTaskTwo}', type = '${taskType}', emailed = '${emailed}', datetime = '${datetime}'
          WHERE id = ${req.params.id}`, (err) => {
            if(err) {
              next(err);
            } else {
                res.redirect(303, '/admin')
            }
          });
});


module.exports = submissionsRouter;