import os

import streamlit as st

from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="DALL-E Image Generator", page_icon=":camera:")

# heading
st.title("DALL-E Image Generator")
st.subheader("Powered by OpenAI's DALL-E")

# body
img_description = st.text_input("Enter description for the image you want to generate")
num_of_images = st.slider("Number of images to generate", 1, 5, 1)
generate_btn = st.button("Generate Images")

if generate_btn:
    pass