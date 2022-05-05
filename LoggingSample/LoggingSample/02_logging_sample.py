from asyncio.log import logger
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler("sample2.log", encoding="utf-8")

s_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.error)

s_formatter = logging.Formatter("%(name)s-%(levelname)s-%(message)s")

logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")