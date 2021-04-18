
TWITTER BOT MANUAL:
Following are the file which are present on GitHub and link is also attached to this document.
•	Mytwitterbot.py
•	simple_twit
•	Twitter_bot_configuration
•	MyProfile
•	Data.csv
Mytwitterbot.py is calling two functions. First function is for API call in which login credentials are passing to me and user has to give ID from where tweets would be fetch. Second function I am calling is to get data from user timeline and then we are storing that data into our Data.csv file for sentiment purposes.
Simple_twit.py contains lots of functions which I have already mentioned in introduction part which are (get_home_timeline, get_user_timeline, get_retweets_of_me, get_user, get_user_followers, follow_users, unfollow_users). These function are implemented but in our case we are not calling all of these functions.
Twitter_bot_configuration contains the secret key, access key, credentials for login to twitter developer account and it has MFA code saved in it.
MyProfile contain author information in this case Usman is author of this code, Time and date of project creation and a SQL connector.
Data.csv contains the data which is fetch by running our program and we can enter how much total number of tweets do we need.
To run this twitter bot you need to download these files from github and run in any compiler. In my case I have build it on pycharm. You simple need to run mytwitterbot.py file and rest program will run automatically and will store data into data.csv file. 


