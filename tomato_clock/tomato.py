import os
import time
import sys

a = input("多少分钟：")
a = int(a)

for i in range(a*60+1):
	time.sleep(1)
	sys.stdout.write("\r" + "还剩: " + str(a - int(i/60)) + "分钟")

os.system('thatgirl.flac')