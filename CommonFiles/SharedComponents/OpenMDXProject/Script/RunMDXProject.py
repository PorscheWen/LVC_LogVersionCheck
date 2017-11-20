import os
import subprocess
import winreg
import time

def CreateMSPFile(RunID):
    # ~~input~~
    # RunID: string
    # example: "01"

    # check and create folder
    chkPath = r"C:\work"
    if not os.path.isdir(chkPath):
        os.makedirs(chkPath)

    # *.msp file content
    mspContent = """<?xml version="1.0"?>\n<MDX_SCRIPT_DATA>\n<SCRIPT>\n#CHANGE_RUN = %s\n</SCRIPT>\n</MDX_SCRIPT_DATA>""" % (RunID)
    
    # write file
    NewPath = os.path.join(chkPath,"RunMDXProj.msp")
    mspFile = open(NewPath ,"w")
    mspFile.write(mspContent)
    mspFile.close()
    
def CreateBatchRunMSPFile():
    # Creat msp file for running bjs(Batch Run)

    # check and create folder
    chkPath = r"C:\work"
    if not os.path.isdir(chkPath):
        os.makedirs(chkPath)

    # *.msp file content
    mspContent = """<?xml version="1.0"?>\n<MDX_SCRIPT_DATA>\n<SCRIPT>\n#RUNBATCH\n#EXIT\n</SCRIPT>\n</MDX_SCRIPT_DATA>"""
    
    # write file
    NewPath = os.path.join(chkPath,"RunMDXProj.msp")
    mspFile = open(NewPath ,"w")
    mspFile.write(mspContent)
    mspFile.close()
    
def ModifyMDXProjectReg():
    # modify Moldex3D Project register, turn off "UEP" items.

    # modify register
    keyVal = r'SOFTWARE\CoreTechSystem\Moldex3D R15.0'
    try:
        key = winreg.OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = winreg.CreateKey(HKEY_CURRENT_USER, keyVal)
    winreg.SetValueEx(key, "UEPEMail", 0, REG_SZ, "")
    
    try:
        key = winreg.OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = winreg.CreateKey(HKEY_CURRENT_USER, keyVal)
    winreg.SetValueEx(key, "UEPSendLogFile", 0, REG_SZ, "0")
    
    try:
        key = winreg.OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = winreg.CreateKey(HKEY_CURRENT_USER, keyVal)
    winreg.SetValueEx(key, "UEPSendMDGFile", 0, REG_SZ, "0")    
 
    winreg.CloseKey(key)   

def LounchMXDProject(ProjExePath,mdxProjPath,RunID):
    # ~~input~~
    # ProjExePath: MDX Project.exe location
    # example: "C:\Program Files\Moldex3D\R14.0\Bin\MDXProject.exe"
    # mdxProjPath: Test Project file location
    # example: "C:\Users\Archer\Downloads\Gear\Gear.m3j"
    # RunID: string
    # example: "01"
    
    # Create msp file
    CreateMSPFile(RunID)
    
    # Modify Moldex3D Project register
    ModifyMDXProjectReg()
    
    # Run MDX Script Wizard
    cmdStr = '"' + ProjExePath + '" "' + mdxProjPath + '" + ' + '"C:\\work\\RunMDXProj.msp"'
    #runPara = os.system('"' + cmdStr + '"')
    #runPara = os.popen('"' + cmdStr + '"')
    #runPara = subprocess.call(cmdStr)
    runPara = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE)

    # Wait for the application for 100 seconds, close mdx script window
    #if Sys.WaitProcess("MDXProject", 100000).Exists:
    #if Sys.Process("MDXProject").WaitWindow("#32770","Script Wizard",-1,100000).Exists:
    if Aliases.MDXProject.dlgScriptWizard.waitProperty("Exists", True, 100000):
      time.sleep(5)
      Aliases.MDXProject.dlgScriptWizard.Close()
    else:
      Log.Error("can not find mdx script window")

      
def LounchBatchRun(mdxProjPath):
    # ~~input~~
    # mdxProjPath: Test Project file location
    # example: "C:\Users\Archer\Downloads\Gear\Gear.m3j"
    
    # ProjExePath: MDX Project.exe location
    ProjExePath = "C:\\Moldex3D\\R15.0\\Bin\\MDXProject.exe"
    
    # Create msp file
    CreateBatchRunMSPFile()
    
    # Modify Moldex3D Project register
    ModifyMDXProjectReg()
    
    # Run MDX Script Wizard
    cmdStr = '"' + ProjExePath + '" "' + mdxProjPath + '" + ' + '"C:\\work\\RunMDXProj.msp"'
    runPara = os.system('"' + cmdStr + '"')
    #runPara = os.popen('"' + cmdStr + '"')
    #runPara = subprocess.call(cmdStr)
    #runPara = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE)

    # Wait for the application for 100 seconds, close mdx script window
    #if Sys.WaitProcess("MDXProject", 100000).Exists:
    #if Sys.Process("MDXProject").WaitWindow("#32770","Script Wizard",-1,100000).Exists:
    

    