import os
import sys
import time
import Queue
import inspect
import logging
import threading
import ConfigParser
import TestFile_BackUp
from shutil import copy2, rmtree


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


class Timer:

    def __init__(self):
        self.t = [time.clock()]
        self.tpn = ["Test Start"]
        self.count = 1

    def Add_Time_Point(self, TimePointName):
        self.count += 1
        self.t.append(time.clock())
        self.tpn.append(TimePointName)
        logging.debug(">>> Add Time Point: %s" % TimePointName)
        # print self.count

    def Output_TimeLog(self):
        self.path = r".\testModel\TimeLog.txt"  # % Get_ProjName()
        # print self.path
        with open(self.path, "a") as file:
            data = []
            for i in xrange(self.count):
                fmt = "{tpn:<30}: {t:>6.2f} sec\n"
                data.append(fmt.format(tpn=self.tpn[i], t=self.t[i]))
            file.writelines(data)
            file.close()


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
    sResult = ">>> Function ({}): {} !\n".format(FunctionName, sLog)
    logging.info(sResult)
    return sLog


class Error(Exception):

    def __init__(self, msg=""):
        self.message = msg
        q.put(2, block=True, timeout=None)
        # Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__


class LogNotFoundError(Error):
    def __init__(self, path="UnknownPath"):
        Error.__init__(self, ">>> Log file Not Found @%s" % path)


class AbortError(Error):
    def __init__(self):
        Error.__init__(self, ">>> Not End Program Normaly")


class LogErrorOccurred(Error):
    def __init__(self):
        Error.__init__(self, ">>> Found ERROR in Log File")


class LogWarningOccurred(Error):
    def __init__(self):
        Error.__init__(self, ">>> Found WARNING in Log File")


class FilesQuantityError(Error):
    def __init__(self):
        Error.__init__(
            self, ">>> FEA Output files quantity don't equal to checking files")


class FileSizeError(Error):
    def __init__(self, file):
        Error.__init__(self, ">>> Filesize of %s is unreasonable" % file)


class FilesNameError(Error):
    def __init__(self, file):
        Error.__init__(self, ">>> Output file %s not exist!" % file)


class FEAOutput:

    def __init__(self, initTag):
        TestInfo = ConfigParser.ConfigParser()
        TestInfo.optionxform = str
        TestInfo.read(r"..\CommonFiles\PythonScript\FEATestCaseInfo.ini")
        self.projName = TestInfo._sections[initTag]["ProjName"]
        self.runNum = int(TestInfo._sections[initTag]["RunNum"])
        self.files = TestInfo._sections[initTag]["files"].split("\n")
        self.files.pop(0)

    def rebuild_output_folder(self):
        try:
            path = r".\testModel\{}\Report\Run{:02d}".format(self.projName, self.runNum)
            if os.path.exists(path):
                rmtree(path, ignore_errors=False, onerror=None)
                logging.info(">>> Remove folder sucessfully!")
            else:
                logging.info(">>> Folder not exist, making folder")
            os.mkdir(path)
            q.put(0, block=True, timeout=None)
        except Exception as e:
            logging.debug(e)
            q.put(2, block=True, timeout=None)

    def replace_cmi_file(self, argv=r"\{0}{1:02d}.cmi"):
        try:
            path = r".\testModel"
            SubPath = r"\{0}\Analysis\Run{1:02d}\{0}{1:02d}.cmi"
            srcCMI = (path + argv).format(self.projName, self.runNum)
            dstCMI = (path + SubPath).format(self.projName, self.runNum)
            copy2(srcCMI, dstCMI)
            logging.info(">>> Copy cmi file to project folder successful")
            q.put(0, block=True, timeout=None)
        except Exception as e:
            logging.debug(e)
            q.put(2, block=True, timeout=None)

    def launch_MDX3DI2(self):
        try:
            mdx3DI2Path = r"C:\Moldex3D\R16\Bin\MDX3DI2.exe"
            passPhrase = "R11_autotest"
            mdxProjFolder = r"C:\WorkingFolder\testCase\testModel\{}".format(self.projName)
            cmd = "{} {} C:\\Moldex3D\\R16\\*{}*{}*0*{}*C:\\ProgramData\\Moldex3D".format(
                mdx3DI2Path, passPhrase, mdxProjFolder, self.projName, self.runNum)
            os.popen(cmd)
            self.check_fea_log()
            q.put(0, block=True, timeout=None)
        except (LogNotFoundError, AbortError, LogErrorOccurred, LogWarningOccurred) as e:
            logging.info(e)
        except Exception as e:
            logging.debug(e)

    def check_fea_log(self):
        path = r".\testModel\{0}\Report\Run{1:02d}\{0}{1:02d}_FEA.log".format(self.projName, self.runNum)
        if not os.path.exists(path):
            raise LogNotFoundError(path)
        with open(path, "r") as f:
            file_data = f.read()
        isEndNormally = 'End Program' in file_data
        if isEndNormally:
            logging.info(">>> Check \"End Program\" Normally!")
        else:
            raise AbortError
        isNoError = 'ERROR' not in file_data
        if isNoError:
            logging.info(">>> Check no \"Error\"!")
        else:
            raise LogErrorOccurred
        isNoWarning = 'WARNING' not in file_data
        if isNoWarning:
            logging.info(">>> Check no \"Warning\"!")
        else:
            raise LogWarningOccurred

    def check_output_files(self):
        try:
            path = ".\\testModel\\{0}\\Report\\Run{1:02d}\\".format(self.projName, self.runNum)
            checkclrFEAOutPutFolder = os.listdir(path)
            if len(checkclrFEAOutPutFolder) == len(self.files) + 1:
                logging.info(">>> FEA Output files quantity equal to checking files list")
            else:
                raise FilesQuantityError
            # Check FEA Output file exists one by one
            for i in range(len(self.files)):
                self.files[i] = path + self.files[i]
                if os.path.exists(self.files[i]):
                    fileSize = os.path.getsize(self.files[i])
                    if fileSize >= 4 * 1024:
                        pass
                        # print (">>> Filesize is reasonable")
                    else:
                        if self.files[i] == (path + "Moldex3DtoANSYS.xml") or self.files[i] == (path + "Moldex3DtoANSYS"):
                            logging.info(">>> It's an extension!")
                        else:
                            raise FileSizeError(self.files[i])
                else:
                    raise FilesNameError(self.files[i])
            logging.info(">>> Check files exist and size is reasonable!")
            q.put(0, block=True, timeout=None)
        except (FilesQuantityError, FilesNameError, FileSizeError) as e:
            logging.info(e)
        except Exception as e:
            logging.debug(e)

