import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes
from random import randint

class_names = ["Class" + c_name for c_name in "ABCDEFGHIJ"]
# print(class_names)
student_names = ["Student" + s_name for s_name in "ABCDEFGHIJ"]
test_name = ["Math", "Language", "Science"]