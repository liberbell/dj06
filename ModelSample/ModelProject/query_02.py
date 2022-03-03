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
# print(Students.objects.filter(pk__in=ids))

# print(Students.objects.filter(name__contains="Er"))

p = Person(
    first_name = "Alex", last_name = "Hepp",
    birthday = "2000-01-01", email="abc@example.com", salary=None, memo="Alex memo",
    web_site = "https://example.com"
)
# p.save()

# print(Person.objects.filter(salary__isnull=True))
# print(Person.objects.exclude(salary__isnull=True))

# print(Students.objects.exclude(name="Elton"))

# print(Students.objects.values("name", "age").filter(pk=14).query)
# students = Students.objects.values("id", "name", "age")
# for student in students:
#     print(student["id"], student["name"])

print(Students.objects.order_by("-name", "id"))