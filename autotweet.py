import requests
import tweepy
import logging
from newsapi import NewsApiClient
from time import sleep
import time
from config import create_api

bot = create_api()

print('Bot is up and live')
print('Logging in...')

#Setting up API and auth


print('Auth Successful!!!')

# #Initializing time and date command

def getDate():
    echoTime = time.time()
    currentTime = time.localtime(echoTime)
    return str(currentTime.tm_mday) + "/" +str (currentTime.tm_mon) + "/" + str(currentTime.tm_year)

def getHour():
    echoTime = time.time()
    currentTime = time.localtime(echoTime)
    return str(currentTime.tm_hour)

def getMin():
    echoTime = time.time()
    currentTime = time.localtime(echoTime)
    return str(currentTime.tm_min)

# #Logging logs

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

#Fetching data from the API

print('Collecting new information...')

url = 'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=413f8796a67d4aee8466796c3385dc60'
    
while True:
    news = requests.get(url).json()
    articles = news['articles']

    for article in articles:
        article_title = article['title']
        article_description = article['description']
        article_url = article['url']
        tweet = '"' + article_title + '"' + '\n' + article_description + ' ...Read More 👇🏻' + '\n' + article_url
        try:
            bot.update_status(tweet)
        except tweepy.error.TweepError:
            pass
        print('Information has been retrieved, sending tweet...')
        print("Tweet Sent")
        print('next tweet will be sent after 2 hrs.')
        sleep(7200)


