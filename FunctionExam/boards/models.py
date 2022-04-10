from turtle import ondrag
from django.db import models

# Create your models here.
class Themes(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        "accounts.Users", on_delete=models.CASCADE
    )