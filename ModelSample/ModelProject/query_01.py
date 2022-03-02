from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students
# print(Students.objects.all())

# print(Students.objects.all()[:5])
# print(Students.objects.all()[5:])

# print(Students.objects.all()[5:8])
# print(Students.objects.all()[5:8].query)
# print(Students.objects.first())

# print(Students.objects.filter(name="Bob"))
# print(Students.objects.filter(age=17))

# print(Students.objects.filter(name="Bob", pk__gt=13).query)
# print(Students.objects.filter(name="Bob", pk__lt=20))

# print(Students.objects.all())
# print(Students.objects.filter(name__startswith="E"))
# print(Students.objects.filter(name__endswith="c"))

from django.db.models import Q
print(Students.objects.filter(Q(name="Eric") | Q(pk__gt=19)))