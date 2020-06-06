import http.server
import socketserver
from socketserver import ThreadingMixIn
from typing import Any

from httpserver.logger import log
from .methods.get import Get
from .methods.post import Post


# noinspection PyPep8Naming
class RequestsHandler(http.server.BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_HEAD(self):
        print("Doing HEAD")
        print(self.path)
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        response = Get(self.path, Any.storage).doing_get()
        self.__send_response(response)

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        post_data = {
            "headers": self.headers,
            "post_body": self.rfile.read(content_len),
            "path": self.path
        }
        response = Post(post_data, Any.storage).doing_post()
        self.__send_response(response)

    def __send_response(self, response):
        self.send_response(response["code"])
        for name, value in response["headers"].items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(response["message"])


class ThreadingServer(ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, config):
        Any.storage = config
        self.config = config
        super().__init__(("", config.get_port()), RequestsHandler)

    def __enter__(self):
        return self

    allow_reuse_address = True


def run(threading_server):
    with threading_server as httpd:
        log.info("Start server")
        try:
            log.info(f"Server is running on {httpd.config.get_port()}")
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()
            httpd.server_close()
        log.info("CTRL+C pressed. Closing socket")
        log.info("******************************")
        httpd.shutdown()
        httpd.server_close()
