var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end("<h1 style='color:blue'>Hello There! From nodejs!</h1>");
}).listen(8080, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8080/');
