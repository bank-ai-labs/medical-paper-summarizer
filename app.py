import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.title("Medical Paper Summarizer")

text = st.text_area("Paste medical abstract here")

if st.button("Summarize"):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this medical paper:\n{text}"
            }
        ]
    )

    st.write(response.choices[0].message.content)