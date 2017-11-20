import os
import sys
import time
import subprocess
import ConfigParser
import TestFile_BackUp
import writexl
from subprocess import PIPE
from time import sleep
sys.dont_write_bytecode = True


class ProcessSnapShot:

    def __init__(self):
        print "ProcessSnapShot"
        self.a = checkTasks()

    def killRedundant(self):
        print "killRedundant"
        self.b = checkTasks()
        for i in range(len(self.b)):
            if not (self.b[i] in self.a):
                os.system("taskkill /t /f /im " + str(self.b[i][0]))
                print "Python killed", self.b[i]


def checkTasks():
    TaskList = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(TaskList)):
        TaskList[i] = [q for q in TaskList[i].split(' ') if q != ''][:1]
    return TaskList


def ReturnTestFinish(pathReserve=""):
    pathFinishProcess = r"C:\Work\XenTools\Test_Finish_Process\Test_Process_Process.py"
    if pathReserve != "":
        pathReserve = " -fp " + pathReserve
    os.popen("call python " + pathFinishProcess + pathReserve)


class DetectCrash:

    def __init__(self, mode):
        self.cScriptPath = r"C:\WorkingFolder\CommonFiles\PythonScript_SAM\DetectCrash.py"
        self.mode = mode
        self.SubPro = subprocess.Popen(
            ["python", self.cScriptPath, self.mode], shell=False, stdout=PIPE, stderr=PIPE)

    def TerminateDetect(self):
        # Result = self.SubPro.communicate()
        self.SubPro.terminate()
        self.SubPro.wait()
        Result = list(self.SubPro.communicate())[0].split("\r")
        if "Kill WerFault.exe" in Result:
            return "Happened"
        else:
            return "Pass"


class Timer:

    def __init__(self):
        self.t = [time.clock()]
        self.tpn = ["Test Start"]
        self.count = 1

    def Add_Time_Point(self, TimePointName):
        self.count += 1
        self.t.append(time.clock())
        self.tpn.append(TimePointName)
        print ("Add Time Point: %s" % TimePointName)
        # print self.count

    def Output_TimeLog(self):
        self.path = r"C:\WorkingFolder\testCase\testModel\TimeLog_%s.txt" % Get_ProjName()
        # print self.path
        with open(self.path, "w") as file:
            data = []
            for i in xrange(self.count):
                fmt = "{tpn:<30}: {t:>6.2f} sec\n"
                data.append(fmt.format(tpn=self.tpn[i], t=self.t[i]))
            file.writelines(data)


def IniInfo_to_TxtInfo(isMCM=False):
    TestInfo = ConfigParser.ConfigParser()
    TestInfo.optionxform = str
    if isMCM:
        TestInfo.read(r"C:\WorkingFolder\testCase\testModel\TestCaseInfo%s.ini" % isMCM)
    else:
        TestInfo.read(r"C:\WorkingFolder\testCase\testModel\TestCaseInfo.ini")
    total_section = TestInfo.sections()
    for sSection in total_section:
        with open(r"C:\WorkingFolder\testCase\testModel\%s.txt" % sSection, "w") as file:
            for i in TestInfo.items(sSection):
                file.write(i[1] + "\n")


def Get_ProjName():
    with open(r"C:\WorkingFolder\testCase\testModel" + r"\ProjectInfo.txt", "r") as PjInfo:
        sMDXPjName = PjInfo.read().split("\n")[1]
    return sMDXPjName


class LounchBatchRun:

    def __init__(self):
        print "Create Batch Run MSPFile"
        # Creat msp file for running bjs(Batch Run)
        # check and create folder
        chkPath = r"C:\work"
        if not os.path.isdir(chkPath):
            os.makedirs(chkPath)
        # *.msp file content
        mspContent = """<?xml version="1.0"?>\n<MDX_SCRIPT_DATA>\n<SCRIPT>\n#RUNBATCH\n#EXIT\n</SCRIPT>\n</MDX_SCRIPT_DATA>"""
        # write file
        with open(os.path.join(chkpath, "RunMDXProj.msp"), "w") as mspFile:
            mspFile.write(mspContent)
        self.mspPath = r"C:\work\RunMDXProj.msp"

    def Solving(self):
        pjexePath = r"C:\Moldex3D\R16.0\Bin\MDXProject.exe"
        with open(r"C:\WorkingFolder\testCase\testModel\ProjectInfo.txt", "r") as file:
            data = file.read().split("\n")
        pjType = {"2D": "m2j",
                  "3DeDN": "mvj",
                  "3DSolid": "m3j"}.get(data[2])
        mpjPath = r"C:\WorkingFolder\testCase\testModel\{pjName}.{pjextName}".format(
            pjName=data[1], pjextName=pjType)
        cmd = "\"%s\" \"%s\" \"%s\"" % (pjexePath, mpjPath, self.mspPath)
        os.popen(cmd)

    def Check_mLog(self):
        pass

