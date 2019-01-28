from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler

#consumer_key=''
#consumer_secret=''
#access_token=''
#access_token_secret=''

access_token = "1088424708935217152-nxrND8jD3JZdNNGX4z45MLyxGc8uFQ"
access_token_secret = "fg4Nwecl1cibJXs2kL4R2xQEmYYYEfUGVTgbLONfUUD2b"
consumer_key = "SqYdDfsc5velqliInagjHeWCI"
consumer_secret = "ZqqSLmybc2o2CbAZcyLWbAYGKQ1ToETpvpyawe5GEaOY97G42K"

class Listener(StreamListener):
    def on_data(self,data):
        print data
        return True
    def on_error(self,status):
        print status

if __name__ == '__main__':
    l=Listener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    stream=Stream(auth,l)
    stream.filter(track=['bigdata','machineleaning','devops','analytics','softwaredeveloper'])