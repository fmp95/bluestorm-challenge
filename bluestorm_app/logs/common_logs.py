from logging import getLogger, FileHandler, StreamHandler, DEBUG
from os.path import isfile

from .settings import base_format

common_logs = getLogger("common_logs")

common_logs_handler = FileHandler("logs/common.log", mode="a")
common_logs_handler.setFormatter(base_format)

common_logs.addHandler(common_logs_handler)

common_logs.setLevel(DEBUG)

if not isfile("logs/common.log"):
    common_logs.info("Log File Created")