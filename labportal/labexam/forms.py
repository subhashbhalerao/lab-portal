from django import forms
from django.forms import ModelForm
from . models import CreateExam

class CreateExamForm(ModelForm):
    class Meta:
        model = CreateExam
        fields = '__all__'
