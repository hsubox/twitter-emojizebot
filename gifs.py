import emoji
import tweepy
import time
import string
from local_settings import *

def connect(): # set up connection to Twitter
    auth = tweepy.OAuthHandler(MY_CONSUMER_KEY, MY_CONSUMER_SECRET)
    auth.set_access_token(MY_ACCESS_TOKEN_KEY, MY_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def post_to_twitter(status, tweetid): # send tweet through Twitter and console
    # api.update_status(status)
    api.update_status(status, in_reply_to_status_id = tweetid)
    print status

def convert_word_to_emoji(x):
    y = u':' + x.lower().translate(string.maketrans("",""), '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~') + ':'
    if y in emoji.EMOJI_UNICODE:
        return emoji.emojize(y)
    return x

def convert_tweet_to_emoji(twt):
    twt = str(twt)
    twt = twt.split(" ") # remove punctuation, break into words
    twt = filter(lambda x: not x.startswith("@"), twt) # remove @bot
    twt = map(convert_word_to_emoji, twt) # convert to emoji
    twt = " ".join(twt) # convert back into string
    return twt
    
def append_mention(user, twt):
    return "@" + user + " " + twt

if DEBUG == True:
    twt = "this is a test! string? input snowflake! ?cat? dog. zap cloud! octopus mount_fuji"
    twt = convert_tweet_to_emoji(twt)
    print(twt)
else:
    api=connect() # connect to Twitter API
    
    # gets the last tweet @ me
    last_mention = api.mentions_timeline(count=1)
    
    # gets my last tweet and gets the "in reply to" tweet value
    my_last_tweet = api.user_timeline(count=1);
    my_last_tweet_reply_to = my_last_tweet[0].in_reply_to_status_id or null
    
    # for debugging
    # print my_last_tweet_reply_to
    # print last_mention[0].id
    
    # only run if last mention has not been responded to
    if (last_mention[0].id != my_last_tweet_reply_to):
    
        last_mention_id = last_mention[0].id
        twt = last_mention[0].text
        tweet_at = last_mention[0].user.screen_name
    
        twt = convert_tweet_to_emoji(twt)
        twt = append_mention(tweet_at, twt)
        post_to_twitter(twt, last_mention_id)
        
        # print "POSTED"
        
    # time.sleep(15*60) # tweets at most every 15 minutes