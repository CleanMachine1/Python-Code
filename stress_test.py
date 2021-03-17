import os
import time
while True:
    os.system("sudo sysbench --num-threads=4 --test=cpu run")
    time.sleep(30)
    