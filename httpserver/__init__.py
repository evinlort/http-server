class Server:
    def __init__(self, *, port: int = 8080, router: str = "router/web", controllers: str = "controllers"):
        self._port = int(port)
        self._router = router
        self._controllers = controllers
