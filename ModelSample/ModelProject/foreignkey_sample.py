from datetime import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

prefectures = ["Tokyo", "Osaka"]
schools = ["West side School", "South side School", "East side School", "North side School"]
students = ["Alex", "Bob", "Elton", "Eric"]