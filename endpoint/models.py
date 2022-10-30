from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def check_name(value):
    for ch in value:
        if ch.isalpha() == False:
            raise ValidationError(_("Invalid character, all characters must be alphabet only"), params = {'value': ch})

class Parent(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 64)

    class Meta:
        db_table = "Parent"

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 64, validators = [check_name])
    last_name = models.CharField(max_length = 64, validators = [check_name])
    class_name = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)
    age = models.IntegerField()
    mark = models.IntegerField(blank = True, null = True)
    parent = models.ForeignKey(Parent, related_name = "students", on_delete = models.CASCADE, blank = True, null = True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = "Student"

    def __str__(self): 
        return self.full_name()

class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 64)
    students = models.ManyToManyField(Student, related_name = "subjects", blank = True)

    class Meta:
        db_table = "Subject"
