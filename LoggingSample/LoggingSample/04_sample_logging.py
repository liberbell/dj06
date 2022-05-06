import logging
import logging.handlers
import time

logger = logging.getLogger(__name__)

r_handler=logging.handlers.RotatingFileHandler(
    "logs/rotation_file.log",
    maxBytes=1000,
    backupCount=5,
    encoding="utf-8"
)

t_handler=logging.handlers.TimedRotatingFileHandler(
    "logs/rotating_time_file.log",
    when="S",
    interval=10,
    backupCount=5,
    encoding="utf-8"
)

logger.setLevel(logging.DEBUG)
sample_formatter = logging.Formatter("%(name)s-%(asctime)s-%(levelname)s-%(message)s")
r_handler.setFormatter(sample_formatter)
t_handler.setFormatter(sample_formatter)

logger.addHandler(r_handler)
logger.addHandler(t_handler)

for _ in range(1000):
    logger.debug("debug log")
    logger.info("info log")
    logger.warning("warning log")
    logger.error("error log")
    logger.critical("critical log")
    time.sleep(1)