
# Live Social Media Sentiment Analyzer

A Streamlit app to analyze sentiment from manual text input and live Twitter topics using **TextBlob** and **Tweepy**. Safe API key handling is included via `.env` files or Streamlit Secrets.

---

## 🚀 Features

1. **Manual Text Sentiment**
   - Enter any text and get sentiment: Positive, Neutral, or Negative.
2. **Live Twitter Sentiment**
   - Search a topic on Twitter and analyze the sentiment of recent tweets.
3. **Safe API Key Handling**
   - Twitter Bearer Token is stored in `.env` (ignored by Git) or Streamlit Secrets.
4. **Interactive Dashboard**
   - Built with **Streamlit**, clean and user-friendly interface.

---

## ⚡ Technologies Used

- Python 3.14
- [Streamlit](https://streamlit.io/)
- [Tweepy](https://www.tweepy.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- Pandas & Matplotlib (for future data visualization)

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/mdimran2211/sentiment-analyzer.git
cd sentiment-analyzer
