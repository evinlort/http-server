import re

from httpserver.logger import log
from httpserver.routing.router import Router


class Get:
    def __init__(self, request_handler, config):
        self.rh = request_handler
        self.conf = config
        self.doing_get()

    def doing_get(self):
        try:
            print("GETTING")
            log.info(self.rh.path)
            path, query = get_path_query(self.rh)
            router = Router(
                "get",
                path,
                query=query,
                web=self.conf.get_router(),
                controllers=self.conf.get_controllers()
            )
            response = router.execute()
            log.info(response)
            self.rh.send_response(200)
            if ".css" in query:
                self.rh.send_header("Content-type", "text/css")
            elif ".js" in query:
                self.rh.send_header("Content-type", "text/javascript")
            else:
                self.rh.send_header("Content-type", "text/html")
            self.rh.end_headers()
            self.rh.wfile.write(self.rh.btext(response))
        except Exception as e:
            log.exception(str(e))


def get_path_query(request_handler):
    regex = r"(\/[a-z]{1,})(\/\w*.[a-z]{2,4})"
    matches = re.findall(regex, request_handler.path, re.MULTILINE)
    if len(matches) == 1 and len(matches[0]) == 2:
        return request_handler.get_clean_path(matches[0][0]), matches[0][1]
    return request_handler.get_clean_path(request_handler.path), request_handler.get_query(request_handler.path)
