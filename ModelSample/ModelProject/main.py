import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name="Bob", last_name="Mary", birthday="1960/7/1",
    email="bob@example.com", salary=300000, memo="bob memo",
    web_site="www.google.com"
)
p.save()