from atexit import register
from django import template

register = template.library()

@register.filter(name="calculate_datetime_to_now")
def calculate_datetime_to_now(value):
    