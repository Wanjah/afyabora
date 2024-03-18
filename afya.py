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
GOOGLE_API_KEY = '123'

genai.configure(api_key=GOOGLE_API_KEY)

#list models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

#underliyng disease
prompt_1 = "diabetes"
#allergies 
prompt_2 = "lactose intolerant"
#Dietery restirictions
prompt_3="vegan"

#%%time
response = model.generate_content("Provide a breakfast, lunch and dinner meal plan for a preson with the following"+ prompt_1+","+ prompt_2+","+ prompt_3)
display(to_markdown(response.text)) 