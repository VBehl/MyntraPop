# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv
import webbrowser 
load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai


os.environ['GOOGLE_API_KEY'] = 'AIzaSyB2lQIodH8iTK8T2eWsAZJ8QSXoCF9uUqA'
# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="MyntraPop")

st.header("MyntraPop")
# input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Find Similar")

if submit:
    response=get_gemini_response('Give the details of the product such that it is easier to search for the product using that decription with some brand name if any given in the image. Describe the product in the provided image in 4-5 words. Analyze the image and provide a concise description in 4-5 words. Dont give any descriptive message just the tags of description',image)
    st.subheader("The Response is")
    st.write(response)
    url = f'https://www.myntra.com/{response}?rawQuery={response}'
    webbrowser.open(url)