import os, subprocess, winreg, time, re

# The following modules are imported for backup & log
from TestFile_BackUp_RPT import GetBackUpItemList
from TestFile_BackUp_RPT import BackupTestingResult
from TestFile_LogMessage_RPT import LogSomeMessage
from TestFile_LogMessage_RPT import OutputTypeNumber_dict

#-- The script is built for testing Project ReportOutput: launch report & check report result
#-- 10 type: HTML/     PowerPoint/     PDF/     3DPDF/     PDFSep/
#--          HTMLComp/ PowerPointComp/ PDFComp/ 3DPDFComp/ PDFSepComp


def GetAnalysizeStep(projectName):
    # Get analysis step from each module
    projectName_dict = {"SolidAHR"  : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics", "_Hot Runner Steady"],
                        "SolidBiIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidCFM"  : ["_Filling", "_Cooling", "_Warpage"],
                        "SolidCM"   : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics"],
                        "SolidCoIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidGAIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidEncapsulation" : ["_Filling", "_Cooling","_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Curing", "_Paddle Shift"],
                        "SolidICCM" : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Paddle Shift"],
                        "SolidICM"  : ["_Filling_Packing", "_Cooling", "_Warpage", "_Stress", "_Optics"],
                        "SolidIM"   : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics", "_Mold Deformation"],
                        "SolidMCIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidPIM"  : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "SolidRIM"  : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Curing"],
                        "SolidRTM"  : ["_Filling_Curing"],
                        "SolidWAIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        # ------------------------------------
                        "eDesignPIM" : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "eDN-RIM"    : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Curing"],
                        "eDesignAHR" : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress"],
                        "eDN-CFM"    : ["_Filling", "_Cooling", "_Warpage"],
                        "eDesignCM"  : ["_Filling", "_Cooling","_Mold Preheat", "_Warpage","_Stress"],
                        "eDesign IC" : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Curing"],
                        "eDN-ICCM"   : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep"],
                        "eDN-IM"     : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress"],
                        "eDN-MCIM"   : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        # ------------------------------------
                        "Shell_GAIM" : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "Shell_IM"   : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "Shell_RIM"  : ["_Filling", "_Curing"]
                       }
    analysize_step = projectName_dict.get(projectName, 0)
    analysize_step.insert(0, "_Model")
    return(analysize_step)


# The following results do not have statistic plot
noStatPlot_List = ["Air Trap", "Weld Line", "Gate Contribution", "Molten Core", "Re-melted Area Temperature", "Clamping Force Centroid",
                   "Stream Line Flow Length", "Stream Line Total Velocity",
                   
                   # For PPT
                   "Animation", 
                   ]


# Change the html linked_pictures_name into result_item_name
Change_Report_Name_from_Links_dicts = {"Viscosity"            : "VIS", 
                                       "PVT"                  : "PVT", 
                                       "Heat Capacity"        : "CP" , 
                                       "Thermal Conductivity" : "K", 
                                       "Viscoelasticity"      : "VisE", 
                                       "Structure VE"         : "VISESOLID", 
                                       "Curing Kinetics"      : "CURING", 
                                       "Foaming Kinetics"     : "FOAMING",
                                       "Mechanical Properties": "MECH", 
                                       "Optics"               : "OPTIC",
                                       "Powder Information"   : "POWDER",
                                       "Content"              : "CONT", 
                                       
                                       "Project Settings"          : "ProjectSettings", 
                                       "Filling/Packing Settings"  : "FillingPackingSettings",
                                       "Filling/Curing Settings"   : "FillingPackingSettings",
                                       "Filling Settings"          : "FillingPackingSettings",
                                       "Curing Setting"            : "RTMCuringSettings",
                                       "Microcellular Settings"    : "Microcellular", 
                                       "Foaming Settings"          : "Microcellular",
                                       "GasIn"                     : "GasIn", 
                                       "Cooling Settings"          : "CoolingSettings", 
                                       "Summary"                   : "Summary", 
                                       "Encapsulation"             : "Encapsulation", 
                                       "Compression"               : "Compression", 
                                       "Flow Rate Profile"         : "FlowRate", 
                                       "Injection Pressure Profile": "InjectionPressure", 
                                       "Packing Pressure Profile"  : "PackingPressure", 
                                       "Curing Pressure Profile"   : "CuringPressure", 
                                       "Bi-Injection Molding_EM1"  : "BIInjectionSettings_EM1",
                                       "Bi-Injection Molding_EM2"  : "BIInjectionSettings_EM2",
                                       "Co-Injection Molding_Core" : "CoreInjectionSettings_Core",
                                       "Co-Injection Molding_Skin" : "CoreInjectionSettings_Skin"
                                       } 


def Create_RPT_MSPFile():
    # Check and create folder
    chkPath = r"C:\work"
    if not os.path.exists(chkPath):
        os.makedirs(chkPath)
    
    change_RunID = "1"
    mspContent = "<?xml version=\"1.0\"?>\n<MDX_SCRIPT_DATA>\n<SCRIPT>\n#CHANGE_RUN= {}\n</SCRIPT>\n</MDX_SCRIPT_DATA>".format(change_RunID)
    
    # Command to choose report type and run
    #mspContent = """<?xml version="1.0"?>\n<MDX_SCRIPT_DATA>\n<SCRIPT>\n#GENERATE_REPORT= %s\n#EXIT\n</SCRIPT>\n</MDX_SCRIPT_DATA>""" % (OutputType)
    
    # Write file
    mspPath = os.path.join(chkPath, "RunMDXProj.msp")
    with open(mspPath, "w") as mspFile:
        mspFile.write(mspContent)


# Change the Report templete-setting excel file
def Modify_Report_Setting_Excel():
    WorkPath = r"C:\Users\Administrator\AppData\Roaming\CoreTechSystem\Moldex3D R16\ReportSetting"
    NewWorkPath = r"C:\WorkingFolder\CommonFiles\RPT_Files\ReportSettingMdfy"
    
    # Delete the working directory
    cmd_del_str = 'cmd.exe /c rmdir /s /q \"{}\"'.format(WorkPath)
    os.system(cmd_del_str)
    time.sleep(0.3)
    
    # Rebuid the working directory
    cmd_rebuild_str = 'cmd.exe /c mkdir \"{}\"'.format(WorkPath)
    os.system(cmd_rebuild_str)
    time.sleep(0.3)
    
    # Copy the modified files to the new working directory
    cmd_copy_str = 'cmd.exe /c copy /y \"{}\" \"{}\"'.format(NewWorkPath, WorkPath)
    os.system(cmd_copy_str)
    time.sleep(0.3)


# Auto read the run ID in Project
def AutoReadRunID(Site_Project):
    RunIDList = []
    site_Analysis = r"{}\Analysis".format(Site_Project)
    for site, folder, files in os.walk(site_Analysis): 
        for ID in folder:
            if ID[0:3] == "Run":
                RunIDList.append(ID[3:5]) 
    if len(RunIDList) == 4:
        return(RunIDList[0:2])
    else:
        return(RunIDList)


# Auto change outputType name into only HTML, PDF or PowerPoint
def AutoChangeOutputTypeName(OutputType):
    if "Comp" in OutputType:
        OutputType = OutputType[:-4]
    if "3D" in OutputType:
        OutputType = OutputType[2:]
    if "Sep" in OutputType: 
        OutputType = OutputType[:-3] 
    
    return(OutputType)


# Check if Moldex, IE, Office and AdobeReader been installed 
def SoftwareExeCheck(ProjExePath, OutputType):
    
    exe_Path_dict = {"HTML":       [r"C:\Program Files (x86)\Internet Explorer\iexplore.exe",        "Stage 1 - IE isn't installed yet!"],
                     "PowerPoint": [r"C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE",      "Stage 1 - Office isn't installed yet!"],
                     "PDF":        [r"C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe", "Stage 1 - Adobe Reader isn't installed yet!"]
                     }
    
    if os.path.exists(ProjExePath) == 0:
        return("Stage 1 - Moldex isn't installed yet!")
    
    ClassicType = AutoChangeOutputTypeName(OutputType)
    
    if ClassicType == "HTML":
        IE_Location = exe_Path_dict.get(ClassicType, "")[0]
        if os.path.exists(IE_Location) == 0:
            return(exe_Path_dict.get(ClassicType, "")[1]) 
    
    elif ClassicType == "PowerPoint": 
        PPT_Location = exe_Path_dict.get(ClassicType, "")[0]
        if os.path.exists(PPT_Location) == 0:
            return(exe_Path_dict.get(ClassicType, "")[1]) 
    
    elif ClassicType == "PDF": 
        PDF_Location = exe_Path_dict.get(ClassicType, "")[0]
        if os.path.exists(PDF_Location) == 0:
            return(exe_Path_dict.get(ClassicType, "")[1]) 
    
    return("Stage 1 - Software installed check OK (IE | Office | AdobeReader).")


# Modify Moldex3D Project register, turn off "UEP" items.
def Modify_MDXProject_Reg():
    # modify register
    keyVal = r'SOFTWARE\CoreTechSystem\Moldex3D R16'
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


