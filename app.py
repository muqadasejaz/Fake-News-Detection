import streamlit as st
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = joblib.load("gbc_model.pkl")
vectorizer = joblib.load("vectorizer.pkl") 

# Set page config
st.set_page_config(page_title="📰 Fake News Detection", layout="centered")

# App title
st.markdown("""
    <h2 style='text-align: center; color: #4B8BBE;'>📰 Fake News Detection App</h2>
    <p style='text-align: center;'>Paste a news article below and find out if it's real or fake!</p>
""", unsafe_allow_html=True)

# Input text
user_input = st.text_area("✍️ Paste News Content Here:", height=250)

# Predict button
if st.button("🔍 Detect"):
    if user_input.strip() == "":
        st.warning("Please paste some news text to analyze.")
    else:
        # Transform input text
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)[0]

        # Display result
        if prediction == 1:
            st.success("✅ This news is predicted to be **REAL**.")
        else:
            st.error("🚫 This news is predicted to be **FAKE**.")

