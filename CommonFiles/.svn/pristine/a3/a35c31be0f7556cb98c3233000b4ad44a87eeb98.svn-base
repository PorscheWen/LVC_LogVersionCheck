import os
from shutil import copy2
from string import lstrip, rstrip
from PythonScript import TestFile_BackUp_FEA

def LunchMDX3DI2(mdxProjFolder,mdxProjName,RunNum):
    MDX3DI2Path = "C:\\Moldex3D\\R16\\Bin\\MDX3DI2.exe"
    Passphrase = "R11_autotest"
    InputI2 = "C:\\Moldex3D\\R16\\*" + mdxProjFolder + "*" + mdxProjName + "*" + "0" + "*" + RunNum + "*C:\\ProgramData\\Moldex3D"
    Arg = [Passphrase , InputI2]
    try:
        ReturnMDX3DI2 = os.popen(MDX3DI2Path + " " + Arg[0] + " " + Arg[1])
        Result = "Successful"
    except:
        print (">>> LunchMDX3DI2 Failed!")
        Result = "Failed"
    # if (ReturnMDX3DI2.read()) != 0:
        # Result = "Successful"
    # else:
        # Result = "Failed"
    return Result

def CoverCMIFile(mdxProjName,RunNum,cmiName):
    testModelPath = "C:\\WorkingFolder\\testCase\\testModel\\%s"
    mdxProjFolder = testModelPath % mdxProjName
    SubPath = "\\Analysis\\Run0%s\\%s0%s.cmi"
    FEAUIOutputProj = (testModelPath + SubPath) % (mdxProjName,RunNum,mdxProjName,RunNum)
    FEAUIOutputPart = (testModelPath + cmiName) % (mdxProjName)
    try:
        Result = copy2(FEAUIOutputPart,FEAUIOutputProj)
        print (">>> Copy cmi file to project folder successful")
    except:
        print (">>> Copy cmi file to project folder fail")
        Result = "Failed"
    return Result

def RebuildOutputFolder(Folder):
    Folder = Folder.rstrip("\\")
    removeOutputFolder = os.system("rmdir /s /q \"%s\"" % Folder)
    try:
        if removeOutputFolder == 0 :
            print (">>> Remove folder sucessfully!")
            makeOutputFolder = os.popen("mkdir \"%s\"" % Folder)
        else:
            print (">>> Folder not exist, making folder")
            makeOutputFolder = os.popen("mkdir \"%s\"" % Folder)
        Result = makeOutputFolder
    except:
        Result = "Failed"
    return Result

def checkFEALog(site):

    if os.path.exists(site) == True:
        f = open(site)
        file_data = f.read()
        f.close()
        checkEndProg = 'End Program' in file_data
        if checkEndProg == True:
            print (">>> Check \"End Program\" Normally!")
        else:
            print (">>> Check \"End Program\" Failed!")
            Result = "Failed"
            return Result
        checkError = 'ERROR' in file_data
        if checkError == False:
            print (">>> Check no \"Error\"!")
        else:
            print (">>> Check \"Error\" Failed!")
            Result = "Failed"
            return Result
        checkWarning = 'WARNING' in file_data
        if checkWarning == False:
            print (">>> Check no \"Warning!\"")
        else:
            print (">>> Check \"Warning!\" Failed!")
            Result = "Failed"
            return Result
    else:
        Result = "Failed"
    Result = "Successful"
    return Result

def checkFEAOutputExists(FEAOutPutFolder,files):
    #Double Check FEA Output files no. = check list no. + 1(log file )
    checkclrFEAOutPutFolder = os.listdir(FEAOutPutFolder)
    if len(checkclrFEAOutPutFolder) == len(files) + 1:
        print (">>> FEA Output files match checking files list")
    else:
        print (">>> FEA Output files don't match checking files")
        Result = "Failed"
        return Result
    #Check FEA Output file exists one by one
    for i in range(len(files)):
        files[i] = FEAOutPutFolder + files[i]
        if os.path.exists(files[i]) == True:
            # print (">>> Check output file exist!")
            filesize = os.path.getsize(files[i])
            if filesize >= 4*1024:
                pass
                # print (">>> Filesize is reasonable")
            else:
                if files[i] == (FEAOutPutFolder + "Moldex3DtoANSYS.xml") or files[i] == (FEAOutPutFolder + "Moldex3DtoANSYS"):
                    print (">>> It's an extension!")
                else:
                    print (">>> Filesize is unreasonable")
                    Result = "Failed"
                    return Result
        else:
            print (">>> Output file %s not exist!" % files[i])
            Result = "Failed"
            return Result
    print (">>> Check files exist and size is reasonable!")
    Result = "Successful"
    if Result == "Successful":
        BackupOutputMesh(FEAOutPutFolder)
    return Result

