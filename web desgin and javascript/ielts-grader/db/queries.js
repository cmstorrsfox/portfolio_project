const { Client } = require('pg');
const PORT = process.env.PORT || 5001;

if(PORT !== 5001) {
  const client = new Client({
    host: process.env.RDS_HOSTNAME,
    user: process.env.RDS_USERNAME,
    password: process.env.RDS_PASSWORD,
    port: process.env.RDS_PORT

  })

  client.connect();

  module.exports = { client }

} else {
  // for localhost
  const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'postgres',
    password: 'Shadow0801',
    port: 5432,
  });
  
  client.connect();

  module.exports = { client };
}


