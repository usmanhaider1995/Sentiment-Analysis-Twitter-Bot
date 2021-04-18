

import sys
import time
import simple_twit
import csv
  
def main():

   # verification process
    api = simple_twit.create_api()

    simple_twit.version()
    
    ranomuserid="@CoinDesk"
    #ranomuserid="@gem_detecter"
    #ranomuserid="@jonathanbosh"
    #ranomuserid="@binance"

    timeline=simple_twit.get_user_timeline(api,ranomuserid,15)
    textonly_tweets = [[tweet.full_text] for tweet in timeline]
    print("Tweets From another user Timeline",*textonly_tweets, sep = "\n")
    print("Total tweets From another user timeline",len(textonly_tweets))
    
    print(type(textonly_tweets))
    file = open('data.csv', 'w+', newline ='')
    with file:    
        write = csv.writer(file)
        write.writerow(["Tweets"])
        print("type=================================================================>",type(textonly_tweets))
        for x in textonly_tweets:
            try:
                write.writerows([x])
            except:
                pass

if __name__ == "__main__":
       main()
