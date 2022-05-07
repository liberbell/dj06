import logging
import logging.config
import time

logging.config.fileConfig(fname="conf/rotation_logger.conf")

logger = logging.getLogger(__name__)

for _ in range(1000):
    logger.debug("debug log")
    logger.info("info log")
    logger.warning("warning log")
    logger.error("error log")
    logger.critical("critical log")
    time.sleep(1)