from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def check_name(value):
    for ch in value:
        if ch.isalpha() == False:
            raise ValidationError(_("Invalid character, all characters must be alphabet only"), params={'value' : ch})

class parent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64)

    class Meta:
        db_table = "parent"

class student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 64, validators = [check_name])
    last_name = models.CharField(max_length = 64, validators = [check_name])
    class_name = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)
    age = models.IntegerField()
    mark = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(parent, related_name="students", on_delete=models.CASCADE, blank=True , null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = "student"

    def __str__(self) : 
        return self.full_name()

class subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64)
    students = models.ManyToManyField(student , related_name = "subjects", blank=True)

    class Meta:
        db_table = "subject"