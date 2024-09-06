import streamlit as st
from run_model import output_img

st.title('Image Generation Consultancy')

prompt = st.text_input("Enter your prompt here:")

if prompt:
    output = output_img(prompt)
    st.image(output, use_column_width=True)
    st.markdown(f"Generated image URL: {output}")

