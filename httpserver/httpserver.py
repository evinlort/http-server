class HttpServer:
    def __init__(self, *, port: int = 8080):
        print("HttpServer is initialized")
        self.port = port

    def set_port(self, port: int):
        self.port = port

    def get_port(self):
        return self.port
