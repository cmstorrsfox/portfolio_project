const express = require('express');
const morgan = require('morgan');
const bodyParser = require('body-parser');
const errorhandler = require('errorhandler');
const cors = require('cors');
const formRouter = require('./routes/submit');
const { client } = require('./db/queries');


const app = express();
const PORT = process.env.PORT || 3001;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : false }));
app.use(morgan('dev'));
app.use(cors());
app.use(errorhandler());

app.set('views', './views')
app.set('view engine', 'pug');
app.use(express.static('public'));
app.use('/submit', formRouter);


app.get('/', (req, res, next) => {
  client.query(`SELECT * FROM submissions`, (err, submissions) => {
    if(err) {
      next(err);
    } else {
      res.status(200).render('home', { submissions: submissions.rows })
    }
  })
})


app.listen(PORT, () => {
  console.log(`The app is listening on ${PORT}`);
})