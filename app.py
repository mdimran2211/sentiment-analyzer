import streamlit as st
from textblob import TextBlob
import tweepy
import os
from dotenv import load_dotenv

# Load safe key from key.env
load_dotenv("key.env")
bearer_token = os.getenv("BEARER_TOKEN")

# Initialize Twitter client
client = tweepy.Client(bearer_token=bearer_token)

st.title("Live Social Media Sentiment Analyzer")

# ---------------------
# 1️⃣ Manual text sentiment
# ---------------------
text = st.text_area("Enter your own text to analyze sentiment:")

if st.button("Analyze My Text"):
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

st.markdown("---")  # separator

# ---------------------
# 2️⃣ Live Twitter sentiment
# ---------------------
topic = st.text_input("Search topic on Twitter")

if st.button("Analyze Tweets"):
    if topic != "":
        tweets = client.search_recent_tweets(query=topic, max_results=10)
        
        if tweets.data:
            for tweet in tweets.data:
                st.write("Tweet:", tweet.text)
                
                analysis = TextBlob(tweet.text)
                if analysis.sentiment.polarity > 0:
                    st.success("Positive 😊")
                elif analysis.sentiment.polarity == 0:
                    st.warning("Neutral 😐")
                else:
                    st.error("Negative 😡")
        else:
            st.write("No tweets found for this topic")