q = Queue.Queue(maxsize=1)


class PyCIs:

    def __init__(self, sClassName, initArgv=None):
        self.sClassName = sClassName
        if initArgv:
            self.TestClass = {
                "FEAOutput": FEAOutput
            }.get(sClassName)(initArgv)
        else:
            self.TestClass = {
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
        self.thd.join(0)

    def Run_Wait(self, tLimit=0):
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
                logging.info("===> {to:^28} <===".format(to="Time Out Failed..."))
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


class Template:

    def __init__(self):
        self.iniSettingTemp = r"""
[Setting]
# ProductLine: "Moldex3D"
# TestCaseModule: "FEAOutput"
# testCaseName: "{}"
# sourceParentPath: r"C:\WorkingFolder\"
# BackupTargetPath: "\\172.16.0.31\QA3Test\AutoTest_Backup"
[/Setting]
"""
        self.iniFEAMeshTemp = r"""
[FEAMesh]
.\testModel\{}\Report\Run{:02d}
[/FEAMesh]
"""
        self.iniTimeLogTemp = r"""
[TimeLog]
.\testModel\TimeLog.txt
[/TimeLog]"""


def BackUp(sT1="", sT2="", sT3="", sSN="", sTR="", sMT=""):
    tmp = Template()
    TestInfo = ConfigParser.ConfigParser()
    TestInfo.optionxform = str
    TestInfo.read(r"..\CommonFiles\PythonScript\FEATestCaseInfo.ini")
    initTag = "_".join([sT1, sT2, sT3])
    runNum = int(TestInfo._sections[initTag]["RunNum"])
    projName = TestInfo._sections[initTag]["ProjName"]
    tmp.iniSettingTemp = tmp.iniSettingTemp.format(initTag)
    tmp.iniFEAMeshTemp = tmp.iniFEAMeshTemp.format(projName, runNum)
    tmp.iniTimeLogTemp = tmp.iniTimeLogTemp
    backupInfoPath = r".\testModel\backupInfo.ini"
    with open(backupInfoPath, "w") as fini:
        fini.write(tmp.iniSettingTemp)
        fini.write(tmp.iniFEAMeshTemp)
        fini.write(tmp.iniTimeLogTemp)
    backupPoint = TestFile_BackUp.BackupTestingResult(backupInfoPath, "Py2.7", "TimeLog", "")
    logging.info(backupPoint)
    if sTR == "Successful":
        backupPoint = TestFile_BackUp.BackupTestingResult(backupInfoPath, "Py2.7", "FEAMesh", "")


if __name__ == '__main__':
    pass
