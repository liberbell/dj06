import logging
from tkinter.tix import ListNoteBook

logging.basicConfig(
    level=logging.error, filename="sample.log",
    filemode="w", format="%(asctime)s-%(process)s-%(levelname)s- %(message)s"
)