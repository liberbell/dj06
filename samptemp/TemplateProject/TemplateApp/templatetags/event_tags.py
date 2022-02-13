from atexit import register
from django import Template

register = template.Library()
@register.filter(name="status_to_string")