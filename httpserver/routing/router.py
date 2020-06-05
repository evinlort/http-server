from importlib import import_module
from typing import Any

from httpserver.logger import log
from httpserver.routing.route_tuple import *


class Router:
    def __init__(self, command, route, query=None, *, web, controllers):
        self.web = import_module(".".join(web[:-3].split("/")))
        self.controllers = controllers
        self.query = query
        self.executor = self.get_executor(command, route)

    def execute(self):
        try:
            controller, method = self.executor.split(":")
        except AttributeError:
            return "Route not defined"
        controller_method = self.execute_controller_method(controller, method)
        return controller_method(self.query)

    def execute_controller_method(self, controller: str, method: str) -> Any:
        try:
            imported_module = import_module(f"{self.controllers}.{controller.lower()}")
            controller_method = getattr(imported_module, method.lower())
            return controller_method
        except ModuleNotFoundError:
            pass
        except AttributeError:
            pass

    def get_executor(self, command: str, given_route: str) -> str:
        for route in self.web.routes:
            try:
                route = Route(route[0], route[1], route[2])
            except Exception as e:
                log.exception(str(e))
            if route.command.upper() == command.upper() and route.route == given_route:
                return route.executor
