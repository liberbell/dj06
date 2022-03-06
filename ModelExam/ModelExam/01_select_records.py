import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students

student = Students.objects.get(pk=1)
for test_result in student.testresults_set.all():
    print(Students.class_fk.name, student.name, test_result.test.name, test_result.score)