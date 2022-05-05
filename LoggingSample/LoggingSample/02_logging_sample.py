from asyncio.log import logger
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler("sample2.log", encoding="utf-8")

logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")