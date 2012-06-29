from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import webbrowser
from jinja2 import Template
import models.home as model
import tweepy
import twitter
import sys
from pymongo import Connection
connection = Connection('localhost', 27017)
db = connection.test_database
db = connection['test-database']
collection = db.test_collection
app = Flask(__name__)
CONSUMER_KEY = 'St8n8AHvZAnCAelRK6xRQ'
CONSUMER_SECRET = 'NiyVw3BhHgMGE5CVGCS5VcVRShlHqoIIbizwCNqXk'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url=" "
<<<<<<< HEAD
ACCESS_KEY=" "
ACCESS_SECRET=" "
infl=[]
top_scores=[]
=======
infl=[]
>>>>>>> 12df44735741d83e13a31c2a1849cc750d7e9977
urll=[]

@app.route('/index', methods=['GET', 'POST'])
def index():	
<<<<<<< HEAD


	
##	AUTHORIZING
	if 'ACCESS_KEY' in session:

=======
	session['user_pin'] = request.form['user_pin']

##	AUTHORIZING

	if 'user_pin' in session:	
>>>>>>> 12df44735741d83e13a31c2a1849cc750d7e9977
		try:
			api = twitter.Api(consumer_key=CONSUMER_KEY,
			consumer_secret = CONSUMER_SECRET,
<<<<<<< HEAD
			access_token_key=escape(session['ACCESS_KEY']),
			access_token_secret=escape(session['ACCESS_SECRET']))
		
		except Exception, e:
		       return render_template('errorPage.html', error=e)
	else:
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
			
			except Exception, e:
			       return render_template('errorPage.html', error=e) 	
		else:
			 return render_template('errorPage.html', error=e)
	user=api.VerifyCredentials()

##	MENTIONS
	mentions=api.GetMentions()
	mname=[]
	mid=[]
	m=0
	for mention in mentions:
		mid.append(mention.GetUser().GetId())
		m=m+1	
	muser=model.calc_mention(mid)
	k=0
	while len(infl)>0: infl.pop()
	while len(urll)>0: urll.pop()				
	while k<3 and k<len(muser):
		infl.append(api.GetUser(muser[k][0]))
		urll.append(infl[k].GetProfileImageUrl())
		k=k+1
##	LISTS
	list_count=user.GetListedCount()
	list_score=model.calc_list(list_count)
	
#	FOLLOWERS COUNT
	
	folls=user.GetFollowersCount()
	foll_score=model.calc_follower_count(folls)
	
##	FRIENDS
	friends=user.GetFriendsCount()
	friends_score=model.calc_friends(folls,friends)
	
	
# 	RETWEET/TWEET RATIO
=======
			access_token_key=ACCESS_KEY,
			access_token_secret=ACCESS_SECRET)
			
		except Exception, e:
		       return render_template('errorPage.html', error=e) 	
		user=api.VerifyCredentials()

##	MENTIONS
		mentions=api.GetMentions()
		mname=[]
		mid=[]
		m=0
		for mention in mentions:
			mid.append(mention.GetUser().GetId())
			m=m+1	
		muser=model.calc_mention(mid)
		k=0
		while len(infl)>0: infl.pop()
		while len(urll)>0: urll.pop()				
		while k<3 and k<len(muser):
			infl.append(api.GetUser(muser[k][0]))
			urll.append(infl[k].GetProfileImageUrl())
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
		
		retweet_count=0		
		tweet_count=0
		status=api.GetUserTimeline(count=200)		
		tweets=user.GetStatusesCount()	
		for stat in status:		
			retweet_count=retweet_count+stat.GetRetweetCount()
			tweet_count=tweet_count+1
		ratio_score=model.calc_tweet_ratio(retweet_count,tweet_count)
>>>>>>> 12df44735741d83e13a31c2a1849cc750d7e9977
		
	retweet_count=0		
	tweet_count=0
	status=api.GetUserTimeline(count=200)		
	tweets=user.GetStatusesCount()	
	for stat in status:		
		retweet_count=retweet_count+stat.GetRetweetCount()
		tweet_count=tweet_count+1
	ratio_score=model.calc_tweet_ratio(retweet_count,tweet_count,tweets)
	
##     CALCULATING FOLLOWERS SCORE
<<<<<<< HEAD
	
	l=[]
	follower_score=0
	i=0
	followers_list=api.GetFollowers()
	for follower in followers_list:
		l.append(follower.GetFollowersCount())
		i=i+1	
	follower_score=model.calc_top_followers(l,i)		
	
	
