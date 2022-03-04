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
# print(Students.objects.filter(name="Eric").count())

from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.aggregate(Count("pk"), Max("pk"), Min("pk"), Avg("pk"), Sum("age")))

# aggregate_student = Students.objects.aggregate(Count("pk"), Max("pk"), Min("pk"), Avg("pk"), Sum("age"))
# print(aggregate_student["pk__max"])

# print(Students.objects.aggregate(pk_count=Count("pk"), max_pk=Max("pk"), min_pk=Min("pk"), avarage=Avg("pk"), sum=Sum("age")))

# print(Students.objects.values("name", "age").annotate(
#     max_id=Max("pk"), min_id=Min("pk")
# ))

for student in Students.objects.values("name", "age").annotate(
    max_id=Max("pk"), min_id=Min("pk")
):
    print(student["name"], student["max_id"])