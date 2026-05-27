import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Medical Paper Summarizer",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 Medical Paper Summarizer")

st.write(
    "An AI-powered tool that summarizes medical research abstracts into clear, structured clinical insights."
)

st.warning("This tool is for educational purposes only. It is not medical advice.")

text = st.text_area(
    "Paste medical abstract here",
    height=180,
    placeholder="Paste a medical research abstract..."
)

if st.button("Summarize"):
    if not text.strip():
        st.error("Please paste a medical abstract first.")
    else:
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Summarize this medical research abstract in the following format:

## Objective
What was the study trying to find?

## Methods
How was the study conducted?

## Results
What were the key findings?

## Clinical Significance
Why does this matter clinically?

## Limitations
What are the possible limitations?

Use clear, concise language.
Do not provide medical advice.

Abstract:
{text}
"""
                    }
                ]
            )

            st.markdown(response.choices[0].message.content)
