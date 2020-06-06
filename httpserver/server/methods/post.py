import re
from urllib.parse import urlsplit

from httpserver.logger import log
from httpserver.routing.router import Router


class Post:
    def __init__(self, request_handler_post_data, config):
        self.headers = request_handler_post_data["headers"]
        self.post_body = request_handler_post_data["post_body"]
        self.path = request_handler_post_data["path"]
        self.conf = config

    def doing_post(self) -> dict:
        try:
            print("POSTING")
            log.info(self.headers)
            body = self.__get_post_body()
            log.info(body)
            path = urlsplit(self.path).path
            router = Router(
                "post",
                path,
                query=body,
                web=self.conf.get_router(),
                controllers=self.conf.get_controllers()
            )
            response = router.execute()
            return {
                "code": 200,
                "headers": {"Content-type": "text/html"},
                "message": response.encode()
            }
        except Exception as e:
            log.exception(str(e))
            return {
                "code": 500,
                "headers": {"Content-type": "application/json"},
                "message": str(e).encode()
            }

    def __get_post_body(self):
        log.info(self.post_body)
        content_type = self.headers.get('content-type')
        if not content_type:
            return self.post_body.decode()
        if content_type == "application/json":
            # TODO: to func
            import json
            return json.loads(self.post_body.decode("utf-8"))
        if content_type == "application/x-www-form-urlencoded":
            # TODO: to func
            query_list = re.split("[=&]", self.post_body.decode("utf-8"))
            return {query_list[i]: query_list[i + 1] for i in range(0, len(query_list), 2)}
        if "multipart/form-data" in content_type:
            # TODO: to func
            boundary = bytes("--" + re.findall("(-+[0-9]+)", content_type)[0], "ascii")

            def boundary_filtrate(s):
                if s == boundary:
                    return False
                return True

            query_list = filter(boundary_filtrate, self.post_body.split(b'\r\n'))
            multipart = dict()
            for q in query_list:
                try:
                    self.__fetch_decodable_post_data(q, multipart)
                except Exception as e:
                    multipart["binary"] = q
            return multipart

    @staticmethod
    def __fetch_decodable_post_data(data, d):
        line = re.findall("Content-Disposition: form-data; name=\"(.*)\"(?!;)", data.decode())
        if line:
            d[line[0]] = line
            return True
        return False
