import os

import httpserver.server.server as srv


class Server:
    def __init__(self, *, port: int = 8080, router: str = "router/web", controllers: str = "controllers"):
        self._port = int(port)
        self._router = router
        self.__router_check()
        self.__folder_check(controllers)
        self._controllers = controllers

    def get_port(self) -> int:
        return self._port

    def get_router(self) -> str:
        return self._router

    def get_controllers(self) -> str:
        return self._controllers

    def __router_check(self):
        if self._router[-3:] != ".py":
            self._router += ".py"
        if os.path.exists(self._router):
            return
        router_list = self._router.split("/")
        router_file = router_list[-1]
        router_path = "/".join(router_list[:-1])
        try:
            os.makedirs(router_path)
        except FileExistsError:
            pass
        open(f"{router_path}/{router_file}", "w").close()

    @staticmethod
    def __folder_check(folder_path):
        if os.path.exists(folder_path):
            return
        os.makedirs(folder_path)

    def run(self):
        http_server = srv.ThreadingServer(self)
        srv.run(http_server)
