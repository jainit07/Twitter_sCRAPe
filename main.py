import tweepy
import pandas as pd
import time

# Credentials

consumer_key = "XXXXXX"
consumer_secret = "XXXXXX"
access_token = "XXXXXX"
access_token_secret = "XXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# tweets = []
#
#
# def username_tweets_to_csv(username, count):
#     try:
#         # Creation of query method using parameters
#         tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)
#
#         # Pulling information from tweets iterable object
#         tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
#
#         # Creation of dataframe from tweets list
#         # Add or remove columns as you remove tweet information
#         tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text'])
#
#         # Converting dataframe to CSV
#         tweets_df.to_csv('{}-tweets.csv'.format(username), sep=',', index=False)
#
#     except BaseException as e:
#         print('failed on_status,', str(e))
#         time.sleep(3)
#
#
# # Input username to scrape tweets and name csv file
# # Max recent tweets pulls x amount of most recent tweets from that user
# username = 'jack'
# count = 150
#
# # Calling function to turn username's past X amount of tweets into a CSV file
# username_tweets_to_csv(username, count)

tweets = []


def text_query_to_csv(text_query, count):
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search, q=text_query).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text'])

        # Converting dataframe to CSV
        tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index=False)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)  # Input search query to scrape tweets and name csv file


# Max recent tweets pulls x amount of most recent tweets from that user
text_query = 'USA Election 2020'
count = 150

# Calling function to query X amount of relevant tweets and create a CSV file
text_query_to_csv(text_query, count)
