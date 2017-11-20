import os, re

def LogSomeMessage(backupInfo_Address, ReadVersion_Py, word):
    # Read the DailyBuild version   
    if "Py3" in ReadVersion_Py: 
        from ReadMoldexVersion_py34 import AutoReadMoldexVersion
        version = AutoReadMoldexVersion()
    elif "Py2" in ReadVersion_Py: 
        from ReadMoldexVersion_py27 import AutoReadMoldexVersion
        version = AutoReadMoldexVersion()
    
    # Check if the backupInfo_Address path exist
    if not os.path.exists(backupInfo_Address):
        return("backUp_Inforation.ini path setting Error !!")      
        
    # Read the setting infomation from backupInfo_Address
    with open(backupInfo_Address, "r") as backUpInfoFile :
        backUpInfo = backUpInfoFile.read()
    [ProductLine, TestCaseModule, testCaseName, BackupTargetPath] = ["ProductLine", "TestCaseModule", "testCaseName", "BackupTargetPath"]
    settingInfo_List = []
    for parameter in [ProductLine, TestCaseModule, testCaseName, BackupTargetPath]:
        patten = r"{}.+\".+\"\n".format( parameter)
        parameterLine = re.search(patten, backUpInfo).group()
        parameter = re.search("\".+\"", parameterLine).group().replace( "\"", "") 
        settingInfo_List.append(parameter)
    [ProductLine, TestCaseModule, testCaseName, BackupTargetPath] = settingInfo_List     
    
    # Build the DailyBuild folder under TestCase Module folder
    targetPath_parent = r"{}\{}\{}\{}\{}".format(BackupTargetPath, ProductLine,TestCaseModule, version, testCaseName)
    if not os.path.exists(targetPath_parent):
        os.makedirs( targetPath_parent)     
    
    logFilePath = targetPath_parent + r"\{}_Log.txt".format(testCaseName)
    
    # Record time
    from datetime import datetime
    timeFormat = "[%Y-%m-%d %H:%M:%S]"
    nowTime = datetime.now().strftime(timeFormat) 
    
    # Writing something
    with open(logFilePath, "a") as logFile :
        backUpInfo = logFile.write("{}  {}\n".format(nowTime, word))  
    
    return("Log succesed")
    

if __name__ == '__main__':

    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini" 
    ReadVersion_Py = "Py2.7"  # Py3.4 
    word = "step 4 - end."
    
    message = LogSomeMessage(backupInfo_Address, ReadVersion_Py, word)    
    print(message)