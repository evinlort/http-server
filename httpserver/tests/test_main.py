import pytest

import httpserver as h


class TestMain:
    def test_instance(self):
        assert "HttpServer" in dir(h)

    def test_default_port(self):
        hs = h.HttpServer()
        assert hs.get_port() == 8080

    def test_set_port(self):
        hs = h.HttpServer(port=80)
        assert hs.get_port() == 80

    def test_set_port_by_setter(self):
        hs = h.HttpServer()
        hs.set_port(80)
        assert hs.get_port() == 80

    def test_faulty_port_definition(self):
        with pytest.raises(TypeError) as excinfo:
            # noinspection PyArgumentList
            h.HttpServer(80)
        assert "takes 1 positional argument but 2 were given" in str(excinfo.value)
