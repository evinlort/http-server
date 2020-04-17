import logging
import os

log_format = "%(asctime)s: %(filename)s %(funcName)s :%(lineno)s => %(message)s"

logging.basicConfig(level=logging.DEBUG, format=log_format)
log = logging.getLogger("http_server")

if not os.path.exists("logs"):
    os.makedirs("logs")

file_handler = logging.FileHandler(f"logs/httpserver.log")
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