# Run Report Output bu ReportWizard UI
def RunReportUI( mdxProjPath, OutputType):
    # Close Script Wizard
    Aliases.MDXProject.dlgScriptWizard.WaitProperty("Exists", True, 10000000)
    time.sleep(2)
    Aliases.MDXProject.dlgScriptWizard.Close()
    
    # Open ReportWizard & Change output type
    time.sleep(2)
    Aliases.MDXProject.wndAfx.MainMenu.Click("Post|Report Wizard...")
    
    # Choose output type in UI
    if "Sep" in OutputType:
        Aliases.MDXProject.dlgReportWizard.ComboBox.ClickItem("PDF(Separated by module)")
    else:
        OutputType_mdfy = AutoChangeOutputTypeName(OutputType)    
        Aliases.MDXProject.dlgReportWizard.ComboBox.ClickItem(OutputType_mdfy)
    
    # Choose run
    if "Comp" in OutputType:
        Aliases.MDXProject.dlgReportWizard.ListView.Click(42, 30)  # Run1:(42,30); Run1Model(58,50) 
        Aliases.MDXProject.dlgReportWizard.ListView.Click(42, 30)  # Run1Fill:(58,67)
        Aliases.MDXProject.dlgReportWizard.ListView2.ClickItem("Compare run", 0)
        Aliases.MDXProject.dlgReportWizard.ListView2.btnEdit.ClickButton()
        Aliases.MDXProject.dlgCompareRun.cbxCompare1.ClickItem("Run02")
        Aliases.MDXProject.dlgCompareRun.cbxCompare2.ClickItem("Run03")
        Aliases.MDXProject.dlgCompareRun.cbxCompare3.ClickItem("Run04")
        Aliases.MDXProject.dlgCompareRun.btnOK.ClickButton()  
    else: 
        Aliases.MDXProject.dlgReportWizard.ListView.Click(26, 10)  # Project(26,10); Run1:(42,30); Run1Model(60,50) 
        Aliases.MDXProject.dlgReportWizard.ListView.Click(26, 30)  # Minimize Run1 analysis step 
        Aliases.MDXProject.dlgReportWizard.ListView.Click(42, 48)  # Run2 
        Aliases.MDXProject.dlgReportWizard.ListView.Click(42, 29)  # Run1 
    
    # 3DPDF Option 
    if "3DPDF" in OutputType:
        if "Shell" in mdxProjPath:
            Aliases.MDXProject.dlgReportWizard.ListView2.Click(12, 180)
        else:
            Aliases.MDXProject.dlgReportWizard.ListView2.Click(12, 200)
    
    # Run ReportWizard    
    Aliases.MDXProject.dlgReportWizard.btnOK.ClickButton()


def Check_PPTExe_Run_Once():
    PowerPoint_Opened_Record_File = r"C:\work\Temp\RPT_Already_Open_PPT_Once.txt"
    
    if os.path.exists(PowerPoint_Opened_Record_File) == 0:
        # Modify the reg key to close the firstRun prompt in PowerPoint
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Office\15.0") as key:
            newKey = winreg.CreateKey(key, "Common\\General")
            winreg.SetValueEx(newKey, "shownfirstrunoptin", 0,  winreg.REG_DWORD, 0x00000001)
            
            newKey2 = winreg.CreateKey(key, "FirstRun")
            winreg.SetValueEx(newKey2, "BootedRTM", 0,  winreg.REG_DWORD, 0x00000001) 
        
        # Create the txt after modifing the regs
        os.system("mkdir \"{}\"".format(r"C:\work\Temp"))
        with open(PowerPoint_Opened_Record_File, "a") as localFile:
            localFile.write("") 
        
        return("Modify Office registry... done.")
    
    else:
        return("This VM has already launch Office once.")


def Monitor_MDXProject(backupInfo_Address, OutputType):
    p = subprocess.Popen('tasklist', stdout = subprocess.PIPE, universal_newlines = True, shell = True)
    (output, error) = p.communicate()
    p.terminate()
    
    check_Result = "MDXProject.exe" in str(output)
    
    if check_Result == 1:
        return("MDXProject exists.") 
    elif check_Result == 0:
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - MDXProject crash !", "Error")


def WaitingForOutput(mdxProjPath, OutputType):
    Site_Project = os.path.dirname(mdxProjPath)
    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini"
    
    if "Comp" in OutputType:
        RunIDList = ["01"]
    else:
        RunIDList = AutoReadRunID(Site_Project)
    
    # HTML type ------------------------------------------------
    if OutputType == "HTML" or OutputType == "HTMLComp":
        site_index = r"{}\Report\HTML Report\Report_index.htm".format(Site_Project)
        site_reportTree = r"{}\Report\HTML Report\Report_report_tree.htm".format(Site_Project)
        
        while os.path.exists(site_index) == 0 or os.path.exists(site_reportTree) == 0:
            Monitor_MDXProject(backupInfo_Address, OutputType)
            time.sleep(5)
    
    # PowerPoint type ------------------------------------------------
    elif OutputType == "PowerPoint" or OutputType == "PowerPointComp":
        ID = RunIDList[-1]
        site_PPT = r"{}\Report\PPT Report\Run{runID}\PPT Report-Run{runID}.ppt".format(Site_Project, runID = ID)
        
        click_Office_Active_Window_Once = 0
        
        while os.path.exists(site_PPT) == 0: 
            Monitor_MDXProject(backupInfo_Address, OutputType)
            
            if click_Office_Active_Window_Once == 0:
                # Waiting & skip the activate-Office window
                if Aliases.POWERPNT.wndNUIDialog.WaitProperty("Exists", True, 3000):
                    time.sleep(3)            
                    Aliases.POWERPNT.wndNUIDialog.Close()
                    
                    # Skip the server-busy window
                    if Aliases.MDXProject.dlgServerBusy.Exists == 1:
                        Aliases.MDXProject.dlgServerBusy.btnRetry.ClickButton()
                        Aliases.MDXProject.wndAfx.Minimize()
                    
                    click_Office_Active_Window_Once += 1
            
            time.sleep(5)
    
    # PDF type ------------------------------------------------
    else:
        if "Sep" in OutputType:
            site_PDF = r"{}\Report\PDF Report (Separated)\Run{runID}\PDF Report (Separated)-Run{runID}.pdf"
        else:
            site_PDF = r"{}\Report\PDF Report\Run{runID}\PDF Report-Run{runID}.pdf"
        
        for ID in RunIDList:
            site_PDF2 = site_PDF.format(Site_Project, runID = ID)
            while os.path.exists(site_PDF2) == 0: 
                Monitor_MDXProject(backupInfo_Address, OutputType)
                time.sleep(5) 


def Log_Message_Error(backupInfo_Address, OutputType, log, result):
    if result == "Message":
        LogSomeMessage(backupInfo_Address, "Py3.4", OutputType, log)
        Log.Message(log)
    elif result == "Error":
        BackupTestingResult(backupInfo_Address, "Py3.4", OutputType, "Stage_2", "")
        BackupTestingResult(backupInfo_Address, "Py3.4", OutputType, "Stage_Failed", "")
        LogSomeMessage(backupInfo_Address, "Py3.4", OutputType, "{}...[Error & Stop]".format(log))
        Log.Error(log)


# -----------------------------------------------------------------------------------------------------------------------------------------------
# HTML type checking ----------------------------------------------------------------------------------------------------------------------------

# Change analysis step name into HTML format
def Change_Step_To_HTMLStep(projectName, analysize_step):
    originalStepList = [ "_Model", "_Filling", "_Packing", "_Curing", "_Filling_Packing", "_Filling_Curing", "_Cooling", "_Warpage", "_Optics", "_Paddle Shift", "_Wire Sweep"]
    htmlStepList     = [ "_Mesh", "_Flow", "_Pack", "_Cure", "_Flow", "_Flow", "_Cool", "_Warp", "_Optic", "_PaddleShift", "_WireSweep"]
    html_step = ["_Report"]
    
    for i in analysize_step: 
        if i in originalStepList:
            iindex = originalStepList.index(i)
            html_step.append(htmlStepList[iindex])
        else:
            html_step.append(i)
    
    if projectName == "eDesign IC" or projectName == "SolidEncapsulation":
        html_step.remove( "_Cure") 
        html_step.append( "_Pack") 
    return(html_step)


# Build the Testing_Result folder & record every step result item
def HTML_RecordItem(OutputType, RunPyPath):
    recordHTML_Process = subprocess.Popen(RunPyPath, stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True, shell = True) 
    recordHTML_Process.communicate(OutputType) 
    recordHTML_Process.terminate()  


def HTML_ReadTemplateRange(List, name, rangeType):
    startPoint = List.index('[{}]'.format(name))
    if rangeType == "Module":
        endPoint = List.index('[End_{}]'.format(name)) 
    elif rangeType == "AnalysisStep":
        endPoint = List.index('[End{}]'.format(name))  
    
    new_List = [i.strip() for i in List[startPoint + 1 : endPoint]]
    
    return(new_List)


def Change_HTMLStep_To_THMLLinkStep(projectName, analysisName):
    dic = {"_Flow": "Filling_",   "_Pack": "Packing_",   "_Cool" : "Cooling_",  
           "_Warp": "Warpage_",   "_Cure": "Curing_" ,   "_Optic": "Optics_", 
           "_WireSweep"        : "Wire Sweep_", 
           "_Stress"           : "Stress_", 
           "_PaddleShift"      : "Paddle Shift_", 
           "_Hot Runner Steady": "Hot Runner Steady_", 
           "_Mold Preheat"     : "Mold Preheat_", 
           "_Mold Deformation" : "Mold Deformation_"
           }
    if projectName == "eDesign IC" or projectName == "SolidEncapsulation":
        if analysisName == "_Pack":
            cutWord = dic.get("_Cure", "_Cure")
        else: 
            cutWord = dic.get(analysisName, analysisName)
    else:
        cutWord = dic.get(analysisName, analysisName)
    
    return(cutWord)


