from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import webbrowser
from jinja2 import Template
import easygui as eg
import models.home as model
import tweepy
import twitter
app = Flask(__name__)
CONSUMER_KEY = 'St8n8AHvZAnCAelRK6xRQ'
CONSUMER_SECRET = 'NiyVw3BhHgMGE5CVGCS5VcVRShlHqoIIbizwCNqXk'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
infl =[]
urll = []
auth_url=" "

@app.route('/index', methods=['GET', 'POST'])
def index():
	print "Inside Index"	
	session['user_pin'] = request.form['user_pin']
	if 'user_pin' in session:	
		try:
			s= escape(session['user_pin'])		
			auth.get_access_token(s)	
			ACCESS_KEY = auth.access_token.key
			ACCESS_SECRET = auth.access_token.secret
			api = twitter.Api(consumer_key=CONSUMER_KEY,
			consumer_secret = CONSUMER_SECRET,
			access_token_key=ACCESS_KEY,
			access_token_secret=ACCESS_SECRET)
			user=api.VerifyCredentials()
			list_count=user.GetListedCount()
			mentions=api.GetMentions()
		except:
		       eg.msgbox("Pin Incorrect")
		       return redirect(url_for('pin')) 	

##	MENTIONS

		mname=[]
		mid=[]
		m=0
		for mention in mentions:
			mid.append(mention.GetUser().GetId())
			m=m+1	
		muser=model.calc_mention(mid,m)
		k=0
		while k<3 and k<len(muser):
			infl.append(api.GetUser(muser[k][0]))
			urll.append(infl[k].GetProfileImageUrl())
			user4=api.GetUser(muser[k][0])
			print user4.GetName()
			k=k+1

##	LISTS

		list_count=user.GetListedCount()
		list_score=model.calc_list(list_count)
		
##	FOLLOWERS COUNT

		folls=user.GetFollowersCount()
		foll_score=model.calc_follower_count(folls)
		

##	FRIENDS
		friends=user.GetFriendsCount()
		friends_score=model.calc_friends(folls,friends)
		
		
## 	RETWEET/TWEET RATIO

		i1=0		
		status=api.GetUserTimeline()		
		tweets=user.GetStatusesCount()	
		for stat in status:		
			i1=i1+stat.GetRetweetCount()
		ratio_score=model.calc_tweet_ratio(i1,tweets)
		

##     CALCULATING FOLLOWERS SCORE

		l=[]
		follower_score=0
		i=0
		followers_list=api.GetFollowers()
		for follower in followers_list:
			l.append(follower.GetFollowersCount())
			i=i+1	
		follower_score=model.calc_top_followers(l,i)		
		
		
##	CALCULATING FINAL SCORE

		final_score=follower_score+ratio_score+friends_score+foll_score+list_score

		nam=user.GetName()
		url=user.GetProfileImageUrl()
		none="      "
		if len(muser)==3:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=i1, tweet=tweets, url1=urll[0],url2=urll[1],url3=urll[2],infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=infl[2].GetName()) 
		elif len(muser)==2:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=i1, tweet=tweets, url1=urll[0],url2=urll[1],url3=none,infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=none)
		elif len(muser)==1:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=i1, tweet=tweets, url1=urll[0],url2=none,url3=none,infl1=infl[0].GetName(),infl2=none,infl3=none)
		else:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=i1, tweet=tweets, url1=none,url2=none,url3=none,infl1=none,infl2=none,infl3=none)
		
	return "Pin incorrect"
		   
@app.route('/login', methods=['GET', 'POST'])

def login():		
	#if request.method == 'POST':
#		session['user_pin'] = request.form['user_pin']	
#		return redirect(url_for('index'))
	urll_auth=request.form['url1']
#	session['user_pin'] = request.form['user_pin']
	return render_template('pin.html',  url=urll_auth)
	
@app.route('/', methods=['GET', 'POST'])

def pin():
  #  if request.method == 'POST':
#	return redirect(url_for('login'))
    auth_url = auth.get_authorization_url()    
    return render_template('temp.html', url=auth_url)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_pin', None)
    return redirect(url_for('pin'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT5'

if __name__ == '__main__':
    app.debug= True
    app.run()
