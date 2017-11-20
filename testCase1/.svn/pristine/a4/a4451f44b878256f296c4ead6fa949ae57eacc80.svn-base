import sys
sys.path.append("../../CommonFiles")
from PythonScript import RunMDXProject
from PythonScript import ReadMoldexVersion_py27
from PythonScript import LVC_CheckLogVersion
import _winreg, re
#Fill your project path(.m3j). If yuor file type is not a .m3j, please revise mdxProjM3JPath
mdxProM3JPath = r"C:\WorkingFolder\testCase\testModel\TestCase1_Solid_Flow\TestCase1_Solid_Flow.m3j"



# Get Log Version from single log file ex.160.1.1710.25002
def Stage1_GetLogVersion():
    # Create StageResult.txt to record results by each stage.
    LVC_CheckLogVersion.WriteToResultTxt("Create StageResult.txt", " ......Done")
    mdxProM3JPath = LVC_CheckLogVersion.GetProjectM3JPath()
    # Launch MDX by script
    LVC_CheckLogVersion.WriteToResultTxt("Start to Launch Mold3D Analysis", " ......Done")
    # ##RunMDXProject.LounchBatchRun(mdxProM3JPath)
    # If Crash, Stage1 is Fail
    file = open(r'C:\WorkingFolder\testCase\MDXdata.ini', 'r')
    MDXcontent = file.read()
    file.close()
    strLogVersion = LVC_CheckLogVersion.GetLogVersion(mdxProM3JPath)
    Result = "Stage1_Failed"
    if "Fail" in MDXcontent:
        strLogVersion = "Error: Moldex analysis failed."
    elif "There is no log file" in strLogVersion:
        strLogVersion = "Error: There is no log file."
    else:        
        Result = "Successful"
    LVC_CheckLogVersion.WriteToResultTxt(Result, strLogVersion)
    return Result, strLogVersion
 
# Get Installation MDX Version from Registor ex.R16Beta3Build1710.2422
def Stage2_GetInstallMDX3DVersion():
    Result = "Successful"   
    strInsVersion = LVC_CheckLogVersion.AutoReadMoldexVersion()
    if "None" in strInsVersion:
        Result = "Stage2_Failed"
        strInsVersion = "Error: Cannot find registry infomation."
    LVC_CheckLogVersion.WriteToResultTxt(Result, strInsVersion)  
    return Result, strInsVersion


def Stage3_CheckLogAndInstallVersionMatched(strLogVersion, strInstalVersion):
    Result = "Successful" 
    strCompareResutl = LVC_CheckLogVersion.CompareVersionMatched(strLogVersion, strInstalVersion)
    if "not" not in strCompareResutl:
        Result = "Stage3_Done"
    LVC_CheckLogVersion.WriteToResultTxt(Result, strCompareResutl)        
    return Result, strCompareResutl    

     


if __name__ == '__main__':
    
    Stage1_GetLogVersion()
    #Lauch Project by Moldex Script 
    #tr,strLogVersion = Stage1_GetLogVersion()
    #print " tr strLogVersion  ", tr,strLogVersion 
    #Get Installation Moldex3D Version
    tr,strInstalVersion = Stage2_GetInstallMDX3DVersion()
    print " tr strInstalVersion  ", tr,strInstalVersion     
    
    #Check Log and Installation Moldex3D Version are matched
    #tr = Stage3_CheckLogAndInstallVersionMatched(strLogVersion, strInstalVersion)  
    # print " tr strInstalVersion  ", tr, strCompareResutl 