def HTML_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address):
    
    # Read project name
    projectName = os.path.basename(Site_Project)
    # Read project analysize_step
    analysize_step = GetAnalysizeStep(projectName)
    # Read project html_step
    htmlReport_step = Change_Step_To_HTMLStep(projectName, analysize_step)
    
    # Read Module item from HTML Template
    with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\html_template.ini", "r") as template_AllModule:
        htmlTemplate = template_AllModule.read().split('\n') 
    projectTemplate = HTML_ReadTemplateRange(htmlTemplate, projectName, "Module")
    
    # Read Module remark from HTML Template_remark
    with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\html_remark.ini", "r") as template_remark_AllModule:
        html_remark = template_remark_AllModule.read().split('\n')     
    projectRemark = HTML_ReadTemplateRange(html_remark, projectName, "Module")
    
    if OutputType == "HTML":
        reportIDList = RunIDList
    elif OutputType == "HTMLComp":
        reportIDList = RunIDList[0:1]
    
    for ID in reportIDList:
        for analysisName in htmlReport_step:
            
            # STEP 1: Check item exist ---------------------------------------------------------------------
            # Read each step item from Template
            analysisItemList_Temp = HTML_ReadTemplateRange(projectTemplate, analysisName, "AnalysisStep")
            
            # Read each step item from HTML
            with open(r"{}\Report\HTML Report\Testing_Result\Run{}.txt".format(Site_Project, ID + analysisName), "r") as item_HTML:
                itemList = item_HTML.read().split('\n')
            itemList.remove("")
            
            # Compare item from HTML & item from Template
            errorItemSet = list(set(analysisItemList_Temp)^set(itemList))
            
            if errorItemSet != []: 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: {}".format(ID + analysisName, errorItemSet), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} item check Failed !".format(ID + analysisName), "Error") 
            
            
            # STEP 2-1: Check remark correct ---------------------------------------------------------------------
            if analysisName not in ["_Report", "_Mesh"]:
                # Read each step remark from Template_remark
                analysisRemarkList = HTML_ReadTemplateRange(projectRemark, analysisName, "AnalysisStep")
                
                # Read each item remark from HTML_remark
                with open(r"{}\Report\HTML Report\Testing_Result\Run{}-Remark.txt".format(Site_Project, ID + analysisName), "r") as remark_HTML:
                    remarkList = remark_HTML.read().split('\n')
                remarkList.remove("")
                
                # Check if remarks are in template_remark
                error_item_remark_List = []
                for item in analysisRemarkList:
                    if item in analysisItemList_Temp:
                        itemIndex = analysisRemarkList.index(item)
                        item_remark = analysisRemarkList[itemIndex + 1]
                        if item_remark not in remarkList:
                            error_item_remark_List.append(item)
                
                if error_item_remark_List != []:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: {}".format(ID + analysisName, error_item_remark_List), "Message") 
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} remark check Failed !".format(ID + analysisName), "Error") 
                
                
                # STEP 2-2: Check statistics plot exist ---------------------------------------------------------------------
                # Read each item with statPlot from HTML_statPlot
                with open(r"{}\Report\HTML Report\Testing_Result\Run{}-StatisticsPlot.txt".format(Site_Project, ID + analysisName), "r") as statPlot_HTML:
                    statPlotList = statPlot_HTML.read().split('\n')
                statPlotList.remove("")
                
                # Verify if item has a statPlot in template_item
                item_with_StatPlot_List = []
                for item in analysisItemList_Temp:
                    if item in noStatPlot_List:
                        pass
                    elif ("-Animation" in item) or ("XY Curve Animation" in item) or ("XY_" in item):
                        pass
                    elif ("Melt Front Time" in item) and ("_" in item): 
                        pass # Ex: "Melt Front Time_2", "Melt Front Time (Skin)_2"
                    else:
                        item_with_StatPlot_List.append(item)
                
                # Check if items been filtered have a StatPlot
                error_item_statPlot_list = []
                for item in item_with_StatPlot_List:
                    itemIndex = statPlotList.index(item)
                    item_statPlot = statPlotList[itemIndex + 1]
                    if item_statPlot != "Statistics plot":
                        error_item_statPlot_list.append(item)
                
                if error_item_statPlot_list != []:
                    for item in error_item_statPlot_list:
                        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: [{}]".format(ID + analysisName, item), "Message") 
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} statistic_plot check Failed !".format(ID + analysisName), "Error")
            
            
            # STEP 3: Check links ---------------------------------------------------------------------
            # Read links from HTML_link
            with open(r"{}\Report\HTML Report\Testing_Result\Run{}-Link.txt".format(Site_Project, ID + analysisName), "r") as link_HTML:
                linkList = link_HTML.read().split('\n')
            linkList.remove("")
            
            for link in linkList:
                if "\\Moldex3D" in link:
                    mdxIndex = linkList.index(link)
                    linkList.remove(linkList[mdxIndex])
            
            # STEP 3-1: Check each item has a img/statPlot link ---------------------------------------------------------------------
            # Read item name from HTML links
            item_from_Link_List = []
            for link in linkList:
                item_extent_from_Link = os.path.splitext(link)[0]
                item_from_Link = os.path.basename(item_extent_from_Link) 
                
                if analysisName == "_Report":
                    if "Process_" in item_from_Link:
                        item_from_Link3 = item_from_Link.split("Process_")[-1]
                    else:
                        item_from_Link3 = item_from_Link.split("_")[-1]
                elif analysisName == "_Mesh":
                    item_from_Link3 = item_from_Link
                else:
                    if "Animation" in item_from_Link:
                        item_from_Link3 = "Animation"
                    elif "XY_" in item_from_Link and "_Melt Front Time" in item_from_Link :
                        item_from_Link3 = "XY Curve Animation"
                    elif "ing_Melt Front Time" in item_from_Link:
                        item_from_Link3 = item_from_Link.split("ing_")[-1]
                    elif "Melt Front Time" in item_from_Link and "_" in item_from_Link:
                        item_from_Link3 = item_from_Link
                    elif "Statistics_" in item_from_Link or "XY_" in item_from_Link:
                        item_from_Link3 = item_from_Link
                    else:
                        cutWord = Change_HTMLStep_To_THMLLinkStep(projectName, analysisName)
                        item_from_Link3 = item_from_Link.split(cutWord)[-1]
                
                item_from_Link_List.append(item_from_Link3)
            
            # Read item name (modified) from item_Template
            # List_1 for item result_plot; 
            # List_2 for item result_statistic_plot 
            itemModify_List_1 = []
            itemModify_List_2 = []
            # Read items (modified) in "_Report" from item_Template
            if analysisName == "_Report": 
                for item in analysisItemList_Temp:
                    if "Material " in item or "Process -" in item:
                        item_modify = item.replace("Material ", "").replace("Process - ", "")
                        item_modify2 = Change_Report_Name_from_Links_dicts.get( item_modify, item)
                        itemModify_List_1.append(item_modify2)
            
            elif analysisName != "_Report":
                # Read items (modified) from item_Template
                for item in analysisItemList_Temp:
                    if item[-1] == " ":
                        item_modify = item[:-1]
                    elif "XY Curve Animation" in item:
                        item_modify = "XY Curve Animation"
                    elif "Animation" in item:
                        item_modify = "Animation"
                    elif "#" in item:
                        item_modify = item.replace("#", " ")
                    else:
                        item_modify = item
                    
                    itemModify_List_1.append(item_modify)
                
                # Read items (modified) owned "statistic plot" from item_Template
                if analysisName == "_Mesh":
                    itemModify_List_2.append("Thickness")                 
                elif analysisName != "_Mesh":
                    for item in analysisItemList_Temp:
                        if item in item_with_StatPlot_List:
                            if item[-1] == " ":
                                item_modify = item[:-1]
                            elif "Animation" in item:
                                item_modify = "Animation"
                            elif "#" in item:
                                item_modify = item.replace("#", " ")
                            else:
                                item_modify = item
                        
                        itemModify_List_2.append(item_modify)
            
            # Check if each item has a result image  
            errorLinks_List_1 = []
            for item_modify in itemModify_List_1:
                if item_modify not in item_from_Link_List:
                    errorLinks_List_1.append(item_modify)
            
            if errorLinks_List_1 != []:
                for link in errorLinks_List_1:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: [{}]".format(ID + analysisName, link), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} result_plot links Error !".format(ID + analysisName), "Error") 
            
            # Check if the specific item has a statistic plot
            if analysisName != "Report":
                errorLinks_List_2 = []
                for item_modify in itemModify_List_2:
                    if "Statistics_{}".format(item_modify) not in item_from_Link_List:
                        errorLinks_List_2.append("Statistics_{}".format(item_modify))
                
                if errorLinks_List_2 != []:
                    for link in errorLinks_List_2:
                        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: [{}]".format(ID + analysisName, link), "Message") 
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} result_statistic_plot links Error !".format(ID + analysisName), "Error")             
            
            
            # STEP 3-2: Check linked files exist ---------------------------------------------------------------------
            with open(r"{}\Report\HTML Report\Testing_Result\Run{}-Link.txt".format(Site_Project, ID + analysisName), "r") as link_HTML:
                linkList2 = link_HTML.read().split('\n')
            linkList2.remove("")
            
            errorLinks_List_3 = []
            for link in linkList2:
                # Absolute path
                if os.path.isabs(link) == 1:
                    if os.path.exists(link) == 0 or os.path.isfile(link) == 0:
                        errorLinks_List_3.append(link) 
                # relative path
                elif os.path.isabs(link) == 0:
                    absLink = link.replace(".\\", r"{}\Report\HTML Report\Run{}".format(Site_Project, ID) + "\\").replace(r"\\", "\\")
                    if os.path.exists(absLink) == 0 or os.path.isfile(absLink) == 0:
                        errorLinks_List_3.append(absLink)
            
            if errorLinks_List_3 != []:
                for link in errorLinks_List_3:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} arises problems: [{}]".format(ID + analysisName, link), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} linked files doesn't exist !".format(ID + analysisName), "Error") 
        
        
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} all result item check OK.".format(ID), "Message") 
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} all result item remark check OK.".format(ID), "Message") 
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} all result item statistic_plot check OK.".format(ID), "Message")
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} all result item image links check OK.".format(ID), "Message")


