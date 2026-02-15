import streamlit as st
from textblob import TextBlob

st.title("Social Media Sentiment Analyzer")

text = st.text_area("Enter your comment:")

if st.button("Analyze"):
    if text != "":
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            st.success("Positive 😊")
        elif polarity == 0:
            st.warning("Neutral 😐")
        else:
            st.error("Negative 😡")
    else:
        st.write("Enter text first")
