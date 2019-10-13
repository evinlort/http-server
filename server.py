import http.server
import socketserver
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs, urlsplit

from logger import log
from router import Router

PORT = 8080


class CustomHandler(http.server.BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_HEAD(self):
        print("Doing HEAD")
        print(self.path)
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        print("GETTING")
        print(self.path)
        path = self.get_clean_path(self.path)
        resp = self.get_query(self.path)
        router = Router("get", path, query=resp)
        response = router.execute()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.btext(response))

    def do_POST(self):
        print("POSTING")
        log.info(self.headers)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        log.info(post_body)
        path = self.get_clean_path(self.path)
        router = Router("post", path, query=None)
        response = router.execute()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.btext(response))

    @staticmethod
    def btext(text):
        return text.encode()

    @staticmethod
    def get_query(path):
        return parse_qs(urlsplit(path).query)

    @staticmethod
    def get_clean_path(path):
        return urlsplit(path).path


class ThreadingSimpleServer(ThreadingMixIn, socketserver.TCPServer):
    pass


with ThreadingSimpleServer(("", PORT), CustomHandler) as httpd:
    log.info("Start server")
    try:
        print(f"Server is running on {PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    log.info("CTRL+C pressed. Closing socket")
    log.info("******************************")
    httpd.server_close()
