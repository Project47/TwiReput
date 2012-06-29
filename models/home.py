def calc_list(list_count):
	if list_count <20:
		return 2		
	elif list_count <100:
		return 3
	elif list_count <500:
		return 5
	elif list_count <1000:
		return 8
	elif list_count <10000:
		return 11
	elif list_count <50000:
		return 13
	else:
		return 15


def calc_follower_count(folls):
	if folls<20:
		return 3
	elif folls<100:
		return 4
	elif folls<500:
		return 5
	elif folls<1000:
		return 6
	elif folls<10000:
		return 7
	elif folls<100000:
		return 8
	elif folls<1000000:
		return 8
	else: 
		return 10

def calc_friends(folls,friend):
	followers=folls*1.0
	if followers==0:
		return 0
	friends=friend*1.0
	if folls<20:
		ratio_factor=1.0
	elif folls<100:
		ratio_factor=3.0
	elif folls<500:
		ratio_factor=5.0
	elif folls<1000:
		ratio_factor=7.0
	elif folls<10000:
		ratio_factor=9.0
	elif folls<100000:
		ratio_factor=11.0
	elif folls<1000000:
		ratio_factor=13.0
	else: 
		ratio_factor=15.0
	friends_score = (followers/friends)*ratio_factor
	if friends_score>15:
		friends_score=15
	return friends_score

def calc_tweet_ratio(retweets,tweets,total_tweets):	
	if total_tweets==0:
		return 0 			
	if total_tweets<10:
		ratio_factor=2.0
	elif total_tweets<100:
		ratio_factor=4.0
	elif total_tweets<500:
		ratio_factor=8.0
	elif total_tweets<1000:
		ratio_factor=12.0
	elif total_tweets<50000:
		ratio_factor=16.0
	elif total_tweets<100000:
		ratio_factor=20.0
	elif total_tweets<500000:
		ratio_factor=24.0
	elif total_tweets<1000000:
		ratio_factor=28.0
	else:
		ratio_factor=30.0
	
	retweet_count=retweets*1.0
	tweet_count=tweets*1.0
	ratio_score=(retweet_count/tweet_count)*ratio_factor
	if ratio_score>30:
		ratio_score=30
	return ratio_score


def calc_top_followers(followers_count,length):
	k=1
	while k<length:
		j=k-1
		key=followers_count[k]
		while j>=0 and followers_count[j]<key:
			followers_count[j+1]=followers_count[j]
			j=j-1
		followers_count[j+1]=key
		k=k+1	
	total=0
	k=0
	while k<length:
		total=total+followers_count[k]
		k=k+1	
	print "TOTAL FOLLOWERS"
	print length
	if total<10:
		return 1
	elif total<100:
		return 4
	elif total<500:
		return 8
	elif total<1000:
		return 12
	elif total<50000:
		return 16
	elif total<100000:
		return 20
	elif total<500000:
		return 24
	elif total<1000000:
		return 28
	else:
		return 30	

def calc_mention(mention_id):
	t=0
	mention_user=0
	length=len(mention_id)
	u=0
	muser=[]
	if length>0:
		for t in range(0,length):
	
			if mention_user>0:
				flag=0
				for u in range(0,mention_user):
					if muser[u][0] == mention_id[t]:
						flag=1
						muser[u][1] = muser[u][1]+1 
						break
				if flag == 0:
					muser.append([])
					muser[mention_user].append(mention_id[t])
					muser[mention_user].append(1)
					mention_user=mention_user+1
			else:
				muser.append([])
				muser[mention_user].append(mention_id[t])
				muser[mention_user].append(1)
				mention_user=mention_user+1							
		k=1
		while k<mention_user:
			j=k-1
			key=muser[k][1]
			key1=muser[k][0]
			while j>=0 and muser[j][1]<key:
				muser[j+1][0]=muser[j][0]
				muser[j+1][1]=muser[j][1]
				j=j-1
			muser[j+1][0]=key1
			muser[j+1][1]=key
			k=k+1
	return muser
