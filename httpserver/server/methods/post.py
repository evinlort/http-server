import re

from httpserver.logger import log
from httpserver.routing.router import Router


class Post:
    def __init__(self, request_handler, config):
        self.rh = request_handler
        self.conf = config
        self.doing_post()

    def doing_post(self):
        try:
            print("POSTING")
            log.info(self.rh.headers)
            body = get_post_body(self.rh)
            log.info(body)
            path = self.rh.get_clean_path(self.rh.path)
            router = Router(
                "post",
                path,
                query=body,
                web=self.conf.get_router(),
                controllers=self.conf.get_controllers()
            )
            response = router.execute()
            self.rh.send_response(200)
            self.rh.send_header("Content-type", "text/html")
            self.rh.end_headers()
            self.rh.wfile.write(self.rh.btext(response))
        except Exception as e:
            log.exception(str(e))


def get_post_body(self):
    content_len = int(self.headers.get('content-length', 0))
    post_body = self.rfile.read(content_len)
    log.info(post_body)
    content_type = self.headers.get('content-type')
    if content_type == "application/json":
        import json
        return json.loads(post_body.decode("utf-8"))
    if content_type == "application/x-www-form-urlencoded":
        query_list = re.split("[=&]", post_body.decode("utf-8"))
        return {query_list[i]: query_list[i + 1] for i in range(0, len(query_list), 2)}
    if "multipart/form-data" in content_type:
        boundary = bytes("--" + re.findall("(-+[0-9]+)", content_type)[0], "ascii")

        def boundary_filtrate(s):
            if s == boundary:
                return False
            return True

        query_list = filter(boundary_filtrate, post_body.split(b'\r\n'))
        multipart = dict()
        for q in query_list:
            try:
                self.__fetch_decodable_post_data(q, multipart)
            except Exception as e:
                multipart["binary"] = q
        return multipart
    return post_body


def __fetch_decodable_post_data(data, d):
    line = re.findall("Content-Disposition: form-data; name=\"(.*)\"(?!;)", data.decode())
    if line:
        d[line[0]] = line
        return True
    return False
