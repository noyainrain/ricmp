from http.server import HTTPServer, SimpleHTTPRequestHandler

class RequestHandler(SimpleHTTPRequestHandler):
    def send_response(self, code: int, message: str = None) -> None:
        super().send_response(code, message=message)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')

if __name__ == '__main__':
    with HTTPServer(('', 8080), RequestHandler) as server:
        server.serve_forever()
