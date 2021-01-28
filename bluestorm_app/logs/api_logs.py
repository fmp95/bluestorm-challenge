from logging import getLogger, FileHandler, StreamHandler, DEBUG

from .settings import base_format

api_logs = getLogger("api_logs")

api_logs_handler = FileHandler("logs/api.log", mode="a")
api_logs_handler.setFormatter(base_format)

api_logs.addHandler(api_logs_handler)

api_logs.setLevel(DEBUG)