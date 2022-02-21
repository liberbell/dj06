import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name="Bob", last_name="Mary", birthday="1960-07-01",
    email="bob@example.com", salary=None, memo="bob memo",
    web_site="www.google.com"
)

p = Person(
    first_name="Bob", last_name="Mary", birthday="1960-07-01",
    email="bob@example.com", salary=None, memo="bob memo",
    web_site=""
)
# p.save()

Person.objects.create(
    first_name="Eric", last_name="Clapton",
    email="eric@example.com", salary=150000, memo="class method",
    web_site="None"
)

obj, created = Person.objects.get_or_create(
    first_name="Elton", last_name="Jhon",
    email="eric@example.com", salary=150000, memo="class method",
    web_site="None"
)
print(ojb)
print(created)