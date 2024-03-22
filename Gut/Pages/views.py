from django.shortcuts import render
from .models import AssessementForm
import requests
import os
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# Create your views here.

def AssessmentForm_view(request):
    if request.method =='POST':
        form = AssessementForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            data = form.cleaned_data
            
            # Assign form data to prompts
            prompt_1 = data.get('Age', '')
            prompt_2 = data.get('Gender', '')
            prompt_3 = data.get('Allergies', '')
            prompt_4 = data.get('Medical_Condition', '')
            prompt_5 = data.get('Dietary_Restrictions', '')
            Prompt_6 = data.get('Food_Preferences','')

            # Used to securely store your API key
            api_key = os.environ.get('API_KEY')
            genai.configure(api_key=api_key)

            # List models
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    print(m.name)

            model = genai.GenerativeModel('gemini-pro')

            # Generate content using prompts from form data
            response = model.generate_content(
                "Suggest three well-balanced and diverse meal plans in tables of rows with days of the week and columns of the different meals using locally sourced ingredients for a person with the following: {}, {}, {}, {}, {}".format(
                    prompt_1, prompt_2, prompt_3, prompt_4, prompt_5,Prompt_6
                )
            )

            # Display generated content
            display(to_markdown(response.text))

    else:
        form = AssessementForm()

    return render(request, 'assess.html', {'form': form})

def to_markdown(text):
    text.replace('.', ' *')
    return Markdown(textwrap.indent(text, ' >', predicate=lambda _: True))
