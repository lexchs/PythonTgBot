from datetime import datetime
from datetime import date
ourday = datetime(2020,1,25,23,59,59)
today = datetime.now()
diff=ourday-today
ydiff=diff.days*-1
hdiff=diff.seconds//3600
mdiff=(diff.seconds%3600)//60
sdiff=(diff.seconds%3600)%60


print(ydiff,hdiff,mdiff,sdiff)