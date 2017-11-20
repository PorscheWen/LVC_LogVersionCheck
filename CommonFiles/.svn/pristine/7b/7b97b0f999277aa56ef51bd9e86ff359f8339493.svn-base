import sys
import os
import re
import _winreg
dictLogSubFileName = {"TestCase1":".lgf", "TestCase2":".lgf", "TestCase3":".lgp", 
                      "TestCase4":".lgp", "TestCase5":".lgc", "TestCase6":".lgc",
                      "TestCase7":".lgw", "TestCase8": ".lgo","TestCase9":".lgs",
                      "TestCase10":".lgsf","TestCase11": ".lghc","TestCase12":".lgmd",
                      "TestCase13":".lgi","TestCase14": ".lgs","TestCase15": ".lgf",
                      "TestCase16":".lgc","TestCase17": ".lgw"}



# Get Log File Path by Log FileSubName 
def GetLogPath(strProjectM3JPath):
    strTestCaseName = strProjectM3JPath.split("\\")[-2]
    print "TestCaseName: ", strTestCaseName
    strTestCaseNumber = strTestCaseName.split("_")[0] 
    strLogSubFileName = dictLogSubFileName[strTestCaseNumber] 
    strProPath = strProjectM3JPath.split("\\")[:-1]
    strProPath = "\\".join(strProPath)
    for root, dirs, files in os.walk(strProPath):    
        for file in files:
            if file.endswith(strLogSubFileName):
                strLogPath = os.path.join(root, file)
                print "strLogPath", strLogPath
                return strLogPath     
    
# Get Log Version information from Log file content
def GetLogVersion(strProjectM3JPath):
    strLogPath = GetLogPath(strProjectM3JPath)
    strContent = open(strLogPath)
    for line in strContent:
        if "Build" in line:
            strLogVersion = re.split("Build | -", line)[1].replace(")","")
            print "strLogVersion", strLogVersion
            return strLogVersion
        
# Check MDX Version from Registry 
def AutoReadMoldexVersion():
    # Read the Moldex3D installing address
    pyHKEY = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\CoreTechSystem\MDX_ParallelComputing')
    valueInfo = _winreg.QueryInfoKey(pyHKEY) # Read the value infomation(name & data) under the subKey
    versionPathList = []
    for i in range(0, valueInfo[1], 1):
        value = _winreg.EnumValue(pyHKEY, i)
        if "_INSTALLDIR" in value[0]:
            versionPathList.append(value[1])
    if versionPathList ==[]:
        return("MDX setting address Error !!")
    else:
        versionParentPath = str(versionPathList[-1])
    
    # Read the DailyBuild version   
    with open(r"{}\Moldex3D.ver".format(versionParentPath), "r") as localfile :
        versionLine = localfile.read()
    patten = r"R[0-9]{2}[A-Za-z0-9]+ 64-bit \(Build[0-9]{4}[.][0-9]{4}"
    version = re.search(patten, versionLine).group().replace( " 64-bit (", "")
    _winreg.CloseKey(pyHKEY)
    return(version)    



# Filtered data value of LogVersion for comparing: From Build 160.1.1711.8032 -> 16_11_8
def FilterLogVersion(strLogVersion):
    # Arrange data value of LogVersion and InstallVersion for comparing
    strBigLogVersion = strLogVersion.split("0.")[0]
    strLogBuildYearMonth = strLogVersion.split(".")[2]
    strLogBuildDateTime1 = strLogVersion.split(".")[3]
    strLogBuildDate = strLogBuildDateTime1[:-3]
    strFilterLogVersion = strBigLogVersion + "_" + strLogBuildYearMonth + "_" + strLogBuildDate
    WriteToResultTxt( "Filter Log Version: "+strFilterLogVersion, "......Done")
    return strFilterLogVersion

