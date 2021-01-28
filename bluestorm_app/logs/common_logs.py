from logging import getLogger, FileHandler, StreamHandler, DEBUG

from .settings import base_format

common_logs = getLogger("common_logs")

common_logs_handler = FileHandler("logs/common.log", mode="a")
common_logs_handler.setFormatter(base_format)

common_logs.addHandler(common_logs_handler)

common_logs.setLevel(DEBUG)