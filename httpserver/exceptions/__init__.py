class RouterFileNotFoundException(Exception):
    def __str__(self):
        return 'Router file is not found.'
