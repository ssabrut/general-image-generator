# Stable Diffusion Image Generator

This project combines the capabilities of Stable Diffusion from HuggingFace and Stable Diffusion to create an advanced image generation tool. Leveraging Streamlit, it provides a user-friendly interface for generating high-quality images directly from textual descriptions. This tool is designed to assist users in creative endeavors by transforming textual prompts into vivid, imaginative artworks using state-of-the-art AI techniques.

#### Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

#### Setting Up HuggingFace API
1. ##### Obtain HuggingFace API Token:
   - Sign up on HuggingFace's website to obtain an API token.
   - Store the API token securely for authentication.
2. ##### Create .env File:
   - Create a file named .env in the root directory of your project.
   - Add the following line to the .env file:
     ```bash
     HUGGINGFACE_API_TOKEN=your_gemini_api_key_here
     ```

#### Running the Application

To run the application, execute the following command:

```bash
streamlit run app.py
```

##### Contributors
- Michael (ssabrut) - Project Lead & Developer
