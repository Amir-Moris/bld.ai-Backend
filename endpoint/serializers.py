from dataclasses import field
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *

# validations
def validate_mark(value):
        if value < 0:
            raise ValidationError('Error! ... mark must be a positive number')

def validate_age(value):
    if value <= 6:
        raise ValidationError('Error! ... age must be greater than 6')

# serializers
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(validators = [validate_mark])
    age = serializers.IntegerField(validators = [validate_age])
    subjects = SubjectSerializer(many = True)

    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'