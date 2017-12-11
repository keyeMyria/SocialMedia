#collect data
from twython import Twython
import re, json


def sa(data):
	f=open("result.json","wb+")
	json.dump(data,f)
	f.close


ACCESS_TOKEN = "936241081993351168-3iG0gr8LXPD7a5iKFUdsQTXaCqxlRih"
ACCESS_SECRET = "TUp9mx6h9lZxl5OnhpELmn2A7fneaI9lMMwL4TTl9ITkP"
CONSUMER_KEY =  "NXozb5bdJP4W2vGCMfw34wpQf"
CONSUMER_SECRET = "Kt0uWBWDhApWRsaTCQWDLpsrWJ71nJqYWtgcVkLtMX4y9Dmt6B"

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
main = {}
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
wordlist= ["i love you","i hate you"]
for wordkey in wordlist:	
 query = twitter.search(q=wordkey,count="10")
 data= {}
 for i,k in enumerate(query['statuses']):
    b=emoji_pattern.sub(r'', k["text"]) 
    b=re.sub(r"@\S+","",b) #deleter user name
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', b) #delete links
    data[str(i)]=text
 main[wordkey]=data



sa(main)


