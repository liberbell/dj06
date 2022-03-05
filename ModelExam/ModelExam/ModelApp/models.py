from django.db import models

# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'
class Students(models.Model):
    name =models.CharField(max_length=50)
    grade = models.IntegerField()ß