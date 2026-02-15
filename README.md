
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

git clone https://github.com/mdimran2211/sentiment-analyzer.git
cd sentiment-analyzer

2. Create a virtual environment:
python -m venv venv
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate



3.Install dependencies:
pip install -r requirements.txt


4.Add your Twitter Bearer Token safely:
Create a file key.env:
BEARER_TOKEN=YOUR_NEW_BEARER_TOKEN_HERE
Do not commit this file to GitHub.
Or use Streamlit Secrets for deployment on Streamlit Cloud.


🎯 Usage
Local
streamlit run app.py
Enter your text in the manual input box to analyze sentiment.

Enter a topic to search tweets and see live sentiment analysis.

Streamlit Cloud (Live)

Push your repo to GitHub.

Connect the repo to Streamlit Cloud.

Add the Bearer Token in Secrets.

Deploy → your live app will be ready.

Live Demo: Click here to open app

🛡️ Security Notes

Never share your Bearer Token publicly.

Keep key.env in .gitignore.

Use Streamlit Secrets for live deployments.

Regenerate tokens if they are leaked or exposed.

📌 Author

MD Imran
GitHub: mdimran2211
