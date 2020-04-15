class HttpServer:
    def __init__(self, *, port: int = 8080):
        print("HttpServer is initialized")
        self.port = int(port)

    def set_port(self, port: int):
        self.port = int(port)

    def get_port(self):
        return self.port