def HTML_MultiRunResultName(result, List):
    i = 1
    while "Run0{}__{}".format(i, result) in List:
        i += 1
    return("Run0{}__{}".format(i, result))  


def HTML_Comp_Check_Item(Site_Project, OutputType, backupInfo_Address):
    
    # Read project name
    projectName = os.path.basename(Site_Project)
    # Read project analysize_step
    analysize_step = GetAnalysizeStep(projectName)
    # Read project html_step
    htmlReport_step = Change_Step_To_HTMLStep(projectName, analysize_step)
    
    # Read Module item from HTML Template
    with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\html_template.ini", "r") as template_AllModule:
        htmlTemplate = template_AllModule.read().split('\n') 
    projectTemplate = HTML_ReadTemplateRange(htmlTemplate, projectName, "Module")
    
    # Read Module remark from HTML Template_remark
    with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\html_remark.ini", "r") as template_remark_AllModule:
        html_remark = template_remark_AllModule.read().split('\n') 
    projectRemark = HTML_ReadTemplateRange(html_remark, projectName, "Module")
    
    
    for analysisName in htmlReport_step:
        # STEP 1-1: Check item exist ---------------------------------------------------------------------
        # Read each step item from Template
        analysisItemList_Temp = HTML_ReadTemplateRange(projectTemplate, analysisName, "AnalysisStep")
        
        # Read each step item from HTML
        with open(r"{}\Report\HTML Report\Testing_Result\Run01{}.txt".format(Site_Project, analysisName), "r") as item_HTML:
            itemList = item_HTML.read().split('\n')
        itemList.remove("")
        
        # Compare item from HTML & item from Template
        errorItemSet = list(set(analysisItemList_Temp)^set(itemList))
        
        if errorItemSet != []: 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: {}".format(analysisName, errorItemSet), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} item check Failed !".format(analysisName), "Error") 
        
        # STEP 1-2: Check sub-item exist (Run01 ~ Run04) -----------------------------------------------------
        # Read each item remark from HTML_remark
        if analysisName != "_Report":
            with open(r"{}\Report\HTML Report\Testing_Result\Run01{}-StatisticsPlot_Remark.txt".format(Site_Project, analysisName), "r") as statPlot_Remark_HTML:
                StatPlot_Remark_List = statPlot_Remark_HTML.read().split('\n')
            StatPlot_Remark_List.remove("") 
            
            noFramItem_List = ["Temperature", "Time to Reach Ejection Temperature", "Volumetric Shrinkage"]
        
        # Compare sub-item from HTML & item from Template
        errorItemSet2 = []
        if analysisName == "_Report":
            for item in analysisItemList_Temp:
                if "Material " in item or "Process - " in item:
                    sub_itemIndex = itemList.index(item)
                    sub_item_List = itemList[sub_itemIndex: sub_itemIndex + 4]
                    for i in itemList[sub_itemIndex: sub_itemIndex + 4]:
                        if i != item:
                            errorItemSet2.append(item)
        
        elif analysisName == "_Mesh":
            item2 = "Thickness"
            sub_itemIndex = StatPlot_Remark_List.index("Run01-{}".format(item2))
            sub_item_List = StatPlot_Remark_List[sub_itemIndex + 4: sub_itemIndex + 8]
            
            for i in range(0, 4):
                if "Run0{}-{}".format(i + 1, item2) not in sub_item_List:
                    errorItemSet2.append("Run0{}-{}".format(i + 1, item)) 
        
        else:
            for item in analysisItemList_Temp:
                if item in noFramItem_List:
                    pass
                elif "-Animation" in item or "XY Curve Animation" in item:
                    pass
                else:
                    if "Melt Front Time" in item and "_" in item:
                        item2 = item.replace("_", " ( ") + "0% )"
                    else:
                        item2 = item
                    
                    sub_itemIndex = StatPlot_Remark_List.index("Run01-{}".format(item2))
                    sub_item_List = StatPlot_Remark_List[sub_itemIndex: sub_itemIndex + 4]
                    
                    for i in range(0, 4):
                        if "Run0{}-{}".format(i + 1, item2) not in sub_item_List:
                            errorItemSet2.append("Run0{}-{}".format(i + 1, item)) 
        
        if errorItemSet2 != []: 
            for item in errorItemSet2:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: [{}]".format(analysisName, item), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} sub_item check Failed !".format(analysisName), "Error") 
        
        
        # STEP 2-1: Check remark correct ---------------------------------------------------------------------
        if analysisName not in ["_Report", "_Mesh"]:
            # Read each step remark from Template_remark
            analysisRemarkList_Temp = HTML_ReadTemplateRange(projectRemark, analysisName, "AnalysisStep")
            
            # Check if remarks are in template_remark
            error_item_remark_List = []
            for item in analysisRemarkList_Temp:
                if item in analysisItemList_Temp:
                    itemIndex = analysisRemarkList_Temp.index(item)
                    item_remark = analysisRemarkList_Temp[itemIndex + 1]
                    
                    itemIndex2 = StatPlot_Remark_List.index(item)
                    item_remark2 = StatPlot_Remark_List[itemIndex2 + 1]
                    if item_remark != item_remark2:
                        error_item_remark_List.append(item)
            
            if error_item_remark_List != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: {}".format(analysisName, error_item_remark_List), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} remark check Failed !".format(analysisName), "Error") 
        
        
        # STEP 2-2: Check statistics plot exist ---------------------------------------------------------------------
        if analysisName != "_Report":
            # Verify if item has a statPlot in template_item
            item_with_StatPlot_List = []
            for item in analysisItemList_Temp:
                if item in noStatPlot_List:
                    pass
                elif ("-Animation" in item) or ("XY Curve Animation" in item) or ("XY_" in item):
                    pass
                elif ("Melt Front Time" in item) and ("_" in item):
                    pass
                else:
                    item_with_StatPlot_List.append(item)
            
            # Check if items been filtered have a StatPlot
            error_item_statPlot_list = []
            if analysisName == "_Mesh":
                item = "Run01-Thickness"
                itemIndex = StatPlot_Remark_List.index(item)
                item_statPlot_List = StatPlot_Remark_List[itemIndex: itemIndex + 4] 
                for i in range(0, 4):
                    if "Run0{}-Thickness".format(i + 1) not in item_statPlot_List:
                        error_item_statPlot_list.append("{}__Run0{}-Statistics plot".format(item, i + 1)) 
            
            else:
                for item in item_with_StatPlot_List:
                    itemIndex = StatPlot_Remark_List.index(item)
                    item_statPlot_List = StatPlot_Remark_List[itemIndex + 2: itemIndex + 6]
                    for i in range(0, 4):
                        if "Run0{}-Statistics plot".format(i + 1) not in item_statPlot_List:
                            error_item_statPlot_list.append("{}__Run0{}-Statistics plot".format(item, i + 1)) 
            
            if error_item_statPlot_list != []:
                for item in error_item_statPlot_list:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: [{}]".format(analysisName, item), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} statistic_plot check Failed !".format(analysisName), "Error")
        
        
        # STEP 3: Check links ---------------------------------------------------------------------
        # Read links from HTML_link
        with open(r"{}\Report\HTML Report\Testing_Result\Run01{}-Link.txt".format(Site_Project, analysisName), "r") as link_HTML:
            linkList = link_HTML.read().split('\n')
        linkList.remove("")
        
        for link in linkList:
            if "\\Moldex3D" in link:
                mdxIndex = linkList.index(link)
                linkList.remove(linkList[mdxIndex])
        
        # STEP 3-1: Check each item has a img/statPlot link ---------------------------------------------------------------------
        # Read item name from HTML links
        item_from_Link_List = []
        for link in linkList:
            item_extent_from_Link = os.path.splitext(link)[0]
            item_from_Link = os.path.basename(item_extent_from_Link) 
            
            if analysisName == "_Report":
                #print(item_from_Link)
                if "Process_" in item_from_Link:
                    item_from_Link2 = item_from_Link.split("Process_")[-1]
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link2, item_from_Link_List)
                else:
                    item_from_Link2 = item_from_Link.split("_")[-1]
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link2, item_from_Link_List)
            
            elif analysisName == "_Mesh":
                item_from_Link3 = HTML_MultiRunResultName(item_from_Link, item_from_Link_List)
            
            else:
                if "Animation" in item_from_Link:
                    item_from_Link3 = HTML_MultiRunResultName("Animation", item_from_Link_List)
                
                elif "XY_" in item_from_Link and "_Melt Front Time" in item_from_Link :
                    item_from_Link3 = HTML_MultiRunResultName("XY Curve Animation", item_from_Link_List)          
                
                elif "ing_Melt Front Time" in item_from_Link:
                    item_from_Link2 = item_from_Link.split("ing_")[-1]
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link2, item_from_Link_List)
                
                elif "Melt Front Time" in item_from_Link and "_" in item_from_Link:
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link, item_from_Link_List)
                
                elif "Statistics_" in item_from_Link or "XY_" in item_from_Link:
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link, item_from_Link_List)
                
                else:
                    cutWord = Change_HTMLStep_To_THMLLinkStep(projectName, analysisName)
                    item_from_Link2 = item_from_Link.split(cutWord)[-1]
                    item_from_Link3 = HTML_MultiRunResultName(item_from_Link2, item_from_Link_List)
            
            item_from_Link_List.append(item_from_Link3)
        
        # Read item name (modified) from item_Template
        # List_1 for item result_plot; 
        # List_2 for item result_statistic_plot 
        itemModify_List_1 = []
        itemModify_List_2 = []
        # Read items (modified) in "_Report" from item_Template
        if analysisName == "_Report": 
            for item in analysisItemList_Temp:
                if "Material " in item or "Process -" in item:
                    item_modify = item.replace("Material ", "").replace("Process - ", "")
                    item_modify2 = Change_Report_Name_from_Links_dicts.get( item_modify, item)
                    itemModify_List_1.append(item_modify2)
        
        elif analysisName != "_Report":
            # Read items (modified) from item_Template
            for item in analysisItemList_Temp:
                if item[-1] == " ":
                    item_modify = item[:-1]
                elif "XY Curve Animation" in item:
                    item_modify = "XY Curve Animation"
                elif "Animation" in item:
                    item_modify = "Animation"
                elif "#" in item:
                    item_modify = item.replace("#", " ")
                else:
                    item_modify = item
                
                itemModify_List_1.append(item_modify)        
            
            # Read items (modified) owned "statistic plot" from item_Template
            if analysisName == "_Mesh":
                itemModify_List_2.append("Thickness")                 
            elif analysisName != "_Mesh":
                for item in analysisItemList_Temp:
                    if item in item_with_StatPlot_List:
                        if item[-1] == " ":
                            item_modify = item[:-1]
                        elif "Animation" in item:
                            item_modify = "Animation"
                        elif "#" in item:
                            item_modify = item.replace("#", " ")
                        else:
                            item_modify = item
                    
                    itemModify_List_2.append(item_modify)
        
        # Check if each item has a result image  
        errorLinks_List_1 = []
        for item_modify in itemModify_List_1:
            for i in range(0, 4):
                if "Run0{}__{}".format(i + 1, item_modify) not in item_from_Link_List:
                    errorLinks_List_1.append("{}".format(item_modify)) 
        
        if errorLinks_List_1 != []:
            for link in errorLinks_List_1:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: [{}]".format(analysisName, link), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} result_plot links Error !".format(analysisName), "Error") 
        
        # Check if the specific item has a statistic plot
        if analysisName != "Report":
            errorLinks_List_2 = []
            for item_modify in itemModify_List_2:
                for i in range(0, 4):
                    if "Run0{}__Statistics_{}".format(i + 1, item_modify) not in item_from_Link_List:
                        errorLinks_List_2.append("Statistics_{}".format(item_modify)) 
            
            if errorLinks_List_2 != []:
                for link in errorLinks_List_2:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: [{}]".format(analysisName, link), "Message") 
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} result_statistic_plot links Error !".format(analysisName), "Error") 
        
        
        # STEP 3-2: Check linked files exist ---------------------------------------------------------------------
        with open(r"{}\Report\HTML Report\Testing_Result\Run01{}-Link.txt".format(Site_Project, analysisName), "r") as link_HTML:
            linkList2 = link_HTML.read().split('\n')
        linkList2.remove("")
        
        errorLinks_List_3 = []
        for link in linkList2:
            # Absolute path
            if os.path.isabs(link) == 1:
                if os.path.exists(link) == 0 or os.path.isfile(link) == 0:
                    errorLinks_List_3.append(link) 
            
            # relative path
            elif os.path.isabs(link) == 0:
                if r".\\" in link and r"..\\..\\" not in link:
                    absLink = link.replace(r".\\", r"{}\Report\HTML Report\Run01".format(Site_Project) + "\\").replace(r"\\", "\\")
                    if os.path.exists(absLink) == 0 or os.path.isfile(absLink) == 0:
                        errorLinks_List_3.append(link)
                
                elif r"..\\..\\" in link:
                    absLink = link.replace(r"..\\..\\", r"{}\Report\HTML Report".format(Site_Project) + "\\").replace(r"\\", "\\")
                    if os.path.exists(absLink) == 0 or os.path.isfile(absLink) == 0:
                        errorLinks_List_3.append(link)                    
        
        if errorLinks_List_3 != []:
            for link in errorLinks_List_3:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} arises problems: [{}]".format(analysisName, link), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01{} linked files doesn't exist !".format(analysisName), "Error") 
    
    
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01 all result item check OK.", "Message") 
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01 all result item remark check OK.", "Message") 
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01 all result item statistic plot check OK.", "Message")
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run01 all result item image links check OK.", "Message") 


