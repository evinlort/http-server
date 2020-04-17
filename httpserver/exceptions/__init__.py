class RouterFileNotFoundException(Exception):
    def __str__(self):
        return 'Router file is not found.'


class ControllersFolderNotExists(Exception):
    def __str__(self):
        return "Controllers folder is not found"
