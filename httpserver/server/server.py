import http.server
import socketserver
from socketserver import ThreadingMixIn
from typing import Any
from urllib.parse import parse_qs, urlsplit

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
        Get(self, Any.storage)

    def do_POST(self):
        Post(self, Any.storage)

    @staticmethod
    def btext(text):
        return text.encode()

    @staticmethod
    def get_query(path):
        temp = parse_qs(urlsplit(path).query)
        print(temp)
        build = dict()
        for k, v in temp.items():
            if len(v) == 1:
                build[k] = v[0]
            else:
                build[k] = v
        return build

    @staticmethod
    def get_clean_path(path):
        return urlsplit(path).path


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
