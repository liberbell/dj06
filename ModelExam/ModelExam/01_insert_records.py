import os
from django import setup
setup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from ModelApp.models import Students, TestResults, Tests, Classes
