import datetime
import time
date = '2020-12-31'
while True:
    print(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())
    print(str(time.asctime()).split(" ")[0])
    time.sleep(1)
