from atexit import register
from django import template
from datetime import datetime

register = template.library()

@register.filter(name="calculate_datetime_to_now")
def calculate_datetime_to_now(value):
    join_datetime = datetime.strptime(value, "%Y%m%d")
    now_datetime = datetime.now()
    diff_datetime = now_datetime - join_datetime