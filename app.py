import requests
import os
import io

import streamlit as st

from PIL import Image
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/ehristoforu/dalle-3-xl-v2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_images(description: str, num_of_images: int):
    image_bytes = query({
        "inputs": description,
        "parameters": {
            "num_return_sequences": num_of_images
        }
    })

    image = Image.open(io.BytesIO(image_bytes))
    return image

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