from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os
from unicodedata import name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students, Schools
# for student in Students.objects.all():
#     print(student.name, student.school.name, student.school.prefecture.name)

# for student in Students.objects.filter(school__name="East side School"):
#     print(student.name, student.school.name, student.school.prefecture.name)

for student in Students.objects.exclude(school__name="North side School"):
    print(student.name, student.school.name, student.school.prefecture.name)