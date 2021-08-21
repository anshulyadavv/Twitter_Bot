import tweepy

def create_api():
    info = None

    consumer_key = 'REov37Ec1P30MfGkHTnDJFsqB'
    consumer_secret_key = 'wg9oqia8jyofnxma4RtdKWGIo8fR7jFEhRTEf1IhYNJDqp1xKg'
    access_token = '1407018065217327105-9JR6m5MiG0DiY8HFWTwhEBRmFVGRPw'
    access_token_secret = 'ppcqdT0ld0Fd0BxJcTnkIlOPhKVCsioFTz6WaCU8uctVX'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api