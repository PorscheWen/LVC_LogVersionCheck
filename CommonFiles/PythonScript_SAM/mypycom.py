import os
import sys
import time
import inspect
import threading
import Queue
import writexl


sys.dont_write_bytecode = True


def VM_Info_Sync(StageName):
    path = r"C:\work\VM_Require_Tools\VM_Info_Sync\VM_Info_Sync.py"
    os.popen("python %s -sn '%s'" % (path, StageName))


def Report_Bug_Proxy(sT1, sT2, sT3, sSN, sTR, sMT):
    cmd = 'python "{path}" -t1 "{t1}" -t2 "{t2}" -t3 "{t3}" -sn "{sn}" -tr "{tr}" -se "{se}" -aip "{aip}" -bcp "{bcp}" -fu "{fu}" -fp "{fp}" -mt "{mt}"'.format(
        path=r"C:\work\XenTools\VM_Require_Tools\FogBugzAPITest\Report_Bug_Proxy.py",
        t1=sT1,  # dicProxy.get("t1"),
        t2=sT2,  # dicProxy.get("t2"),
        t3=sT3,  # dicProxy.get("t3"),
        sn=sSN,  # dicProxy.get("sn"),
        tr=sTR,  # dicProxy.get("tr"),
        se="",
        aip="",
        bcp="",
        fu="paulsu",
        fp="123456",
        mt=sMT)  # dicProxy.get("mt"))
    os.popen(cmd)


def Return_Status(FunctionName, Status):
    """
    Input: FunctionName, Status
    Output: Routine Status be readable
    """
    if Status == 0:
        sLog = "Successful"
    elif Status == 1:
        sLog = "Warning"
    else:
        if "Init" in FunctionName:
            sLog = "Warning"
        else:
            sLog = "Failed"

    sResult = "Function (%s): %s !" % (FunctionName, sLog)
    print sResult
    return sLog


class FEA_Output:

    def LaunchMDX3DI2(self):
        try:
            print self.LaunchMDX3DI2.__name__
            q.put(0, block=True, timeout=None)
        except:
            q.put(2, block=True, timeout=None)

    def CheckOutputFiles(self):
        try:
            print self.LaunchMDX3DI2.__name__
            q.put(0, block=True, timeout=None)
        except:
            q.put(2, block=True, timeout=None)


class SampleUnify:
    objunify = writexl.UnifyStatsData()

    def Collect_Net_Data(self):
        try:
            os.system("call python " + r"C:\WorkingFolder\CommonFiles\PythonScript_SAM\mydbtool.py")
            root = r"\\172.16.0.31\QA3Test\AutoTest_Backup\Moldex3D\Sample"
            path = r"\\172.16.0.31\QA3Test\AutoTest_Backup\Moldex3D\Sample\{0}\Stats\testModel"
            testModelpath = r"C:\WorkingFolder\testCase\testModel\{0}"
            MDXVer = self.objunify.get_MDXVer()
            BuckUps = os.listdir(root)
            for i in BuckUps:
                if i.translate(None, ".") == "".join(MDXVer).translate(None, " "):
                    dirs = os.listdir(path.format(i))
                    break
            for j in dirs:
                cmdstr = "xcopy /e /i /y \"{0}\\{1}\" \"{2}\"".format(
                    path.format(i), j, testModelpath.format(j))
                r = os.system(cmdstr)
                if r != 0:
                    raise Error
            q.put(0, block=True, timeout=None)
        except:
            q.put(2, block=True, timeout=None)

    def Write_Stats_Data(self):
        try:
            self.objunify.Unifying()
            self.objunify.Save()
            q.put(0, block=True, timeout=None)
        except:
            q.put(2, block=True, timeout=None)


q = Queue.Queue(maxsize=1)


class PyCIs:

    def __init__(self, sClassName):
        self.sClassName = sClassName
        self.TestClass = {
            "FEA_Output": FEA_Output,
            "SampleUnify": SampleUnify
        }.get(sClassName)()

    def Run_Routine(self, sFunctionName, Parameter=""):
        # need to use thread
        self.sFunctionName = sFunctionName
        fn = getattr(self.TestClass, sFunctionName)
        if Parameter == "":
            self.thd = threading.Thread(target=fn)
        else:
            self.thd = threading.Thread(target=fn, kwargs={"argv": Parameter})
        self.thd.start()

    def Run_Wait(self, tLimit=0):
        self.thd.join(0)
        if tLimit != 0:
            itc = 0
            while itc != tLimit and self.thd.isAlive():
                time.sleep(1)
                itc += 1
                rc = self.detect_Crash()
                if rc:
                    return rc
            if self.thd.isAlive():
                self.intLastResult = 2
                print "===> {to:^28} <===".format(to="Time Out Failed...")
            else:
                self.intLastResult = q.get(block=True, timeout=None)
            self.get_Result()

        else:
            while self.thd.isAlive():
                time.sleep(1)
                rc = self.detect_Crash()
                if rc:
                    return rc
            self.intLastResult = q.get(block=True, timeout=None)
            self.get_Result()
        return self.intLastResult, self.strResult

    def get_Result(self):
        self.strResult = Return_Status(self.sFunctionName, self.intLastResult)

    def detect_Crash(self):
        r = os.popen("tasklist").read()
        if "WerFault.exe" in r:
            self.intLastResult = 2
            self.get_Result()
            return self.intLastResult, self.strResult

    def Py_Quit(self):
        print "\nDelete Python TestClass Object"
        del self.TestClass


if __name__ == '__main__':
    pass
