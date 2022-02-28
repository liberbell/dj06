from datetime import datetime
from email.headerregistry import Address
from importlib.util import resolve_name
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Places, Restaurants

places = [
    ("West Brompton", "London"), ("Ravello", "Salerno")
]
restaurants = ["Lick N hick N", "Sigilgaida"]

for place_name, place_address in places:
    p = Places(name=place_name, address=place_address)
    p.save()
    for restaurant_name in restaurants:
        r = Restaurants(place=p, name=restaurant_name)
        r.save()