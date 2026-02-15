from textblob import TextBlob

text = input("Enter sentence: ")

analysis = TextBlob(text)

print("Polarity:", analysis.sentiment.polarity)

if analysis.sentiment.polarity > 0:
    print("Sentiment: Positive")
elif analysis.sentiment.polarity == 0:
    print("Sentiment: Neutral")
else:
    print("Sentiment: Negative")
