import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
url = 'https://www.imdb.com/title/tt7678620/'
'''
It takes the article you put there, downlaods it, and
summarizes it, then it puts out a positive output or a
negetive output, depending on how positive or negetive
the words in the summary are.
'''
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)