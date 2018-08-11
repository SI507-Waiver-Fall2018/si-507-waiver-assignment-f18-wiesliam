# these should be the only imports you need
import tweepy
import nltk
nltk.download('averaged_perceptron_tagger')
import json
import sys
from nltk.corpus import stopwords
stopwords = set(stopwords.words("english"))
stopwords.update(["http", "https", "RT"])

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
#print("hey")
username = sys.argv[1]
num_tweets = sys.argv[2]


def iterate(tagged_words, tag):
	#print(tagged_words, tag)
	relevant_terms = {}
	for term in tagged_words:
		#print(term[1])
		if term[1][:2] == tag:
			#print(term[1])
			if term[0] not in relevant_terms:
				relevant_terms[term[0]] = 1
			else:
				relevant_terms[term[0]] = relevant_terms[term[0]] + 1

	sorted_words = sorted(relevant_terms.items(), key = lambda x:x[1], reverse = True)
	return sorted_words[:5]

#print("username: ", username)
#print("num_tweets: ", num_tweets)

# Consumer keys and access tokens, used for OAuth
consumer_key = 'SxM3por7g49vIAt0g1KD3UBBv'
consumer_secret = '4RqeT8ZvXk1LvA8KVf1eda01nMuHoOMU8SVrfFOlYrTkVpF9X9'
access_token = '908931385-jKSI38RjL9OWzdkd5P4mlEyQ972PlhvDThZZd8KT'
access_token_secret = 'GzzhQSI51PqtGZaLF1IjdbJeppg9bXJsAZLZdpqA7bfvD'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name = username, count = int(num_tweets), includeRts = True)
#print(tweets)
#print(api.user_timeline(screen_name = username, count = int(num_tweets), includeRts = False))
text_contents = []
for tweet in tweets:
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
		text_contents.append(tweet.text)

#print(text_contents)

lines = []
for line in text_contents:
	if line != "":
		lines.append(line)

words = []
for line in lines:
    tokenized = nltk.word_tokenize(line)
    words.extend(tokenized)

#print(words)

no_stopwords = []
for word in words:
    if word[0].isalpha():
        if word not in stopwords:
            no_stopwords.append(word)

#print(no_stopwords)

tagged = nltk.pos_tag(no_stopwords)
#print(tagged)

verbs = iterate(tagged, "VB")
nouns = iterate(tagged, "NN")
adjectives = iterate(tagged, "JJ")

retweeted_count = 0
favorited_count = 0

for tweet in tweets:
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
		retweeted_count = retweeted_count + tweet.retweet_count
		favorited_count = favorited_count + tweet.favorite_count



print("USER: ", username)
print("TWEETS ANALYZED: ", num_tweets)
print("VERBS: ", verbs)
print("NOUNS: ", nouns)
print("ADJECTIVES: ", adjectives)
print("ORIGINAL TWEETS: ", len(text_contents))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", favorited_count)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweeted_count)