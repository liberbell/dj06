import logging
import logging.handlers

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
)
