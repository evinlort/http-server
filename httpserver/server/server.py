import http.server
import re
import socketserver
from socketserver import ThreadingMixIn
from typing import Any
from urllib.parse import parse_qs, urlsplit

# from config import config
from httpserver import Server
from logger import log
from routing.router import Router


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
        print("GETTING")
        log.info(self.path)
        path, resp = self.get_path_query()
        router = Router("get", path, query=resp)
        response = router.execute()
        self.send_response(200)
        if ".css" in resp:
            self.send_header("Content-type", "text/css")
        elif ".js" in resp:
            self.send_header("Content-type", "text/javascript")
        else:
            self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.btext(response))

    def get_path_query(self):
        regex = r"(\/[a-z]{1,})(\/\w*.[a-z]{2,4})"
        matches = re.findall(regex, self.path, re.MULTILINE)
        if len(matches) == 1 and len(matches[0]) == 2:
            return self.get_clean_path(matches[0][0]), matches[0][1]
        return self.get_clean_path(self.path), self.get_query(self.path)

    def do_POST(self):
        print("POSTING")
        log.info(self.headers)
        body = self.get_post_body()
        log.info(body)
        path = self.get_clean_path(self.path)
        router = Router("post", path, query=body)
        response = router.execute()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.btext(response))

    def get_post_body(self) -> Any:
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        log.info(type(post_body))
        content_type = self.headers.get('content-type')
        if content_type == "application/json":
            import json
            return json.loads(post_body.decode("utf-8"))
        return post_body

    @staticmethod
    def btext(text):
        return text.encode()

    @staticmethod
    def get_query(path):
        return parse_qs(urlsplit(path).query)

    @staticmethod
    def get_clean_path(path):
        return urlsplit(path).path


class ThreadingServer(ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, config: Server):
        self.config = config
        super().__init__(("", config.get_port()), RequestsHandler)

    allow_reuse_address = True


with ThreadingServer as httpd:
    log.info("Start server")
    try:
        print(f"Server is running on {httpd.config.get_port()}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close()
    log.info("CTRL+C pressed. Closing socket")
    log.info("******************************")
    httpd.shutdown()
    httpd.server_close()
