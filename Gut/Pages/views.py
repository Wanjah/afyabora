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
            try:   
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
                response = model.generate_content("Suggest a well balanced and diverse meal plan in a table of rows with days of the week and columns of different meals(day,breakfast,lunch,dinner,snacks) using locally sourced ingridients"+ prompt_1+"years"+","+ prompt_2+","+ prompt_3+","+ prompt_4+","+ prompt_5+","+ Prompt_6) 

                
                def to_markdown(text):
                    text.replace('.', ' *')
                    return Markdown(textwrap.indent(text, ' >', predicate=lambda _: True))


            # Display generated content
                generatedContent= display(textwrap.indent(response.text, '>'))
                return render(request, 'assess.html', {'form': form}, {'generatedContent': generatedContent})
            except Exception as e:
                #handle any exceptions
                error_message = str(e)
                return render(request, 'error.html', {'error_message':error_message})
    
    
    else:
        form = AssessementForm()

    return render(request, 'assess.html', {'form': form})
