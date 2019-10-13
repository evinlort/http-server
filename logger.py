import logging

log_format = "%(asctime)s: %(filename)s %(funcName)s :%(lineno)s => %(message)s"

logging.basicConfig(level=logging.DEBUG, format=log_format)
log = logging.getLogger("http_server")
file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(format)
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
