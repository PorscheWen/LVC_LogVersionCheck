import sys
import time
sys.dont_write_bytecode = True

class Timer():

    def __init__(self):
        self.t = [time.clock()]
        self.tpn = ["Test Start"]
        self.count = 1

    def Add_Time_Point(self, TimePointName):
        self.count += 1
        self.t.append(time.clock())
        self.tpn.append(TimePointName)
        print ("Add Time Point: %s" % TimePointName)
        #print self.count

    def Output_TimeLog(self):
        self.path = r"C:\WorkingFolder\testCase\TimeLog.txt"
        print self.path
        with open(self.path,"w") as file:
            data = []
            for i in xrange(self.count):
                fmt = "{tpn:<30}: {t:>6.2f} sec\n"
                #data.append("%s: %.2f sec\n" % (self.tpn[i], self.t[i]))
                # tpn=self.tpn[i]
                # t=self.t[i]
                
                data.append(fmt.format(tpn=self.tpn[i], t=self.t[i]))
            file.writelines(data)

def main():
    t = Timer()
    a = input(">>> input #")
    print type(a)
    while a != 0:
        t.Add_Time_Point(str(a))
        a = input(">>> input #")
        print type(a)
    t.Output_TimeLog()

if __name__ == "__main__":
    main()