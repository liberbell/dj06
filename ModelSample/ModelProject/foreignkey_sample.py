from datetime import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

prefectures = ["Tokyo", "Osaka"]
schools = ["West side School", "South side School", "East side School", "North side School"]
students = ["Alex", "Bob", "Elton", "Eric"]

def insert_records():
    for prefecture_name in prefectures:
        prefecture = Prefectures(
            name = prefecture_name
        )
        prefecture.save()
        for school_name in schools:
            school = Schools(
                name = school_name,
                prefecture = prefecture
            )
            school.save()
            for student_name in students:
                student = Students(
                    name=student_name, age=17, major="Science", prefecture=prefecture, school=school
                )
                student.save()


def select_students():
    students = Students.objects.all()
    for student in students:
        print(student.id, student.name, student.school.id, student.school.name, student.school.prefecture.id, student.school.prefecture.name)

# insert_records()
# select_students()
# Schools.objects.filter(id=2).delete()
# Prefectures.objects.filter(id=1).delete()