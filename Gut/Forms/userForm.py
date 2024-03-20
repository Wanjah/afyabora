from django.shortcuts import render, redirect
from django import forms
from Pages.models import prompts

#create model form
class Form(forms.ModelForm):
    class Meta:
        model = prompts
        fields = '__all__'