def BackupOutputMesh(FEAOutputDir,):
	
    backupInfo_Template = r"C:\WorkingFolder\CommonFiles\PythonScript\FEA_Backup_template.ini" 
    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini" 
    temp = os.listdir(r"C:\WorkingFolder\testCase\testScript")
    for i in temp:
        if "Test_" in i and ".pyc" not in i:
            TypeFolder = i.rstrip(".py")
            TypeFolder = TypeFolder.lstrip("Test")
            if "3DMap" not in TypeFolder:
                TypeFolder = TypeFolder.translate(None,"0123456789_")
            else:
                TypeFolder = TypeFolder.translate(None,"17_")
            """
            if "Nastran" in i or "OptiStruct" in i:
                print (">>> Nastran/OpitStruct do not backup mesh files")
                return
            """
    with open(backupInfo_Template, mode="r") as tempfile:
        temp = tempfile.readlines()
        temp[3] = "# testCaseName: \"%s\"\n" % TypeFolder
        temp[4] = "sourceParentPath: \"%s\"\n" % FEAOutputDir[:-1]
        temp[10] = "%s\n" % FEAOutputDir[:-1]
    with open(backupInfo_Address, mode="w") as inifile:
        inifile.writelines(temp)

    ReadVersion_Py = "Py2.7" # Py2.7
    backUplabel = "Stage_002"
    xFileNameLabel = "" # xFileName1    
    backupPoint = TestFile_BackUp_FEA.BackupTestingResult(backupInfo_Address, ReadVersion_Py, backUplabel, xFileNameLabel)    
    print(backupPoint)
    """
    print (">>> start Backup FEA Output Mesh Files...")
    NetPath = r"\\192.168.3.229\QAData\QAPublicData\AutoTestBackup\FEA_Output\%s\%s"
    # Looking for DailyBuild Version
    with open(r"C:\Moldex3D\R16\Moldex3D.ver", "r") as file :
        VerData = file.readlines()
    Ver = VerData[1].split(" ")
    # Ver[3] = Ver[3].lstrip("(")
    # Ver[3] = Ver[3].rstrip(")\n")
    Ver[3] = Ver[3].translate(None,"()\n")    
    BuildFolder = Ver[1]+Ver[3]
    # Looking for the Type of Test
    temp = os.listdir(r"C:\WorkingFolder\testCase\testScript")
    for i in temp:
        if "Test_" in i and ".pyc" not in i:
            TypeFolder = i.rstrip(".py")
            TypeFolder = TypeFolder.lstrip("Test")
            if "3DMap" not in TypeFolder:
                TypeFolder = TypeFolder.translate(None,"0123456789_")
            else:
                TypeFolder = TypeFolder.translate(None,"17_")
            if "Nastran" in i or "OptiStruct" in i:
                print (">>> Nastran/OpitStruct do not backup mesh files")
                return

    DistinationFolder = NetPath % (BuildFolder,TypeFolder)
    RebuildOutputFolder(DistinationFolder)
    # FEAOutPutFolder = r"D:\Desktop\temp\Ori\Run02"
    List = os.listdir(FEAOutputDir)
    for i in List:
        if "Moldex3DtoANSYS" not in i:
            FileDir = FEAOutputDir + i
            BackupDir = DistinationFolder + "\\" + i
            os.popen("copy /y \"%s\" \"%s\"" % (FileDir,BackupDir))
        else:
            pass
    """