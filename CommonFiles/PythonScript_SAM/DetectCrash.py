import sys
sys.dont_write_bytecode = True
import os
from time import sleep


def Detect():
	while True:
		sleep(1)
		r = os.popen('tasklist').read().split('\n')
		for i in r:
			if i.split(" ")[0] == "WerFault.exe":		
				# os.popen("taskkill /f /t /im WerFault.exe")
				print ("Kill WerFault.exe")
				PrintFlag = 0
			else:
				PrintFlag = 1
		if PrintFlag == 1:
			print "pass\r",
			sys.stdout.flush()
            
def Monitor():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("No Arg")
        sys.exit(0)
    else:
        if sys.argv[1] == "-D":
            print (">>> Start Detecting Crash Event"),
            sys.stdout.flush()
            Detect()
        elif sys.argv[1] == "-M":
            print (">>> Start Monitor Crash Event"),
            sys.stdout.flush()
            Monitor()