# ----------------------------------------------------------------------------------------------------------------------------------------------
# PDF type checking ----------------------------------------------------------------------------------------------------------------------------

def PDF_Check_Item(OutputType, Site_Project, backupInfo_Address):
    if "Comp" not in OutputType:
        RunIDList = AutoReadRunID(Site_Project)
    else:
        RunIDList = ["01"] 
    
    if OutputType == "PDF" or OutputType == "3DPDF" or OutputType == "PDFComp" or OutputType == "3DPDFComp":
        for ID in RunIDList:
            site_PDF = r"{}\Report\PDF Report\Run{runID}\PDF Report-Run{runID}.pdf".format(Site_Project, runID = ID)
            site_TXT = site_PDF.replace(".pdf", ".txt")
            savePDFLocation = os.path.dirname(site_PDF)
            
            # Open PDF & save to txt
            cmdStr = '\"{}\"'.format(site_PDF)
            subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
            PDF_Save_to_TXT(savePDFLocation, site_TXT, OutputType)
            
            # Read title ini_template
            INI_Title_results = PDF_Read_ini_Template(Site_Project, OutputType)
            
            # Read result & remark from txt
            # Result_remark_results is empty ( {} ) for compare type & 3DPDF
            Title_results, Result_remark_results = PDF_TXTread(site_TXT, OutputType)
            
            # Title compare -------------------------------------------------------------------
            ini_Title_Result_set = set(INI_Title_results)
            Title_results_set = set(Title_results)
            
            if ini_Title_Result_set != Title_results_set:
                ini_Exculde_Str = str(ini_Title_Result_set.union(Title_results_set) - Title_results_set)
                txt_Exculde_Str = str(ini_Title_Result_set.union(Title_results_set) - ini_Title_Result_set)
                
                Log_Message_Error(backupInfo_Address, OutputType, "INI_Result: {}".format(ini_Exculde_Str), "Message")
                Log_Message_Error(backupInfo_Address, OutputType, "Result:     {}".format(txt_Exculde_Str), "Message")
                
                err_log = "Stage 2 - Run{} title Not Match !".format(ID)
                Log_Message_Error(backupInfo_Address, OutputType, err_log, "Error")
            
            # Remark compare -------------------------------------------------------------------
            if OutputType == "PDF" or OutputType == "3DPDF":
                # Read remark from ini_template
                INI_Result_remark_results = PDF_Read_ini_Remark(Site_Project, OutputType)
                
                # Call another py to change the Result_remark_results set if OutputType == 3DPDF
                if OutputType == "3DPDF":
                    PDF_Call3DPDF_Remark(Site_Project, ID)
                    Result_remark_results = PDF_Read_3DPDF_Remark_Temp(Site_Project)
                
                # Result remark compare
                if Result_remark_results != INI_Result_remark_results:
                    txt_Remark_Exculde_Str = set(Result_remark_results.items()) - set(INI_Result_remark_results.items())
                    ini_Remark_Exculde_Str = set(INI_Result_remark_results.items()) - set(Result_remark_results.items())
                    
                    Log_Message_Error(backupInfo_Address, OutputType, "Result_remark:     {}".format(txt_Remark_Exculde_Str), "Message")
                    Log_Message_Error(backupInfo_Address, OutputType, "INI_Result_remark: {}".format(ini_Remark_Exculde_Str), "Message")
                    
                    err_log = "Stage 2 - Run{} remark Not Match !".format(ID)
                    Log_Message_Error(backupInfo_Address, OutputType, err_log, "Error")
            
            cmdStr = '"taskkill /f /im AcroRd32.exe"'
            os.system(cmdStr)
            Aliases.AcroRd32.wndAcrobatSDIWindow.WaitProperty("Exists", False, 10000000)
            
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} title check OK.".format(ID), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} remark check OK.".format(ID), "Message")
    
    
    elif OutputType == "PDFSep" or OutputType == "PDFSepComp":
        projectName = os.path.basename(Site_Project)
        analysize_step = GetAnalysizeStep(projectName)
        analysize_step.append('')  # add ''   	
        
        for ID in RunIDList:
            for ResultName in analysize_step:
                site_PDF = r"{}\Report\PDF Report (Separated)\Run{}\PDF Report (Separated)-Run{}.pdf".format(Site_Project, ID, ID + ResultName)
                site_TXT = site_PDF.replace(".pdf", ".txt")
                savePDFLocation = os.path.dirname(site_PDF)
                
                cmdStr = '\"{}\"'.format(site_PDF)
                subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
                PDF_Save_to_TXT(savePDFLocation, site_TXT, OutputType)
                
                # Need to check Title & Result remark
                Title_results, Result_remark_results = PDF_TXTread(site_TXT, OutputType) # Result_remark_results is empty ( {} ) for compare type
                INI_Title_results = PDF_Read_ini_Template(Site_Project, OutputType, ResultName)
                
                # Title compare -------------------------------------------------------------------
                Title_results_set = set(Title_results)
                ini_Title_Result_set = set(INI_Title_results)
                
                if ini_Title_Result_set != Title_results_set:
                    ini_Exculde_Str = str(ini_Title_Result_set.union(Title_results_set) - Title_results_set)
                    txt_Exculde_Str = str(ini_Title_Result_set.union(Title_results_set) - ini_Title_Result_set)
                    
                    Log_Message_Error(backupInfo_Address, OutputType, "INI_Result: {}".format(ini_Exculde_Str), "Message")
                    Log_Message_Error(backupInfo_Address, OutputType, "Result:     {}".format(txt_Exculde_Str), "Message")
                    
                    err_log = "Stage 2 - Run{} title Not Match !".format(ID + ResultName)
                    Log_Message_Error(backupInfo_Address, OutputType, err_log, "Error")
                
                # Remark compare -------------------------------------------------------------------
                if OutputType == "PDFSep":
                    INI_Result_remark_results = PDF_Read_ini_Remark(Site_Project, OutputType, ResultName)
                    
                    if Result_remark_results != INI_Result_remark_results:
                        txt_Remark_Exculde_Str = set(Result_remark_results.items()) - set(INI_Result_remark_results.items())
                        ini_Remark_Exculde_Str = set(INI_Result_remark_results.items()) - set(Result_remark_results.items())
                        
                        Log_Message_Error(backupInfo_Address, OutputType, "Remark_results:     {}".format(txt_Remark_Exculde_Str), "Message")
                        Log_Message_Error(backupInfo_Address, OutputType, "INI_Remark_results: {}".format(ini_Remark_Exculde_Str), "Message")
                        
                        err_log = "Stage 2 - Run{} remark Not Match !".format(ID + ResultName)
                        Log_Message_Error(backupInfo_Address, OutputType, err_log, "Error")
                
                cmdStr = '"taskkill /f /im AcroRd32.exe"'
                os.system(cmdStr)
                Aliases.AcroRd32.wndAcrobatSDIWindow.WaitProperty("Exists", False, 10000000) 
            
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} title check OK.".format(ID), "Message") 
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} remark check OK.".format(ID), "Message")


