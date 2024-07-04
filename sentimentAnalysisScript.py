from textblob import TextBlob

text1 = "I am so happy and love everything"
blob1 = TextBlob(text1)

text2 = "I am so angry and hate everything"
blob2 = TextBlob(text2)

# Get the sentiment
sentiment = blob1.sentiment
print("First line sentiment:", sentiment)
sentiment2 = blob2.sentiment
print("Second line sentiment", sentiment2)
