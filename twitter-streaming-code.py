from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler

# enter Twitter API Keys
consumer_key=' Enter your key'
consumer_secret=' Enter your key'
access_token=' Enter your key'
access_token_secret=' Enter your key'


# class which prints recieved data 
class Listener(StreamListener):
    def on_data(self,data):
        print data
        return True
    def on_error(self,status):
        print status

if __name__ == '__main__':
    # authentication with twitter api for streaming
    l=Listener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret) 
    stream=Stream(auth,l)
    
    # filter tweet based on keywords
    stream.filter(track=['bigdata','machineleaning','devops','analytics','softwaredeveloper'])
