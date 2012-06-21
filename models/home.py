def calc_list(list_count):
	if list_count <20:
		list_score=2		
	elif list_count <100:
		list_score=3
	elif list_count <500:
		list_score=5
	elif list_count <1000:
		list_score=8
	elif list_count <10000:
		list_score=11
	elif list_count <50000:
		list_score=13
	else:
		list_score=15
	return list_score


def calc_follower_count(folls):
	if folls<20:
		foll_score=3
	elif folls<100:
		foll_score=4
	elif folls<500:
		foll_score=5
	elif folls<1000:
		foll_score=6
	elif folls<10000:
		foll_score=7
	elif folls<100000:
		foll_score=8
	elif folls<1000000:
		foll_score=8
	else: 
		foll_score=10
	return foll_score

def calc_friends(folls,friends):
	q1=folls*1.0
	q2=friends*1.0
	if folls<20:
		ab=1.0
	elif folls<100:
		ab=3.0
	elif folls<500:
		ab=5.0
	elif folls<1000:
		ab=7.0
	elif folls<10000:
		ab=9.0
	elif folls<100000:
		ab=11.0
	elif folls<1000000:
		ab=13.0
	else: 
		ab=15.0
	friends_score = (q2/q1)*ab
	if friends_score>15:
		friends_score=15
	return friends_score

def calc_tweet_ratio(i1,tweets):				
	if tweets<10:
		aa=2.0
	elif tweets<100:
		aa=4.0
	elif tweets<500:
		aa=8.0
	elif tweets<1000:
		aa=12.0
	elif tweets<50000:
		aa=16.0
	elif tweets<100000:
		aa=20.0
	elif tweets<500000:
		aa=24.0
	elif tweets<1000000:
		aa=28.0
	else:
		aa=30.0
	
	a1=i1*1.0
	a2=tweets*1.0
	ratio_score=(a1/a2)*aa
	if ratio_score>30:
		ratio_score=30
	return ratio_score


def calc_top_followers(l,i):
	k=1
	while k<i:
		j=k-1
		key=l[k]
		while j>=0 and l[j]<key:
			l[j+1]=l[j]
			j=j-1
		l[j+1]=key
		k=k+1	
	total=0
	k=0
	while k<i and k<5:
		total=total+l[k]
		k=k+1		
	if total<10:
		follower_score=1
	elif total<100:
		follower_score=4
	elif total<500:
		follower_score=8
	elif total<1000:
		follower_score=12
	elif total<50000:
		follower_score=16
	elif total<100000:
		follower_score=20
	elif total<500000:
		follower_score=24
	elif total<1000000:
		follower_score=28
	else:
		follower_score=30
	return follower_score	

def calc_mention(mid,m):
	t=0
	mention_user=0
	u=0
	muser=[]
	if m>0:
		for t in range(0,m):
	
			if mention_user>0:
				flag=0
				for u in range(0,mention_user):
					if muser[u][0] == mid[t]:
						flag=1
						muser[u][1] = muser[u][1]+1 
						break
				if flag == 0:
					muser.append([])
					muser[mention_user].append(mid[t])
					muser[mention_user].append(1)
					mention_user=mention_user+1
			else:
				muser.append([])
				muser[mention_user].append(mid[t])
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
