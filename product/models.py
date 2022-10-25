from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class student(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    Class = models.CharField(max_length=64)
    age = models.IntegerField()
    email = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'student'
    def __str__(self):
        return self.firstName
