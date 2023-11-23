# your_server_script.py

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, this is your HTTP server!')

if __name__ == "__main__":
    PORT = 8000

    # Start the HTTP server
    with TCPServer(('127.0.0.1', PORT), MyHandler) as httpd:
        print(f'Serving on port {PORT}')
        httpd.serve_forever()
