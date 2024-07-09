import requests
import os
import io
import tempfile
import base64

import streamlit as st

from PIL import Image
from dotenv import load_dotenv
from streamlit_carousel import carousel
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_images(description: str, index: int):
    image_bytes = query({"inputs": description})
    image = Image.open(io.BytesIO(image_bytes))
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        image.save(temp_file, format='PNG')
        temp_file_path = temp_file.name

    with open(temp_file_path, 'rb') as temp_file:
        image_data = temp_file.read()
        base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
        image_url = f"data:image/png;base64,{base64_encoded_image}"

    image = {
        "title": f"Image {index+1}",
        "text": description,
        "img": image_url
    }
    
    return image

# set page config
st.set_page_config(page_title="Stable Diffusion Image Generator", page_icon=":camera:")

# heading
st.title("Stable Diffusion Image Generator")
st.subheader("Powered by Stable Diffusion and HuggingFace 🤗")

# body
img_description = st.text_input("Enter description for the image you want to generate")
num_of_images = st.slider("Number of images to generate", 1, 5, 1)
generate_btn = st.button("Generate Images")

if generate_btn:
    generated_img = [generate_images(img_description, i) for i in range(num_of_images)]
    carousel(items=generated_img)