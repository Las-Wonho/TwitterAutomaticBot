import tweepy


class Twitter:
    def __init__(self):
        consumerKey = "drUtc6UoLs5gPM3UOclKzkGkK"
        consumerSecret = "uup8NH3yClVDSsyB8QhAyoxcpkECF5FoKaaa6AaZ5EkeZqX3KF"
        self.auth = tweepy . OAuthHandler(
            consumerKey, consumerSecret, callback=None)

    def Auth(self, IT, IS):
        
        self.auth.set_access_token(IT, IS)
        self.api = tweepy.API(self.auth)
        return

    def newAccount(self):
        return self.auth.get_authorization_url()

    def joinAccount(self, verifier):
        self.auth.get_access_token(verifier)
        self.auth.set_access_token(
            self.auth.access_token.key, self.auth.access_token.secret)

    def tweet(self, string):
        self.api.update_status(status=string)


tw = Twitter()
webbrowser.open_new_tab(tw.newAccount())
#tw.Auth(IKATTHAN_T, IKATTHAN_S)
tw.joinAccount(input('code'))
while(True):
    _tweet = input('>')+'\r\n'+'#test'
    try:
        tw.tweet(_tweet)
    except:
        try:
            tw.tweet("너무 자주합니다.")
        except:
            pass
        print("너무 자주보고싶어합니다.")

    
