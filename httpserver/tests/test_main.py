import httpserver as h


class TestMain:
    def test_instance(self):
        assert "HttpServer" in dir(h)

    def test_set_port(self):
        hs = h.HttpServer(port=80)
        assert hs.get_port() == 80

    def test_set_port_by_setter(self):
        hs = h.HttpServer()
        hs.set_port(80)
        assert hs.get_port() == 80
