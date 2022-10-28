from django import forms
from django.forms import ValidationError
from .models import student

def validate_mark(value):
    if value < 0:
        raise ValidationError('mark must be a positive number')

def validate_age(value):
    if value <= 6:
        raise ValidationError('age must be greater than 6')

class studentForm(forms.ModelForm):
    mark = forms.IntegerField(validators=[validate_mark])
    age = forms.IntegerField(validators=[validate_age])

    class Meta:
        model = student
        fields = '__all__'

class parentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = '__all__'

class subjectForm(forms.ModelForm):

    class Meta:
        model = student
        fields = '__all__'