import snscrape.modules.twitter as twitter
import csv
import pyodbc

class TwitterScraper():
    def __init__(self) -> None:
        self.con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-J87TA1M; DATABASE=twitter3; UID=twitter3user; PWD=123456')
        self.cursor = con.cursor()
        self.maxTweets = 100

    def tweetSearch(self, keyword='trump'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            if i > maxTweets:
                break
            print(i)
            print(tweet.username)
            print(tweet.content)
            print(tweet.date)
            print(tweet.user.location)
            print(tweet.likeCount)
            print(tweet.retweetCount)
            print(tweet.user.followersCount)
            print(tweet.url)
            print(tweet.id)
            print('\n')

    def userTweets(self, username='FlaRenegade'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper('from:' +username+ ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            if i > maxTweets: break
            print(i)
            print(tweet.username)
            print(tweet.content)
            print(tweet.date)
            print(tweet.user.location)
            print(tweet.likeCount)
            print(tweet.retweetCount)
            print(tweet.user.followersCount)
            print(tweet.url)
            print('\n') 

    def userTweets_CSV(self, username='FlaRenegade'):
        with open('WattsLamiel.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i, tweet in enumerate(twitter.TwitterSearchScraper('from:' +username+ ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
                writer.writerow([tweet.username, tweet.content.encode("utf-8"), tweet.date, tweet.user.location, tweet.likeCount, tweet.retweetCount, tweet.user.followersCount, tweet.url])

    def userTweets_Sql(uself, sername='FlaRenegade'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper('from:' +username+ ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            cursor.execute("insert into tweet(username, content, date, location, url) values (?, ?, ?, ?, ?)",
                            tweet.username, tweet.content, tweet.date, tweet.user.location, tweet.url
                            )
            con.commit()
   
    def tweetSearch(self, keyword='trump'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            if i > maxTweets: break
            print(i)
            print(tweet.username)
            print(tweet.content)
            print(tweet.url)
            print('\n')

    def exactPhrase(self, keyword='"python%20learning"'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            if i > maxTweets: break
            print(i)
            print(tweet.username)
            print(tweet.content)
            print(tweet.url)
            print('\n')

    def anyOfWords(self, keyword='(python%20OR%20learning)'):
        for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2020-11-01 until:2021-01-01 lang:"en" ').get_items()):
            if i > maxTweets: break
            print(i)
            print(tweet.username)
            print(tweet.content)
            print(tweet.url)
            print('\n')

    def from_to(self):
        # from:Projects_007 kullanıcısından  to:@mertcobanov kullanıcısına atilan tweetleri çek
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:Projects_007  to:@mertcobanov lang:tr since:2020-01-01 until:2020-12-30').get_items()):
                if i > 1 : break  
                print(tweet.username)
                print(tweet.date)
                print(tweet.content)
                print("\n")

    def geocode(self):
        # geocode:37.7764685,-122.4172004,10km 
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(' geocode:37.7764685,-122.4172004,10km since:2020-01-01 until:2020-12-30').get_items()):
                if i > 20 : break  
                print(tweet.username)
                print(tweet.date)
                print(tweet.content)
                print("\n")

    def userTweets_CSV(self, username='Projects_007'):
        import csv 
        with open('Projects_007.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i, tweet in enumerate(twitter.TwitterSearchScraper('from:' +username+ ' since:2020-11-01 until:2021-01-01 ').get_items()):
                writer.writerow([tweet.username, tweet.content.encode("utf-8"), tweet.date, tweet.url])

    def download_filter_tweets(self, maxTweets, keyword, start, end):
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:tr since:'+start+ ' until:'+end+' -filter:links -filter:replies').get_items()):
            print(tweet.username,tweet.date,tweet.content,str(tweet.outlinks), tweet.url)

    def tweetSearch(self):
        for i, tweet in enumerate(twitter.TwitterSearchScraper('python%20learning since:'+last_3_hour+' until:'+now).get_items()):
            if i > 30: break
            print(i)
            print(tweet.content)





if __name__=="__main__":
    ts = TwitterScraper()

    ts.tweetSearch()
    ts.userTweets('Projects_007')
    ts.userTweets_CSV('Projects_007')
    ts.userTweets_Sql('Projects_007')
