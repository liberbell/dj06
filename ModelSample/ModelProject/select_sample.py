import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person

persons = Person.objects.all()
for person in persons:
    print(person.id, person)

persons = Person.objects.filter(first_name="Eric", id=2).all()
print(persons)

for person in persons:
    print(person.id, person)