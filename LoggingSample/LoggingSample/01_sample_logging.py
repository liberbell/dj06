import logging
from tkinter.tix import ListNoteBook

logging.basicConfig(
    level=logging.ERROR, filename="sample.log",
    filemode="w", format="%(asctime)s-%(process)s-%(levelname)s- %(message)s"
)

logging.debug("debug.log")
logging.info("info.log")
logging.warning("warning.log")
logging.error("error.log")
logging.critical("critical.log")