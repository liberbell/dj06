from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Books, Authors

def insert_books():
    book1 = Books(name="BOOK 1")
    book2 = Books(name="BOOK 2")
    book3 = Books(name="BOOK 3")
    book1.save()
    book2.save()
    book3.save()

def insert_authors():
    author1 = Authors(name="Authors1")
    author2 = Authors(name="Authors2")
    author3 = Authors(name="Authors3")
    author1.save()
    author2.save()
    author3.save()

# insert_books()
# insert_authors()
book1 = Books.objects.get(pk=1)
author1 = Authors.objects.get(pk=1)
author2 = Authors.objects.get(pk=2)

# book1.authors.add(author1, author2)
print(book1.authors.all())
book3.authors.add(author1)
book3.authors.add(author2, author3)