import os

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text.replace('.',' *')
    return Markdown(textwrap.indent(text, ' >', predicate= lambda _:True))


#used to securely store your API key
#from google. import userdata
api_key = os.environ.get('API_KEY')

genai.configure(api_key=api_key)

#list models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

#underliyng disease
prompt_1 = "diabetes "
#allergies 
prompt_2 = "lactose intolerant"
#Dietery restirictions
prompt_3="vegan"
#Age
prompt_4="12 years"
#Gender
prompt_5 = "female "

#%%time
response = model.generate_content("Suggest three well balanced and diverse meal plan in tables of rows with days of the week and columns of the different meals using locally sourced ingridients for a person with the following"+ prompt_1+","+ prompt_2+","+ prompt_3+","+ prompt_4+","+ prompt_5)
display(to_markdown(response.text))