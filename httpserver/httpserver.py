import os

from .exceptions import *
from .logger import log


class HttpServer:
    def __init__(self, *, port: int = 8080, routing: str = "routing/web.py", controllers: str = "controllers",
                 css: str = "css", js: str = "js",
                 html: str = "html", log: str = "httpserver.log"):
        self._port = int(port)
        self.__check_routing(routing)
        self._controllers = controllers
        self.__check_folder_exists(controllers)
        self._css = css
        self._js = js
        self.__html = html
        self._log = log

    def set_port(self, port: int):
        self._port = int(port)

    def get_port(self) -> int:
        return self._port

    def set_router(self, route: str):
        self.__check_routing(route)

    def get_route(self) -> str:
        return self._routing

    def set_controllers(self, folder_path: str):
        self.__check_folder_exists(folder_path)
        self._controllers = folder_path

    def get_controllers(self) -> str:
        return self._controllers

    def __check_routing(self, route: str):
        if route[-3:] != ".py":
            route = f"{route}.py"
        if not os.path.exists(route):
            raise RouterFileNotFoundException
        self._routing = route

    @staticmethod
    def __check_folder_exists(route):
        if not os.path.exists(route):
            log.debug(f"Folder {route} not exists, will create it")
            os.makedirs(route)
