import streamlit as st
from transformers import pipeline

st.title("GPT-NEO Text Generation")

# Create a text area for user input
prompt = st.text_area("Enter a prompt:", "The current stock market")

# Check if the user has entered any text and proceed with text generation
if st.button("Generate Text"):
    # Load the generator pipeline
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    # Generate text based on the prompt
    res = generator(prompt, max_length=60, do_sample=True, temperature=0.9)

    # Display the generated text
    st.write("Generated Text:")
    st.write(res[0]['generated_text'])
