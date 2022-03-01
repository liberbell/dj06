from datetime import datetime
from email.headerregistry import Address

from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

# s = Schools.objects.first()
# print(type(s))
# print(dir(s))
# print(s.prefecture.name)
# print(s.students_set)
# st = s.students_set
# print(type(st))

# from ModelApp.models import Places, Restaurants
# p = Places.objects.first()
# print(type(p))
# print(dir(p))

# print(p.restaurants.name)
# r = Restaurants.objects.first()
# print(r.place.name)
from ModelApp.models import Books, Authors
b = Books.objects.first()
# print(type(b))
# print(dir(b))
# print(b.authors.all())
r = Authors.objects.all()
print(r.books_set.all())