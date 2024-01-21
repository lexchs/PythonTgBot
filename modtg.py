def ourdate():
	from datetime import datetime
	from datetime import date
	ourday = datetime(2020,1,25,23,59,59)
	today = datetime.now()
	diff=today-ourday
	ydiff=diff.days
	hdiff=diff.seconds//3600
	mdiff=(diff.seconds%3600)//60
	sdiff=(diff.seconds%3600)%60
	x=f"Мы вместе: {ydiff}-дней, {hdiff}-часов,{mdiff}-минут, {sdiff}-секунд!❤"
	return x
print(ourdate())
