from datetime import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person

Person.objects.filter(first_name="Bob").delete()