def PDF_Call3DPDF_Remark(Site_Project, ID):
    RunPypath = r"C:\WorkingFolder\CommonFiles\PythonScript\Check3DPDFResultremark.py"
    totalStr1 = Site_Project + "@@" + ID
    record3DPDF_Process = subprocess.Popen(RunPypath, stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True, shell = True)
    record3DPDF_Process.communicate(totalStr1)
    record3DPDF_Process.terminate()  # for stop this process


def PDF_Read_3DPDF_Remark_Temp(Site_Project):
    moduleName = os.path.basename(Site_Project)
    folder_path = r"{}\Report\PDF Report\Testing_Result".format(Site_Project)
    
    sPath = r"{}\temp.ini".format(folder_path)
    Key = Storages.INI(sPath)
    
    # Specifies the name of the needed subkey
    Count = Key.GetSubSection(moduleName).OptionCount
    
    INI_Result_remark_results = {}
    
    #Log.Message(Count)
    for i in range(0, Count):
        ValueName = Key.GetSubSection(moduleName).GetOptionName(i)
        value = Key.GetSubSection(moduleName).GetOption(ValueName, "")
        INI_Result_remark_results[ValueName.strip()] = value.strip()
    
    return(INI_Result_remark_results)


def PDF_Read_ini_Remark(Site_Project, OutputType, result_Step = ''):
    
    moduleName = "{}_{}{}".format(os.path.basename(Site_Project), OutputType, result_Step)
    
    sPath = r"C:\WorkingFolder\CommonFiles\RPT_Files\pdf_remark.ini"
    Key = Storages.INI(sPath)
    
    # Specifies the name of the needed subkey
    Count = Key.GetSubSection(moduleName).OptionCount
    
    INI_Result_remark_results = {}
    
    for i in range(0, Count):
        ValueName = Key.GetSubSection(moduleName).GetOptionName(i)
        value = Key.GetSubSection(moduleName).GetOption(ValueName, "")
        INI_Result_remark_results[ValueName.strip()] = value.strip()
    
    return(INI_Result_remark_results)


def PDF_Read_ini_Template(Site_Project, OutputType, result_Step = ''):
    
    moduleName = "{}_{}{}".format(os.path.basename(Site_Project), OutputType, result_Step)
    
    sPath = r"C:\WorkingFolder\CommonFiles\RPT_Files\pdf_template.ini"
    Key = Storages.INI(sPath)
    
    # Specifies the name of the needed subkey
    Count = Key.GetSubSection(moduleName).OptionCount
    
    INI_Title_results = []
    
    for i in range(0, Count):
        ValueName = Key.GetSubSection(moduleName).GetOptionName(i)
        INI_Title_results.append(ValueName.strip())
    
    if "Comp" in OutputType:
        rep = [ x.split("@")[0] if "@" in x else x for x in INI_Title_results]
        INI_Title_results = rep
    
    return(INI_Title_results)


# Read the result from each txt
def PDF_TXTread(site_TXT, OutputType):
    # Check if the site_TXT file can be launched
    try:
        with open(site_TXT, 'r') as fileRead:
            txtTemplage = fileRead.read().split('\n')
    except:
        cmdStr = '"taskkill /f /im AcroRd32.exe"'
        os.system(cmdStr)
        time.sleep(1)
        with open(site_TXT, 'r') as fileRead:
            txtTemplage = fileRead.read().split('\n') 
    
    # difpage: Record the line number with "\x0c" mark
    # lineCount: Record how many line in the file.txt 
    difpage = [] 
    lineCount = 0 
    
    for line in txtTemplage:
        if "\x0c" in line:
            difpage.append(lineCount)
        lineCount += 1 
    
    # first_Line_Number_List: Record the first line number in each page, Given an initial number 0 and delete the last line number        
    # last_Line_Number_List : Record the last line number in each page    
    first_Line_Number_List = [0]
    last_Line_Number_List = []
    for i in difpage:
        first_Line_Number_List.append(i + 1)
        last_Line_Number_List.append(i)
    first_Line_Number_List.pop() 
    
    Title_results = []
    Remark_results_dict = {}  # It's a dictionary    
    
    for j in range(0, len(difpage)):
        # Record the title results
        frontnumber = first_Line_Number_List[j]
        backnumber = last_Line_Number_List[j]
        
        pageRange_0 = txtTemplage[frontnumber : backnumber]
        pageRange = list(filter(lambda x : x != '', pageRange_0))
        
        finalStr = pageRange[0].strip()   # Record: pageRange[0] = page title
        
        if finalStr in Title_results:
            i = 1
            format_Type = "{}@{}"
            while format_Type.format(finalStr, i) in Title_results:
                i += 1
            finalStr = format_Type.format(finalStr, i)
        
        Title_results.append(finalStr)
        #Title_results.append("{}".format(pageRange[0].strip())) 
        
        # Record the remark results
        # No remark results in compare type & 3DPDF (3DPDF Result remark need to use anothor package)
        if OutputType == "PDF" or OutputType == "PDFSep":
            if 'Result remark ' in pageRange:
                remarkStart = pageRange.index('Result remark ')
                remarkEnd = pageRange.index('Copyright (c) 2017 Moldex3D. All rights reserved. ')
                
                if 'Statistics plot ' in pageRange:
                    remarkContentList = pageRange[remarkStart + 3 : remarkEnd]
                else:
                    remarkContentList = pageRange[remarkStart + 2 : remarkEnd]
                
                remark = ''
                for remarkline in remarkContentList:
                    remark = "{}".format(remark + str(remarkline))
                
                Remark_results_dict[pageRange[0].strip()] = remark.strip()  # pageRange[0] = page title
    
    return(Title_results, Remark_results_dict)


# Open PDF and save to txt
def PDF_Save_to_TXT(savePDFLocation, site_TXT, OutputType):
    # Check if PDF file opened
    while Aliases.AcroRd32.wndAcrobatSDIWindow.Exists == 0:
        time.sleep(1)
    time.sleep(5)
    
    correct_savePDFLocation = 'Address: ' + savePDFLocation
    
    # Open the "Save as other..." prompt
    Aliases.AcroRd32.wndAcrobatSDIWindow.WaitProperty("Exists", True, 10000000)
    Aliases.AcroRd32.wndAcrobatSDIWindow.MainMenu.Click("[0]|[7]|[0]")
    msctls_progress32 = Aliases.AcroRd323.dlgSaveAs.WorkerW.ReBarWindow32.AddressBandRoot.msctls_progress32
    msctls_progress32.BreadcrumbParent.ToolbarWindow32.WaitProperty("Exists", True, 10000000)
    time.sleep(1)
    # Write the V_path
    V_path = PDF_Write_Path(savePDFLocation)
    
    # Check if the V_path is the target path. If not, write the V_path again 
    while (V_path != correct_savePDFLocation):
        Log.Message("Inside the loop")
        V_path = PDF_Write_Path(savePDFLocation)
        time.sleep(2)
    
    # Click "Save" from PDF to txt 
    Aliases.AcroRd323.dlgSaveAs.btnSave.ClickButton()
    
    while os.path.exists(site_TXT) == 0: 
        time.sleep(1)
    time.sleep(15)