#	CALCULATING FINAL SCORE
	final_score="{0:.2f}".format(follower_score+ratio_score+friends_score+foll_score+list_score)
	dbscore=float(final_score)
	nam=user.GetScreenName()
	url=user.GetProfileImageUrl()
	posts = db.posts
	if 'ACCESS_KEY' in session:
		posts.rank.update({"name": nam},{"$set": {"score": dbscore}},True)			
	else:
		posts.rank.update({"name": nam},{"$set": {"score": dbscore,"key": ACCESS_KEY,"secret": ACCESS_SECRET}},True)		
	rank=0
	for pt in posts.rank.find({"score":{"$gt": dbscore}}).sort("score",-1):
		rank=rank+1
	for pt in posts.rank.find().sort("score",-1):
		print pt["name"]
	print "SCREEN NAME:" + user.GetScreenName()
	total_ranks=posts.rank.count()
	rank=rank+1
	none="      "
	if len(muser)>=3:
		return render_template('scorePage.html', namee=nam, score=final_score,	 url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=urll[1],url3=urll[2],infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=infl[2].GetName(),rank=rank,total_ranks=total_ranks,arr=top_scores) 
	elif len(muser)==2:
		return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=urll[1],url3=none,infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=none,rank=rank,total_ranks=total_ranks,arr=top_scores)
	elif len(muser)==1:
		return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=none,url3=none,infl1=infl[0].GetName(),infl2=none,infl3=none,rank=rank,total_ranks=total_ranks,arr=top_scores)
	else:
		return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=none,url2=none,url3=none,infl1=none,infl2=none,infl3=none,rank=rank,total_ranks=total_ranks,arr=top_scores)
	
        return "Pin incorrect"
		   
@app.route('/login', methods=['GET', 'POST'])

def login():
	username=request.form['username']
	posts = db.posts
	
	print "User" + username

    	pt=posts.rank.find_one({"name":username})
	if pt!=None:
		print "INSIDE LOOOOP"
		session['ACCESS_KEY']=pt['key']
		session['ACCESS_SECRET']=pt['secret']
		return redirect(url_for('index'))		
	else:	
		urll_auth=request.form['url1']
		return render_template('pin.html',  url=urll_auth,arr=top_scores)
=======
		
		l=[]
		follower_score=0
		i=0
		followers_list=api.GetFollowers()
		for follower in followers_list:
			l.append(follower.GetFollowersCount())
			i=i+1	
		follower_score=model.calc_top_followers(l,i)		
		
		
##	CALCULATING FINAL SCORE

		final_score="{0:.2f}".format(follower_score+ratio_score+friends_score+foll_score+list_score)
		dbscore=float(final_score)
		nam=user.GetName()
		url=user.GetProfileImageUrl()
		posts = db.posts
		posts.rank.update({"name": nam},{"$set": {"score": dbscore}},True)		
		rank=0
		for pt in posts.rank.find({"score":{"$gt": dbscore}}).sort("score",-1):

			rank=rank+1
		total_ranks=posts.rank.count()
		rank=rank+1
		none="      "
		if len(muser)>=3:
			return render_template('scorePage.html', namee=nam, score=final_score,	 url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=urll[1],url3=urll[2],infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=infl[2].GetName(),rank=rank,total_ranks=total_ranks) 
		elif len(muser)==2:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=urll[1],url3=none,infl1=infl[0].GetName(),infl2=infl[1].GetName(),infl3=none,rank=rank,total_ranks=total_ranks)
		elif len(muser)==1:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=urll[0],url2=none,url3=none,infl1=infl[0].GetName(),infl2=none,infl3=none,rank=rank,total_ranks=total_ranks)
		else:
			return render_template('scorePage.html', namee=nam, score=final_score, url=url, follower=folls, retweet=retweet_count, tweet=tweets, url1=none,url2=none,url3=none,infl1=none,infl2=none,infl3=none,rank=rank,total_ranks=total_ranks)
		
	return "Pin incorrect"
		   
@app.route('/login', methods=['GET', 'POST'])

def login():		
	urll_auth=request.form['url1']
	return render_template('pin.html',  url=urll_auth)
>>>>>>> 12df44735741d83e13a31c2a1849cc750d7e9977
	
@app.route('/', methods=['GET', 'POST'])

def pin():
<<<<<<< HEAD
    posts = db.posts
    i=0
    while len(top_scores)>0: top_scores.pop()
    for pt in posts.rank.find().sort("score",-1):
	i=i+1	
	ar1=[pt["name"],str(pt["score"])]
    	top_scores.append(ar1)
	if i==10:
		break;


=======
>>>>>>> 12df44735741d83e13a31c2a1849cc750d7e9977
    auth_url = auth.get_authorization_url()    
    return render_template('temp.html', url=auth_url,arr=top_scores)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('ACCESS_SECRET', None)
    session.pop('ACCESS_KEY', None)
    session.pop('user_pin', None)
    return redirect(url_for('pin'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT5'

if __name__ == '__main__':
    app.debug= True
    app.run()
