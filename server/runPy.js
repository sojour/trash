//Decided to move it to index.js as nodejs run things synchronously and wouldn't wait for pyscript results

const { PythonShell } = require('python-shell')
let runPy = async (name, data) => {
  console.log('Im in!')
  let options = {
    mode: 'text',
    pythonPath: '/usr/local/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '/Users/weiji/Documents/GHJ/W8/trash/py',
    args: [name, data]
  };
  let pyshell = new PythonShell('main.py', options)

  await pyshell.send(options); // path, args etc
  let info = []
  pyshell.on('message', await function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    info.push(message)
    return message
  });
  await pyshell.end(function (err, code, signal) {
    if (err) throw err;
    // console.log('finished');
    return info[info.length - 1];
  });
}

module.exports = runPy;
