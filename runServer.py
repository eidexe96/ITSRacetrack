import time
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '192.168.0.193'
PORT_NUMBER = 8081

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.respond({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = ""
        htmlFile = open("test.html")
        for line in htmlFile:
            html += line.rstrip()
        htmlFile.close()
        content = html
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    #print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))

    try:
        httpd.serve_forever()
        time.sleep(10)
        httpd.server_close()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    #print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
