import datetime
import time
while True:
    time.sleep(1)
    x = datetime.datetime.now()
    x = x.strftime("%S")
    if x == "30":
        print("It is 30 seconds into the minute")
    else:
        pass
        
