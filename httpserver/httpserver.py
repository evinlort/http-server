import os

from .exceptions import *


class HttpServer:
    def __init__(self, *, port: int = 8080, routing: str = "routing/web", controllers: str = "controllers",
                 css: str = "css", js: str = "js", html: str = "html"):
        self._port = int(port)
        self._routing = routing
        self._controllers = controllers
        self._css = css
        self._js = js
        self.__html = html
        self.__check_routing()

    def set_port(self, port: int):
        self._port = int(port)

    def get_port(self):
        return self._port

    def __check_routing(self):
        if self._routing[-3:] != ".py":
            self._routing = f"{self._routing}.py"
        if not os.path.exists(self._routing):
            raise RouterFileNotFoundException
