import os
import sys
import time
import inspect
import win32com.client

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
            sLog = "Successful"
        else:
            sLog = "Failed"

    sResult = "Function (%s): %s !" % (FunctionName, sLog)
    print sResult
    return sLog


class InitEnvStage:

    def __init__(self):
        self.itercont = 0
        self.compjsPath = r"C:\WorkingFolder\CommonFiles\SharedComponents_Sample\SharedComponents.pjs"
        self.compjName = "SharedComponents"
        self.UnitName = "PrepareEnvFunction"
        self.TEObj = TEAPIs(self.compjsPath, self.compjName, self.UnitName)
        self.t1 = "Initial Env"
        self.t2 = "Initial Env"
        self.t3 = "Initial Env"
        self.Parameter = ""
        self.tLimit = 0

    def Stage_001_IniteDN(self):
        self.sn = "Stage_000_IniteDN"
        self.mt = "Initial Env eDN"
        self.tLimit = 30

    def Stage_002_InitBLM(self):
        self.sn = "Stage_000_InitBLM"
        self.mt = "Initial Env BLM"
        self.tLimit = 30

    def Stage_003_InitRhino(self):
        self.sn = "Stage_000_InitRhino"
        self.mt = "Initial Env Rhino"
        self.tLimit = 90

    def Stage_004_InitProj(self):
        self.sn = "Stage_000_InitProj"
        self.mt = "Initial Env Proj"
        self.tLimit = 90

    def Info(self):
        return self.t1, self.t2, self.t3, self.sn, self.TEObj.strResult, self.mt

    def __iter__(self):
        return self

    def next(self):
        iterMethod = []
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for m in methods:
            if "Stage_00" in m[0]:
                iterMethod.append(m[1])
        if self.itercont < 4:
            self.itercont += 1
            self.tLimit = 0
            return iterMethod[self.itercont - 1]
        else:
            self.TEObj.TE_Quit()
            os.popen("taskkill /im MDXproject.exe")
            os.popen("taskkill /im Rhino.exe")
            os.popen("taskkill /im MDXDesigner.exe")
            raise StopIteration()


class TEAPIs:

    def __init__(self, pjsPath, pjName, UnitName):
        self.pjName = pjName
        self.UnitName = UnitName
        print "try Dispatch TE"
        self.APP = win32com.client.dynamic.Dispatch(
            "TestExecute.TestExecuteApplication")
        self.APP.Manager.RunMode = 1  # SlientMode
        self.APP.Integration.OpenProjectSuite(pjsPath)
        self.iLogCont = 0
        
    def Run_Routine(self, FunctionName, Parameter=""):
        TEITObj = self.APP.Integration
        self.FunctionName = FunctionName
        if Parameter == "":
            TEITObj.RunRoutine(self.pjName, self.UnitName, FunctionName)
        else:
            TEITObj.RunRoutineEx(self.pjName, self.UnitName,
                                 FunctionName, Parameter)
        self.iLogCont += 1

    def Run_Wait(self, tLimit=0):
        if "Init" not in self.FunctionName:
            tLimit=0
        TEITObj = self.APP.Integration
        if tLimit != 0:
            itc = 0
            while itc != tLimit and TEITObj.IsRunning():
                time.sleep(1)
                itc += 1
                rc = self.detect_Crash()
                if rc:
                    return rc
            if TEITObj.IsRunning():
                TEITObj.Halt("Time Out")
                self.intLastResult = 2
                self.strResult = Return_Status(self.FunctionName, self.intLastResult)
                print "===> {to:^28} <===".format(to="Time Out Failed...")
                self.APP.Integration.ExportResults(r"C:\WorkingFolder\testCase\testModel\TCLog{0:02d}.mht".format(self.iLogCont))
                return self.intLastResult, self.strResult
            else:
                self.get_Result()
        else:
            res = TEITObj.IsRunning
            while res():
                time.sleep(1)
                rc = self.detect_Crash()
                if rc:
                    return rc
            self.get_Result()
        return self.intLastResult, self.strResult

    def get_Result(self):
        TEITObj = self.APP.Integration
        sReadValue = TEITObj.RoutineResult
        self.intLastResult = TEITObj.GetLastResultDescription().Status
        self.strResult = Return_Status(self.FunctionName, self.intLastResult)
        self.APP.Integration.ExportResults(r"C:\WorkingFolder\testCase\testModel\TCLog{0:02d}.mht".format(self.iLogCont))

    def detect_Crash(self):
        TEITObj = self.APP.Integration
        r = os.popen("tasklist").read()
        if "WerFault.exe" in r:
            try:
                TEITObj.Halt("Crash")
            except:
                pass
            self.intLastResult = 2
            self.strResult = Return_Status(
                self.FunctionName, self.intLastResult)
            return self.intLastResult, self.strResult

    def TE_Quit(self):
        print "\nQuit Dispatch TE"
        self.APP.Quit()
        """
        Check "TestExecute.exe" work or not
        This check behavior is for stability of test platform system.
        """
        chkTE = "TestExecute.exe" in os.popen("tasklist").read()
        t = 0
        while chkTE and t <= 30:
            time.sleep(0.2)
            chkTE = "TestExecute.exe" in os.popen("tasklist").read()
            print "TestExecute Exsisting...%s\r" % str(t),
            sys.stdout.flush()
            t += 1

if __name__ == '__main__':
    pass
