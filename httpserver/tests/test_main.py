import pytest

import httpserver as h
from httpserver.exceptions import *


class TestMain:
    def test_instance(self):
        assert "HttpServer" in dir(h)

    def test_init_no_webfile(self):
        with pytest.raises(RouterFileNotFoundException) as excinfo:
            hs = h.HttpServer(port=80, routing="../routing/webXXX", controllers="controllers", js="js", css="css",
                              html="html")
        print(excinfo)

    def test_init_server_kwargs(self):
        hs = h.HttpServer(port=80, routing="../routing/web", controllers="controllers", js="js", css="css", html="html")
        assert hs._port == 80

    def test_init_server_default(self):
        hs = h.HttpServer(routing="../routing/web")
        assert hs._port == 8080

    def test_default_port(self):
        hs = h.HttpServer(routing="../routing/web")
        assert hs.get_port() == 8080

    def test_set_port(self):
        hs = h.HttpServer(port=80, routing="../routing/web")
        assert hs.get_port() == 80

    def test_faulty_port_definition(self):
        with pytest.raises(TypeError) as excinfo:
            # noinspection PyArgumentList
            h.HttpServer(80)
        assert "takes 1 positional argument but 2 were given" in str(excinfo.value)

    def test_controllers_folder_exists(self):
        hs = h.HttpServer(port=80, routing="../routing/web", controllers="../controllers")
        assert hs.get_controllers == "../controllers"


class TestSetterGetters:
    def test_set_port_by_setter(self):
        hs = h.HttpServer(routing="../routing/web")
        hs.set_port(80)
        assert hs.get_port() == 80

    def test_set_router_by_setter(self):
        hs = h.HttpServer(routing="../routing/web")
        hs.set_router("w")
        assert hs.get_route() == "w.py"

    def test_fault_set_router_by_setter(self):
        with pytest.raises(RouterFileNotFoundException) as err:
            hs = h.HttpServer(routing="../routing/web")
            hs.set_router("wX")
        assert hs.get_route() == "../routing/web.py"

    def test_controllers__by_setter(self):
        hs = h.HttpServer(port=80, routing="../routing/web")
        hs.set_controllers("../controllers")
        assert hs.get_controllers() == "../controllers"
