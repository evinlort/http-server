class HttpServer:
    def __init__(self, *, port: int = 8080, routing: str = "routing/web", controllers: str = "controllers",
                 css: str = "css", js: str = "js", html: str = "html"):
        self._port = int(port)

    def set_port(self, port: int):
        self._port = int(port)

    def get_port(self):
        return self._port
