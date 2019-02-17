import os
import time
import sys

a = input("多少分钟：")
a = int(a)
s = "/mnt/c/'Program Files'/'Windows Media Player'/wmplayer.exe"
b = "'D:/code/tomato/a.mp3'"
for i in range(1, a*60+1):
	sys.stdout.write("\r" + "还剩: " + str(a - int(i/60)) + "分钟")
	time.sleep(1)

os.system(s + ' ' + b)
print('\r')
