import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes
from random import randint

class_names = ["Class" + c_name for c_name in "ABCDEFGHIJ"]
# print(class_names)
student_names = ["Student" + s_name for s_name in "ABCDEFGHIJ"]
test_names = ["Math", "Language", "Science"]

inserterd_tests = []
for test_name in test_names:
    test = Tests(
        name = test_name
    )
    test.save()
    inserterd_tests.append(test)

for class_name in class_names:
    insert_class = Classes(
        name=class_name
    )
    insert_class.save()
    for student_name in student_names:
        name = class_name + " " + student_names