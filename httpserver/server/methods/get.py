import re
from urllib.parse import parse_qs, urlsplit

from httpserver.logger import log
from httpserver.routing.router import Router


class Get:
    def __init__(self, path, config):
        self.path = path
        self.conf = config

    def doing_get(self) -> dict:
        try:
            print("GETTING")
            log.info(self.path)
            path, query = self.__get_path_query()
            router = Router(
                "get",
                path,
                query=query,
                web=self.conf.get_router(),
                controllers=self.conf.get_controllers()
            )
            response = router.execute()
            log.info(response)
            headers = dict()
            if ".css" in query:
                headers["Content-type"] = "text/css"
            elif ".js" in query:
                headers["Content-type"] = "text/javascript"
            else:
                headers["Content-type"] = "text/html"
            return {
                "code": 200,
                "headers": headers,
                "message": response.encode()
            }
        except Exception as e:
            log.exception(str(e))
            return {
                "code": 500,
                "headers": {"Content-type": "application/json"},
                "message": str(e).encode()
            }

    def __get_path_query(self):
        regex = r"(\/[a-z]{1,})(\/\w*.[a-z]{2,4})"
        matches = re.findall(regex, self.path, re.MULTILINE)
        if len(matches) == 1 and len(matches[0]) == 2:
            return urlsplit(matches[0][0]).path, matches[0][1]
        return urlsplit(self.path).path, self.get_query(self.path)

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
