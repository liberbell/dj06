from signal import raise_signal
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator():

    def __init__(self):
        pass

    def validate(self, password, user=None):
        if all((re.search('0-9', password), re.search('a-z', password), re.search('A-Z', password))):
            return
        raise ValidationError("Require for password 0-9, a-z, A-Z")

    def get_help_text(self):
        return "Require for password 0-9, a-z, A-Z"