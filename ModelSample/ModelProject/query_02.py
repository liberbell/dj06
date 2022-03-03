from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students, Person

# print(Students.objects.all())
ids = [13, 14, 15]
print(Students.objects.filter(pk__in=ids))

# print(Students.objects.filter(name__contains="Er"))

p = Person(
    first_name = "Alex", last_name = "Hepp",
    birthday = "2000-01-01", email="abc@example.com", salary=None, memo="Alex memo",
    web_site = "https://example.com"
)
p.save()