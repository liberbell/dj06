import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person
from django.utils import timezone
import pytz

person = Person.objects.get(id=1)
person.birsthday = "2001-01-01"
person.update_at = timezone.datetime.now(pytz.timezone("Asia/Tokyo"))
person.save()