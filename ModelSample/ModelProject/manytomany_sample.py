from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Books, Authors

def insert_books:
    book1 = Books(name="BOOK 1")
    book2 = Books(name="BOOK 2")
    book3 = Books(name="BOOK 3")
    book1.save()
    book2.save()
    book3.save()