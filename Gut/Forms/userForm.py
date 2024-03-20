from django.shortcuts import render, redirect
from django import forms
from Pages.models import prompts

#create model form
class AssessmentForm(forms.ModelForm):
    class Meta:
        model = prompts
        fields = '__all__'

#create the assessment form
form = AssessmentForm()

#create a form to change the existing assessment    
assess = Assess.objects.