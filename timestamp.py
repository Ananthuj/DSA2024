import time
ts = time.time()
print(ts)

import datetime;
ct = datetime.datetime.now()
print("current time:",ct)
print("timestamp:",ts)

import calendar
import time
gmt = time.gmtime()
print("gmt:",gmt)
ts = calendar.timegm(gmt)
print("timestamp:",ts)
