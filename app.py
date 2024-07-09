import os

import streamlit as st

from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

# initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_images(description: str, num_of_images: int):
    img_response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1
    )

    img_url = img_response.data[0].url
    return img_url

# set page config
st.set_page_config(page_title="DALL-E Image Generator", page_icon=":camera:")

# heading
st.title("DALL-E Image Generator")
st.subheader("Powered by OpenAI's DALL-E")

# body
img_description = st.text_input("Enter description for the image you want to generate")
num_of_images = st.slider("Number of images to generate", 1, 5, 1)
generate_btn = st.button("Generate Images")

if generate_btn:
    generated_img = generate_images(img_description, num_of_images)
    st.image(generated_img)