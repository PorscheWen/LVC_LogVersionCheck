import os
import sys
import time
import re
sys.path.append("../CommonFiles")
# ## from testScript import TestCase
from testScript import testCase1_Solid_Flow
from PythonScript import CheckProcessStatusV2

def checkTasks():
    TaskList = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(TaskList)):
        TaskList[i]=[q for q in TaskList[i].split(' ') if q != ''][:1]
    return TaskList

class ProcessSnapShot():
    def __init__(self):
        self.a=checkTasks()
    def killRedundant(self):
        self.b=checkTasks()
        for i in range(len(self.b)):
            if not (self.b[i] in self.a):
                os.system("taskkill /t /f /im "+ str(self.b[i][0]) )
                print "Python killed", self.b[i]

def StageStart(sn):
    #Stage Start
    path = r"C:\work\VM_Require_Tools\VM_Info_Sync\VM_Info_Sync.py"
    os.popen("python %s -sn '%s'" %(path, sn))

def StageFinish(t1,t2,t3,sn,tr,se,aip,bcp,fu,fp,mt):
    #Stage Finish
    cmd = 'python "{path}" -t1 "{t1}" -t2 "{t2}" -t3 "{t3}" -sn "{sn}" -tr "{tr}" -se "{se}" -aip "{aip}" -bcp "{bcp}" -fu "{fu}" -fp "{fp}" -mt "{mt}"'.format(
    path= r"C:\work\XenTools\VM_Require_Tools\FogBugzAPITest\Report_Bug_Proxy.py",
    t1=t1,
    t2=t2,
    t3=t3,
    sn=sn,
    tr=tr,
    se=se,
    aip=aip,
    bcp=bcp,
    fu=fu,
    fp=fp,
    mt=mt)
    #print cmd
    os.popen(cmd)
    

def ReturnTestFinish(pathReserve=""):
    pathFinishProcess = r"C:\Work\XenTools\Test_Finish_Process\Test_Process_Process.py"
    if pathReserve != "":
        pathReserve = " -fp " + pathReserve
    os.popen("call python " + pathFinishProcess + pathReserve)

def main():    
    #TestInfo
    t1 = "Solid"
    t2 = "Flow"
    t3 = "Case1"
    sn =""
    tr =""
    se ="Please Check StageResult.txt.\n"+ r"C:\WorkingFolder\testCase\StageResult.txt"
    aip =""
    bcp =""
    fu ="porsche"
    fp ="wpc84200"
    mt = "Fill"

    #Stage1
    print "Stage1"
    sn = "GetLogVersion" #StageName
    StageStart(sn)
    tr, strLogVersion = testCase1_Solid_Flow.Stage1_GetLogVersion()
    StageFinish(t1,t2,t3,sn,tr,se,aip,bcp,fu,fp,mt)
    print "Function (%s): %s !" % ("Stage1_GetLogVersion",tr)
    if "Failed" in tr:
        return
    
    #Stage2
    print "Stage2"
    sn = "GetInstallVersion" #StageName
    StageStart(sn)
    tr, strInstalVersion = testCase1_Solid_Flow.Stage2_GetInstallMDX3DVersion()
    StageFinish(t1,t2,t3,sn,tr,se,aip,bcp,fu,fp,mt)
    print "Function (%s): %s !" % ("Stage2_CheckAnalysisResult",tr)
    if "Failed" in tr:
        return
    
    #Stage3
    print "Stage3"
    sn = "CheckVersionMatched" #StageName
    StageStart(sn)
    tr = testCase1_Solid_Flow.Stage3_CheckLogAndInstallVersionMatched(strLogVersion, strInstalVersion)
    StageFinish(t1,t2,t3,sn,tr,se,aip,bcp,fu,fp,mt)
    print "Function (%s): %s !" % ("Stage3_CheckLogAndInstallVersionMatched",tr)
    
    
  
if __name__ == '__main__':
    
    #For Test Mode Setting(Test or not, 1:Yes, 0:No)
    print "TestMode"
    TestMode = 1
    
    #Record start time
    print "StartTime"
    StartTime = time.time()
    
    #Create ini file(record crash status) and start new thread to check crash or not
    print "CheckProcessStatusV2"  
    fileMDXdata = open(r'MDXdata.ini', 'w')
    CheckProcessStatusV2.CreateMDXdata()
    CheckProcessStatusV2.StartToCallmyCheckCrashFunction()

    #Record all processes in test duration.    
    print "Record all processes in test duration"    
    if TestMode == 0:
        processes = ProcessSnapShot()

    #Start Test
    print "main" 
    main()
    
    #OverWrite MDXData content to "Done" (2017/04/01 Bowen new)
    print"OverWrite MDXData"
    CheckProcessStatusV2.OverWriteMDXData()

    # Kill all processes(Used by this test)
    print"Kill all processes"
    if TestMode == 0:
        processes.killRedundant()
    
    #Record end time and cal. totoal time
    print"Record end time"
    EndTime = time.time()
    CheckProcessStatusV2.RunScriptTime(StartTime,EndTime)

    # Test Finish
    # Copy test files to C:\work\LOG\TestID
    if TestMode == 0:
        ReturnTestFinish("C:\\WorkingFolder\\testCase")
