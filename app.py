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

API_URL = "https://api-inference.huggingface.co/models/ehristoforu/dalle-3-xl-v2"
# API_URL = "https://api-inference.huggingface.co/models/ehristoforu/dalle-3-xl"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

carousel_content = [
    
]

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_images(description: str, num_of_images: int):
    images = []
    for i in range(num_of_images):
        image_bytes = query({"inputs": description})
        image = Image.open(io.BytesIO(image_bytes))
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            image.save(temp_file, format='PNG')
            temp_file_path = temp_file.name

        with open(temp_file_path, 'rb') as temp_file:
            image_data = temp_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
            image_url = f"data:image/png;base64,{base64_encoded_image}"
        
        image_dict = dict({
            "title": f"Image {i+1}",
            "text": description,
            "img": image_url
        })

        images.append(image_dict)
    return images

# set page config
st.set_page_config(page_title="DALL-E Image Generator", page_icon=":camera:")

# heading
st.title("DALL-E Image Generator")
st.subheader("Powered by DALL-E and HuggingFace 🤗")

# body
img_description = st.text_input("Enter description for the image you want to generate")
num_of_images = st.slider("Number of images to generate", 1, 5, 1)
generate_btn = st.button("Generate Images")

if generate_btn:
    generated_img = generate_images(img_description, num_of_images)
    carousel(items=generated_img, width=1)