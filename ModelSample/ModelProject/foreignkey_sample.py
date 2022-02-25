from datetime import datetime

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
                name = school_name
                prefecture = prefecture
            )
            school.save()
            for student_name in students:
                student = Students(
                    name=student_name, age=17, major="Science", school=school
                )
                student.save()