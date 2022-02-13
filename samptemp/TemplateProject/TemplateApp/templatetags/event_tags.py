from atexit import register
from django import Template

register = template.Library()
@register.filter(name="status_to_string")

def convert_status_to_string(status):
    if status == 10:
        return "success"
    elif status == 20:
        return "error"
    elif status == 30:
        return "pending"