# Write the V_path
def PDF_Write_Path(savePDFLocation):
    msctls_progress32 = Aliases.AcroRd323.dlgSaveAs.WorkerW.ReBarWindow32.AddressBandRoot.msctls_progress32
    msctls_progress32.BreadcrumbParent.ToolbarWindow32.ClickItemXY("Desktop", 8, 11, False)
    msctls_progress32.ComboBoxEx32.SetText(savePDFLocation)
    msctls_progress32.ComboBoxEx32.ComboBox.Edit.Keys("[Enter]")   
    V_path = msctls_progress32.BreadcrumbParent.ToolbarWindow32.WndCaption   
    return(V_path)


# ------------------------------------------------------------------------------------------------------------------------------------------------
# PowerPoint type checking -----------------------------------------------------------------------------------------------------------------------

def PPT_ReadTemplateRange(List, name, OutputType):
    startPoint = List.index('[{}_{}]'.format(name, OutputType))
    endPoint = List.index('[End_{}_{}]'.format(name, OutputType))
    new_List = [i.strip() for i in List[startPoint + 1 : endPoint]]
    
    return(new_List) 


# Record the PPT result to text
def PPT_RecordItem(OutputType, RunPyPath):
    # Launch PowerPoint.exe to skip the Activate prompt first
    PowerPointEXE = r"C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE"
    subprocess.Popen("\"{}\"".format(PowerPointEXE), shell = True)
    time.sleep(3) 
    if Aliases.POWERPNT.wndNUIDialog.WaitProperty("Exists", True, 10000000):
        time.sleep(1) 
        Aliases.POWERPNT.wndNUIDialog.Close() 
        time.sleep(3)
    
    recordPPT_Process = subprocess.Popen(RunPyPath, stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True, shell = True) 
    (output, error) = recordPPT_Process.communicate(OutputType) 
    recordPPT_Process.terminate()  
    return(output)


def PPT_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address):
    # Read project name
    projectName = os.path.basename(Site_Project)
    
    # Read Module item from ppt_template.ini
    with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\ppt_template.ini", "r") as template_AllModule:
        ppt_Template = template_AllModule.read().split('\n') 
    title_ini_List = PPT_ReadTemplateRange(ppt_Template, projectName, OutputType)
    
    for ID in RunIDList:
        # Step 0: Read [*ppt].txt & set the range of each page & read the shape_count ----------------------------
        # Read all content list from ppt result
        with open(r"{}\Report\PPT Report\Run{runID}\PPT Report-Run{runID}.txt".format(Site_Project, runID = ID), "r") as result_Content:
            ppt_Content = result_Content.read()
        ppt_List = ppt_Content.split('\n')
        
        # Collect the "Page_Title" index
        shape_First_Line_index_List = []
        for line in range(len(ppt_List)):
            if "Page_Title : " in ppt_List[line]:
                shape_First_Line_index_List.append(line)
        
        # Collect the first "empty line" index based on the "Page_Title" index
        shape_Last_Line_index_List = []
        for index in shape_First_Line_index_List:
                number = index
                while ppt_List[number] != "":
                    number += 1
                shape_Last_Line_index_List.append(number)
        
        # The page counts we want to check in the PPT file
        shape_Count = len(shape_First_Line_index_List)
        
        # STEP 1: Check item (PPT & PPTComp) ---------------------------------------------------------------------
        # Select those string named as "Page_Title"
        title_List = []
        for line in ppt_List:
            if "Page_Title : " in line:
                title_Name = line.split(": ")[-1]
                
                # If there is the same name in the title_List, add "_@" symbol in the end of the name
                if title_Name in title_List:
                    i = 1
                    format_Type = "{}_@{}"
                    while format_Type.format(title_Name, i) in title_List:
                        i += 1
                    title_Name = format_Type.format(title_Name, i)
                title_List.append(title_Name.strip())
        
        # Title compare
        ini_errorItemSet = list(set(title_ini_List) - set(title_List))
        ppt_errorItemSet = list(set(title_List) - set(title_ini_List))
        
        if ini_errorItemSet != [] or ppt_errorItemSet != []:
            if ini_errorItemSet != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} ini excess title: {}".format(ID, ini_errorItemSet), "Message")
            if ppt_errorItemSet != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} ppt excess title: {}".format(ID, ppt_errorItemSet), "Message")
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} item check Failed !".format(ID), "Error")
        
        # STEP 2: Check remark (PPT only) ---------------------------------------------------------------------
        if OutputType == "PowerPoint":
            # Read Module remark from ppt_remark.ini (Compare don't exist remark)
            with open(r"C:\WorkingFolder\CommonFiles\RPT_Files\ppt_remark.ini", "r") as template_remark_AllModule:
                ppt_Remark = template_remark_AllModule.read().split('\n')
            remark_ini_List = PPT_ReadTemplateRange(ppt_Remark, projectName, OutputType)
            
            # Scan the all objects page by page, and pick up the page_title & Item_remark if remark exists
            title_Remark_List = []
            for page in range(0, shape_Count, 1):
                shape_List = ppt_List[shape_First_Line_index_List[page] : shape_Last_Line_index_List[page]]
                
                remark_Exist = 0
                for line in shape_List:
                    if "Page_Title : " in line:
                        title = line.split(": ")[-1]
                    if "Item_remark : " in line:
                        remark = line.split(": ")[-1]
                        remark_Exist = 1
                
                if remark_Exist == 1:
                    title_Remark_List.append("{} = {}".format(title.strip(), remark.strip()))
            
            # Remark compare
            ini_errorRemarkSet = list(set(remark_ini_List) - set(title_Remark_List))
            ppt_errorRemarkSet = list(set(title_Remark_List) - set(remark_ini_List))
            
            if ini_errorRemarkSet != [] or ppt_errorRemarkSet != []:
                if ini_errorRemarkSet != []:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} ini excess remark: {}".format(ID, ini_errorRemarkSet), "Message")
                if ppt_errorRemarkSet != []:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} ppt excess remark: {}".format(ID, ppt_errorRemarkSet), "Message")
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} remark check Failed !".format(ID), "Error")
        
        # STEP 3: Check result_table (PPT & PPTComp) ------------------------------------------------------------------
        #         Check result_picture (PPT & PPTComp) ----------------------------------------------------------------
        #         Check statistic_plot (PPT only) ---------------------------------------------------------------------
        missing_item_table_List = []
        missing_item_pic_List = []
        missing_item_stat_List = []
        missing_item_stat_pic_List = []
        
        for page in range(0, shape_Count, 1):
            shape_List = ppt_List[shape_First_Line_index_List[page] : shape_Last_Line_index_List[page]]
            
            shape_Content = ""
            for line in shape_List:
                shape_Content = "{}\n{}".format(shape_Content, line)
            
            step_title = shape_List[0].split(" : ")[-1]  # Ex: Filling - Pressure
            
            # Check 'Summary' analysis step
            if (step_title == "Summary") or ("Summary - " in step_title):
                # Check if result_table exist
                patten = r"Table_name : [0-9][.][0-9][.] {}\n".format(step_title.replace("Summary", "Summary table"))
                try:
                    table_Name = re.search(patten, shape_Content).group().split(" : ")[-1].strip()
                except:
                    missing_item_table_List.append(step_title)
                
                # Check if result_picture exist
                if "Table_object : {}__Table".format(table_Name) not in shape_List:
                    missing_item_pic_List.append(step_title) 
                
                # Compare type bonus check runID string
                if OutputType == "PowerPointComp":
                    for i in range(1, 5, 1):
                        if "Table_text : Run0{}".format(i) not in shape_List:
                            missing_item_table_List.append("{}_Run0{}".format(step_title, i))
            
            # Check 'Material figure' (PPT only) ----------------------------------------------
            elif ("Material figures" in step_title) and (OutputType == "PowerPoint"): 
                material_item_List = []
                for line in shape_List:
                    if "Table_name : " in line:
                        material_item_List.append(line.split(" : ")[-1])
                
                if len(material_item_List) < 1:
                    missing_item_table_List.append(step_title)
                
                for i in material_item_List:
                    if "Table_object : {}__Picture".format(i) not in shape_List:
                        missing_item_pic_List.append("{}__Picture".format(i))
            
            # Check shapes besides 'Summary' & 'Material figure' analysis step (PPT only)
            elif (OutputType == "PowerPoint"):
                title = step_title.split(" - ")[-1].replace(" (Animation)", "")  # Ex: Pressure
                
                # Check if result_table & result_picture exist
                if "Table_name : {}".format(title) not in shape_List:
                    missing_item_table_List.append(step_title)
                if "Table_object : {}__Picture".format(title) not in shape_List:
                    missing_item_pic_List.append(step_title)
                
                # Check if statistic_plot exist 
                if (title in noStatPlot_List) or ("Process - " in step_title) or ("XY_" in step_title):
                    pass
                elif ("Melt Front Time" in step_title) and ("% )" in step_title):
                    pass
                elif ("Model - " in step_title) and ("Thickness" not in step_title):
                    pass
                else:
                    if "Table_name : Statistics plot" not in shape_List:
                        missing_item_stat_List.append(step_title)
                    if "Table_object : Statistics plot__Picture" not in shape_List:
                        missing_item_stat_pic_List.append(step_title)                
            
            # Check shapes besides 'Summary' analysis step (PPTComp only) ----------------------------------------------
            elif (OutputType == "PowerPointComp"): 
                title = step_title.split(" - ")[-1].replace(" (Animation)", "")  # Ex: Pressure
                
                for i in range(1, 5, 1):
                    if "Table_name : Run0{}-{}".format(i, title) not in shape_List:
                        missing_item_table_List.append("{}_Run0{}".format(step_title, i))
                    
                    if "Table_object : Run0{}-{}__Picture".format(i, title) not in shape_List:
                        missing_item_pic_List.append("{}_Run0{}__Picture".format(step_title, i))
        
        
        # Log_Message_Error - table_item & table_pic
        if missing_item_table_List != [] or missing_item_pic_List != []:
            if missing_item_table_List != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} missing item_table: {}".format(ID, missing_item_table_List), "Message")
            if missing_item_pic_List != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} missing item_picture: {}".format(ID, missing_item_pic_List), "Message")
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} result check Failed !".format(ID), "Error")
        
        # Log_Message_Error - statistic_item & statistic_plot
        elif missing_item_stat_List != [] or missing_item_stat_pic_List != []:
            if missing_item_stat_List != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} missing statistic table: {}".format(ID, missing_item_stat_List), "Message")
            if missing_item_stat_pic_List != []:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} missing statisitc_picture: {}".format(ID, missing_item_stat_pic_List), "Message")
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} statistic_plot check Failed !".format(ID), "Error")
        
        else:
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} Page_Title check OK.".format(ID), "Message")
            if OutputType == "PowerPoint":
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} Item_Remark check OK.".format(ID), "Message")
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} Item_table & Item_Picture check OK.".format(ID), "Message")
            if OutputType == "PowerPoint":
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} Statistic_table & Statistic_Picture check OK.".format(ID), "Message")


