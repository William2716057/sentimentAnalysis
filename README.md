# Sentiment Analysis with TextBlob
This repository provides a simple example of how to perform sentiment analysis using the TextBlob library in Python.

## Installation
First, ensure you have Python installed on your machine. Then, install TextBlob and download the necessary NLTK corpora.

`pip install textblob`

Explanation of Results from script
First Line Sentiment:

1. Text: "I am so happy and love everything"
- Sentiment: Sentiment(polarity=0.65, subjectivity=0.8)
- Polarity: 0.65 (positive sentiment)
- Polarity ranges from -1 (very negative) to 1 (very positive).
- A value of 0.65 indicates a strong positive sentiment.
Subjectivity: 0.8
- Subjectivity ranges from 0 (very objective) to 1 (very subjective).
- A value of 0.8 indicates a high degree of subjectivity, suggesting that the statement is based on personal opinions and feelings.

Second Line Sentiment:

2. Text: "I am so angry and hate everything"
- Sentiment: Sentiment(polarity=-0.65, subjectivity=0.95)
- Polarity: -0.65 (negative sentiment)
- A value of -0.65 indicates a strong negative sentiment.
Subjectivity: 0.95
- A value of 0.95 indicates a very high degree of subjectivity, suggesting that the statement is highly based on personal opinions and emotions.