class Template:
    IniTemplate = r"""[Setting]
# ProductLine: "Moldex3D"
# TestCaseModule: "Sample"
# testCaseName: "{1}"
# sourceParentPath: "C:\WorkingFolder\testCase\testModel"
# BackupTargetPath: "\\172.16.0.31\QA3Test\AutoTest_Backup"
[/Setting]

[Stats]
C:\WorkingFolder\testCase\testModel\Stats_{0}
[/Stats]

[Project]
C:\WorkingFolder\testCase\testModel\{0}
[/Project]

[ProCmx]
{2}
[/ProCmx]

[TimeLog]
C:\WorkingFolder\testCase\testModel\TimeLog_{0}.txt
[/TimeLog]

[TCLogs_{0}]
{3}
[/TCLogs_{0}]
"""
    def __init__(self, sProjName):
        self.sProjName = sProjName

    def __call__(self, sCaseLabel, lstTCLogs, lstOptionFiles=None):
        if lstOptionFiles:
            return self.IniTemplate.format(self.sProjName, sCaseLabel, "\n".join(lstOptionFiles), "\n".join(lstTCLogs))
        else:
            return self.IniTemplate.format(self.sProjName, sCaseLabel, "", "\n".join(lstTCLogs))


class BackUp:
    lstFiles = []
    lstLogs = []
    testModelPath = r"C:\WorkingFolder\testCase\testModel"

    def __init__(self):
        self.sMDXPjName = Get_ProjName()
        self.initstr = Template(self.sMDXPjName)

    def BackUp_Start(self, NameTag):
        self.update_Ini(NameTag)
        self.excute_BackUp(NameTag)

    def update_Ini(self, NameTag):
        self.fInitpath = "\\".join([self.testModelPath, "backUp_Information.ini"])
        with open(self.fInitpath, "w") as fInit:
            fInit.write(self.initstr(NameTag, self.lstLogs, self.lstFiles))

    def excute_BackUp(self, backUplabel):
        TestFile_BackUp.BackupTestingResult(self.fInitpath, "Py2.7", backUplabel, "")

    def Collect_PRO(self):
        dirpath = "\\".join([self.testModelPath, self.sMDXPjName, "Process"])
        if os.path.isdir(dirpath):
            files = os.listdir(dirpath)
            for f in files:
                if ".pro" in f:
                    self.lstFiles.append("\\".join([self.testModelPath, f]))
                    os.popen("copy /y \"%s\" \"%s\"" % ("\\".join([dirpath, f]), self.testModelPath))

    def Collect_CMX(self):
        dirpath = "\\".join([self.testModelPath, self.sMDXPjName, "Analysis"])
        if os.path.isdir(dirpath):
            dirs = os.listdir(dirpath)
            for d in dirs:
                files = os.listdir("\\".join([dirpath, d]))
                for f in files:
                    if ".cmx" in f:
                        self.lstFiles.append("\\".join([self.testModelPath, f]))
                        os.popen("copy /y \"%s\" \"%s\"" % ("\\".join([dirpath, d, f]), self.testModelPath))

    def Collect_TCLog(self):
        files = os.listdir(self.testModelPath)
        for f in files:
            if ".mht" in f:
                self.lstLogs.append("\\".join([self.testModelPath, f]))

def BackUp_to_Net(tr):
    BU = BackUp()
    BU.Collect_TCLog()
    BU.BackUp_Start("TimeLog")
    BU.BackUp_Start("TCLogs_" + Get_ProjName())
    if tr == "Successful":
        BU.Collect_PRO()
        BU.Collect_CMX()
        BU.BackUp_Start("Project")
        BU.BackUp_Start("Stats")
        BU.BackUp_Start("ProCmx")

def BackUp_Excel(tr):
    if tr == "Successful":
        fInitpath = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini"
        TestFile_BackUp.BackupTestingResult(fInitpath, "Py2.7", "Excel", "")

def Modify_MDXReg():
    RegPath = r"C:\WorkingFolder\CommonFiles\CloseStartupPage.reg"
    os.popen("reg import \"%s\"" % RegPath)


if __name__ == "__main__":
    pass