# ------------------------------------------------------------------------------------------------------------------------------------------------
# The main running functions ---------------------------------------------------------------------------------------------------------------------

def LaunchReportWizard( mdxProjPath, OutputType):
    # ProjExePath: MDX Project.exe location
    ProjExePath = "C:\\Moldex3D\\R16\\Bin\\MDXProject.exe"
    
    # backupInfo_Address: The backup & log information file location
    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini"
    
    # Check IE, Office and AdobeReader been installed or not
    softwareCheckResult = SoftwareExeCheck( ProjExePath, OutputType)
    if "isn't installed yet" in softwareCheckResult:
        Log_Message_Error(backupInfo_Address, OutputType, softwareCheckResult, "Error")
    else:
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Check software installed... OK (IE | Office | AdobeReader).", "Message")
    
    # Check if the working VM launch Office once 
    if "PowerPoint" in OutputType:
        checkPPTExeRun_log = Check_PPTExe_Run_Once()
        Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - {}".format(checkPPTExeRun_log), "Message")
    
    # Modify Report Setting Excel file    
    Modify_Report_Setting_Excel()
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Modify Report Setting Excel file... done.", "Message")
    
    # Create msp file
    Create_RPT_MSPFile()
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Create msp file... done.", "Message")
    
    # Modify Moldex3D Project register
    Modify_MDXProject_Reg() 
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Modify Moldex3D Project register... done.", "Message")
    
    # Run MDX Script Wizard
    cmdStr = '\"{}\" \"{}\" + \"{}\"'.format(ProjExePath, mdxProjPath, r"C:\work\RunMDXProj.msp")
    subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Start running script wizard.", "Message")
    
    # Run by report wizard UI
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Start running report wizard by UI.", "Message")
    RunReportUI(mdxProjPath, OutputType)
    
    # Waiting for report file been generated 
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Waiting for report generated...", "Message")
    WaitingForOutput(mdxProjPath, OutputType)
    
    # Stage 1 completed, Backup files & log
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 1 - Report Output completed --------------------", "Message")
    backupPoint = BackupTestingResult(backupInfo_Address, "Py3.4", OutputType, "Stage_1", "")    
    Log_Message_Error(backupInfo_Address, OutputType, backupPoint, "Message")    


def CheckReportOutputResult(Site_Project, OutputType):
    # Search the set of runID in the TestCase Project
    if "Comp" in OutputType:
        RunIDList = ["01"] 
    else:
        RunIDList = AutoReadRunID(Site_Project)
    
    # Read project name
    projectName = os.path.basename(Site_Project)
    
    # Read project analysize_step
    analysize_step = GetAnalysizeStep(projectName)   
    
    # Backup & log information location
    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini"
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Start check report output result.", "Message")
    
    # HTML & HTMLComp
    if "HTML" in OutputType:
        # Check if the summary report output exist
        site_index = r"{}\Report\HTML Report\Report_index.htm".format(Site_Project)
        site_reportTree = r"{}\Report\HTML Report\Report_report_tree.htm".format(Site_Project)
        
        if os.path.exists(site_index) == 0 or os.path.exists(site_reportTree) == 0:
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Summary report missing !", "Error")
        else:
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Summary report exist.", "Message")
        
        # Read project html_step
        htmlReport_step = Change_Step_To_HTMLStep(projectName, analysize_step) 
        
        # Check if the individual report exist
        for ID in RunIDList:
            for resultname in htmlReport_step:
                site_SingleReport = r"{}\Report\HTML Report\Run{}\Run{}.htm".format(Site_Project, ID, ID + resultname)
                if os.path.exists(site_SingleReport) == 0:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} HTML report missing !".format(ID + resultname), "Error")
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} HTML report all exist.".format(ID), "Message")
        
        # Record all items from HTML
        RunPyPath = r"C:\WorkingFolder\CommonFiles\PythonScript\RPT_HTMLRecorder_py27.py"
        HTML_RecordItem(OutputType, RunPyPath) 
        
        # Check item in each step & each run
        if OutputType == "HTML":
            HTML_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address)
        elif OutputType == "HTMLComp":
            HTML_Comp_Check_Item(Site_Project, OutputType, backupInfo_Address)
    
    
    # PPT & PPTComp
    elif "PowerPoint" in OutputType:
        for ID in RunIDList:
            site_PPT = r"{}\Report\PPT Report\Run{runID}\PPT Report-Run{runID}.ppt".format(Site_Project, runID = ID)
            if os.path.exists(site_PPT) == 0:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PPT report output missing!".format(ID), "Error")
            else:
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PPT report output exist!".format(ID), "Message")
        
        # Shut down all the PPT process
        cmdStr = '"taskkill /f /im POWERPNT.EXE"'
        os.system(cmdStr) 
        
        # Record all items from PPT
        RunPyPath = r"C:\WorkingFolder\CommonFiles\PythonScript\RPT_PPTRecorder_py27.py" 
        recordResult = PPT_RecordItem(OutputType, RunPyPath) 
        if "Error !" in recordResult:
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - {}".format(recordResult), "Error")
        else:
            Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - {}".format(recordResult.replace("\n", "")), "Message")	
        
        # Check PPT result
        PPT_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address)
    
    
    # PDF type
    elif AutoChangeOutputTypeName(OutputType) == "PDF":
        for ID in RunIDList:
            if "Sep" not in OutputType:
                site_PDF = r"{}\Report\PDF Report\Run{runID}\PDF Report-Run{runID}.pdf".format(Site_Project, runID = ID)
                if os.path.exists(site_PDF) == 0:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PDF report output missing!".format(ID), "Error")
                else:
                    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PDF report output exist!".format(ID), "Message") 
            
            else:
                for ResultName in analysize_step:
                    site_PDF = r"{}\Report\PDF Report (Separated)\Run{}\PDF Report (Separated)-Run{}.pdf".format(Site_Project, ID, ID + ResultName)
                    if os.path.exists(site_PDF) == 0:
                        Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PDF report output missing !".format(ID + ResultName), "Error")
                Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Run{} PDF report output all exist.".format(ID), "Message") 
        
        # PDF Type check each page title (PDF, 3DPDF, PDFSep also check result remark)
        cmdStr = '"taskkill /f /im AcroRd32.exe"'
        os.system(cmdStr)
        PDF_Check_Item(OutputType, Site_Project, backupInfo_Address)
    
    
    # Stage 2 completed, Backup files & log
    Log_Message_Error(backupInfo_Address, OutputType, "Stage 2 - Check output result completed --------------------", "Message")
    backupPoint = BackupTestingResult(backupInfo_Address, "Py3.4", OutputType, "Stage_2", "")    
    Log_Message_Error(backupInfo_Address, OutputType, backupPoint, "Message")


if __name__ == '__main__':
    
    Site_Project = r"C:\WorkingFolder\testCase\testModel\SolidBiIM"
    
    #OutputType = "HTML"
    OutputType = "PowerPointComp"
    
    if "Comp" in OutputType:
        RunIDList = ["01"]
    else:
        RunIDList = AutoReadRunID(Site_Project)
    
    backupInfo_Address = r"C:\WorkingFolder\testCase\testModel\backUp_Information.ini"
    
    #HTML_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address)
    PPT_Check_Item(Site_Project, OutputType, RunIDList, backupInfo_Address)
    