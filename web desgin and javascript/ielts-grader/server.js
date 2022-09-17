const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const errorhandler = require('errorhandler');
const morgan = require('morgan');
const { client } = require('./db/queries');
const aboutUsRouter = require('./routes/about-us');
const getStartedRouter = require('./routes/get-started');
const submissionsRouter = require('./routes/submissions');
const authRouter = require('./routes/auth');
const adminRouter = require('./routes/admin');
const faqRouter = require('./routes/faqs');

const app = express();
const PORT = process.env.PORT || 5001;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : false }));
app.use(cors());
app.use(morgan('dev'));
app.use(errorhandler());

app.use(express.static(__dirname + '/public'))

//routers
app.use('/about-us', aboutUsRouter);
app.use('/get-started', getStartedRouter);
app.use('/submissions', submissionsRouter);
app.use('/auth', authRouter);
app.use('/admin', adminRouter);
app.use('/faqs', faqRouter);



app.set('view engine', 'pug');

app.get('/', (req, res, next) => {
  res.render('pages/landing-page', { loginButton: "Log in" });
});



app.listen(PORT, () => {
  console.log(`The server is listening on ${PORT}`);
});
