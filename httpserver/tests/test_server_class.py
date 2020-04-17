import os

from httpserver import Server


class TestServerClass:
    def test_router_creation(self):
        s = Server()
        assert os.path.exists("router/web.py")
        # os.remove("router/web.py")
        # os.rmdir(s._controllers)

    def test_router_creation_when_dir_already_exists(self):
        s = Server()
        assert os.path.exists("router/web.py")
        # os.remove("router/web.py")
        # os.rmdir("router")
        # os.rmdir(s._controllers)

    def test_folder_creation(self):
        Server(controllers="contrls")
        assert os.path.exists("contrls")
        os.rmdir("contrls")
        os.remove("router/web.py")
        os.rmdir("router")

    def test_run_called(self):
        s = Server()
        s.run()
        assert os.path.exists(s._controllers)
        # os.rmdir(s._controllers)
        # os.remove(s._router)
        # os.rmdir("/".join(s._router.split("/")[:-1]))
