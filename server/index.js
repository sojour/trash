const express = require('express')
const path = require('path')
const morgan = require('morgan')
//Did not use
const runPy = require('./runPy')
const { PythonShell } = require('python-shell')


const app = express();

app.use(morgan('dev'));

app.use(express.json({ limit: '50mb', extended: true }))
app.use(express.urlencoded({ limit: '50mb', extended: true }))

app.use(express.static(path.join(__dirname, '../public')));


app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'))
})

app.post('/api/predict', async (req, res, next) => {
  const name = req.body.name;
  const data = req.body.data;

  let runPy = async (name, data) => {
    let options = {
      mode: 'text',
      pythonPath: '/usr/local/bin/python3',
      pythonOptions: ['-u'],
      scriptPath: '/Users/weiji/Documents/GHJ/W8/trash/py',
      args: [name, data]
    };
    let pyshell = new PythonShell('main.py', options)

    await pyshell.send(options); // path, args etc
    pyshell.on('message', await function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      res.send(message)
    });
    await pyshell.end(function (err, code, signal) {
      if (err) res.send('Something happened');
      console.log('finished');
    });
  }

  runPy(name, data)
})


app.use(function (err, req, res, next) {
  console.error(err);
  console.error(err.stack);
  res.status(err.status || 500).send(err.message || 'Internal server error.');
});


module.exports = app
