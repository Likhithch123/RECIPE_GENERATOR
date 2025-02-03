import streamlit as st #type: ignore
import os
from dotenv import load_dotenv
import google.generativeai as genai #type: ignore

load_dotenv(override=True)

API_KEY = os.getenv('GOOGLE_API_KEY1')

genai.configure(api_key=API_KEY)

def generate_recipe(ingredients):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Give me recipe with {ingredients}")

    return response.text


st.title('RECIPE GENERATOR')

ingredients = st.text_input("Give me the ingredients you have (in csv): ")

if st.button("Get Recipe"):
    if ingredients:
        recipe = generate_recipe(ingredients)
        st.markdown(recipe)
    else:
        st.warning("Please enter some values.")