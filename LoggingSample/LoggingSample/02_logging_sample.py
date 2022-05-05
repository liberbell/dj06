from asyncio.log import logger
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")