import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# CSV read
df = pd.read_csv("data.csv")

sentiments = []

for text in df['text']:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiments.append("Positive")
    elif polarity == 0:
        sentiments.append("Neutral")
    else:
        sentiments.append("Negative")

df['Sentiment'] = sentiments

print(df)

# count
count = df['Sentiment'].value_counts()
print(count)

# graph
count.plot(kind='bar')
plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