# Filtered data value of InstallVersion for comparing: From R16Beta3Build1711.0832 -> 16_11_8
def FilterInstallVersion(strInstallVersion):
    # Arrange data value of LogVersion and InstallVersion for comparing
    strBigInstallVersion = strInstallVersion[1:3]
    strInstallBuildMonthDateTime= strInstallVersion.split("Build")[1]
    strLogBuildYearMonth = strInstallBuildMonthDateTime.split(".")[0]
    strInstallBuildDate1 = strInstallVersion.split(".")[-1]
    strInstallBuildDate = strInstallBuildDate1[:2]
    # If date initial with 0 remove 0 (ex:08 -> 8)
    if strInstallBuildDate[0] is "0":        
        strInstallBuildDate = strInstallBuildDate[1] 
    strFilterInstallVersion = strBigInstallVersion + "_" + strLogBuildYearMonth + "_" + strInstallBuildDate
    WriteToResultTxt("Filter Install Version: "+strFilterInstallVersion, "......Done" )
    return strFilterInstallVersion    
    
# Comparing Format: 16_11_8 means R16BuildXX11.08XX
def CompareVersionMatched(strLogVersion, strInstallVersion):
    strCompareResult = "Install and Log Version are Not matched !!"
    strFilterLogVersion = FilterLogVersion(strLogVersion)
    strFilterInstallVersion = FilterInstallVersion(strInstallVersion)
    if strFilterLogVersion == strFilterInstallVersion:
        strCompareResult = "Install and Log Version are Matched."
    print "strCompareResult", strCompareResult        
    return strCompareResult

# Search .m3j or .mvj file from testModel folder by os.walk
def GetProjectM3JPath():
    strTestModelPath = r"C:\WorkingFolder\testCase\testModel"
    strProjectM3JPath = "There is no m3j or mvj file in this Project"
    for root, dirs, files in os.walk(strTestModelPath): 
        for file in files:
            if file.endswith("m3j"):
                strProjectM3JPath = os.path.join(root, file)
                WriteToResultTxt("Log Path: "+ strProjectM3JPath, " ......Done")
                return strProjectM3JPath
            if file.endswith("mvj"):
                strProjectM3JPath = os.path.join(root, file)
                WriteToResultTxt("Log Path: "+ strProjectM3JPath, " ......Done")
                return strProjectM3JPath 
    WriteToResultTxt("Log Path: "+ strProjectM3JPath, " ......Fail")
    return strProjectM3JPath     

def WriteToResultTxt(strStatus, strResult):
    if "Create" in strStatus:
        fileMDXdata = open(r'C:\WorkingFolder\testCase\StageResult.ini', 'w')
    else:
        fileMDXdata = open(r'C:\WorkingFolder\testCase\StageResult.ini', 'a')
    strWriteContent = strStatus + "  " + strResult +"\n"
    print strWriteContent
    fileMDXdata.write(strWriteContent)
    fileMDXdata.close()    
    WriteToResultTxt
    
''' 
# Alarm code to ask Install version from Djangle page
def Get_Cur_Test_Build(self, ixTestList):
    SQL = """
    Select 
    test_case_ignore_sbuild_version."sBuild_Version",
    test_case_mdxbuild."sBuild_Daily_Number",
    test_case_mdxbuild.id
    from
    test_case_testlist, test_case_mdxbuild, test_case_ignore_sbuild_version
    where test_case_testlist."Mdx_Build_id" = test_case_mdxbuild.id
    and test_case_ignore_sbuild_version.id = test_case_mdxbuild."sBuild_Version_id"
    and test_case_testlist.id = {0}
    """.format(ixTestList)
    rows = self.Connection(SQL)
    sBuild_Version = rows[0][0]
    sBuild_Daily_Number = rows[0][1]
    ixMdxBuild = rows[0][2]
    return sBuild_Version + sBuild_Daily_Number, ixMdxBuild    
    '''
    

if __name__ == '__main__':

    #strProjectM3JPath = r"C:\WorkingFolder\testCase\TestCase1_Solid_Flow\TestCase1_Solid_Flow.m3j"    
    #GetLogVersion(strProjectM3JPath)
    strLogVersion  = "160.1.1711.18001"  
    #FilterLogVersion(strLogVersion)
    strInstallVersion = "R16Beta3Build1711.0832 "
    #FilterInstallVersion(strInstallVersion)
    CompareVersionMatched(strLogVersion, strInstallVersion)   
    
""" 
 
    #GetProjectM3JPath()
    strProjectM3JPath = r"C:\WorkingFolder\testCase\TestCase1_Solid_Flow\TestCase1_Solid_Flow.m3j"    
    GetLogPath(strProjectM3JPath)    
        """
    