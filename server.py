import http.server
import socketserver
from router import Router
from urllib.parse import parse_qs, urlsplit

PORT = 8080

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_HEAD(self):
        print("Doing HEAD")
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        print("GETTING")
        print(self.path)
        path = self.get_clean_path(self.path)
        resp = self.get_query(self.path)
        print(resp)
        router = Router("get", path, query=resp)
        response = router.execute()
        print(response)
        # print(resp)
        #
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # if "test" in resp:
        #     if "ok" in resp["test"]:
        #         self.wfile.write(self.btext("<b>The best Code ever</b>"))
        #         return
        # self.wfile.write(self.btext("Hello, world!"))
        self.wfile.write(self.btext(response))

    def do_POST(self):
        print("POSTING")
        print(self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        import time

        self.wfile.write(self.btext(f"Time is: {time.time()}"))

    def btext(self, text):
        return text.encode()

    def get_query(self, path):
        return parse_qs(urlsplit(path).query)

    def get_clean_path(self, path):
        return urlsplit(path).path

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    try:
        print(f"Server is running on {PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("CTRL+C pressed. Closing socket")
    print(httpd.socket)
    httpd.server_close()
