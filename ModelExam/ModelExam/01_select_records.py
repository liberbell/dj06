import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, Classes

student = Students.objects.get(pk=1)
# for test_result in student.testresults_set.all():
#     print(student.class_fk.name, student.name, test_result.test.name, test_result.score)

from django.db.models import Sum, Avg, Max, Min

for class_summary in Classes.object.values("name", "students__testresults__test__name").annotate(
    max_socre = Max("students__testresults__score"),
    min_socre = Min("students__testresults__score"),
    avg_socre = Avg("students__testresults__score"),
    sum_socre = Sum("students__testresults__score"),
):
    print(
        class_summary["name"],
        class_summary["students__testresults__test__name"]
    )