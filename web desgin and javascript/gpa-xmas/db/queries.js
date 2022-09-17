const { Client } = require('pg');


const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

client.connect();

/*
const client = new Client({
  host: 'localhost',
  post: 5432,
  user: 'postgres',
  password: 'Shadow0801',
  database: 'gpa_xmas'
})

client.connect();
*/

module.exports = { client }