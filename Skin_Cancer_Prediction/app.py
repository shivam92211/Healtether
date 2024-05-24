from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])

    # Check if response.text is iterable before accessing its elements
    if hasattr(response.text, '__iter__'):
        return ' '.join(response.text)
    else:
        return str(response.text)


# def get_response(input,image):
#     if input!="":
#         response = model.generate_content([input,image])
#     else:
#         response.generate_content(image)
#     return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini")

input = "Predict the type of cancer and what stage is it at"
file_uploader = st.file_uploader("Input: ",type=['jpg','jpeg','png'])
image = ""


if file_uploader is not None:
    image = Image.open(file_uploader)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit_button = st.button("Tell me about the image")

if submit_button:
    response = get_response(input,image)
    st.header("The response is")
    st.write(response)
