﻿ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

with open(ModelPath + r"\NewRunInfo.txt", "r") as file:
    data = file.read().split("\n")
    Remark = data[0]
    MeshName = data[1]
    MaterialList = []
    for i in range(2, len(data)-1):
        MaterialList.append([data[i].split(": ")[0], "|".join(data[i].split(": ")[1].split(", "))])
        
with open(ModelPath + r"\ProjectInfo.txt", "r") as file:
    AppModule = file.read().split("\n")[3]     

def Main(iRunNum = 1):
    NRI = NewRunIni(iRunNum)
    NRI.RunMesh()
    NRI.RunMaterial()
    NRI.RunProcessIni()
    
#Project.Variables.RunNum = "Create a New Run: [Run 1]"
class NewRunIni():
    def __init__(self, iRunNum=1):
        Project.Variables.RunNum = "Create a New Run: [Run %s]" % str(iRunNum)
        if iRunNum != 1:
            Aliases.MDXProject.wndAfx.AfxControlBarLeft.Workspace.SysTabControl32.SysTreeView32.DblClickItem("|*|Double click here to add a new run...")
        
    def RunMesh(self):
        Aliases.MDXProject.dlgRunWizard.WaitProperty("Exists",True,1*sec)
        Aliases.MDXProject.dlgRunWizard.WaitProperty("Visible",True,1*sec)
        #Setting Run Remark
        if Remark != "Null":
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page32770.Edit.SetText(Remark)
        #Run Option -> Run Mesh
        Aliases.MDXProject.dlgRunWizard.btn_Next.Click()
        oItems = Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327701.NewMesh.wItemList
        if MeshName not in str(oItems):
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327701.NewMesh.ClickItem("New")
            if ".msh" in MeshName:
                Aliases.MDXProject.dlgOpen.OpenFile(ModelPath + "\\" + MeshName, "Moldex3D Shell Mesh File (*.msh)")
            elif ".mde" in MeshName:
                Aliases.MDXProject.dlgOpen.OpenFile(ModelPath + "\\" + MeshName, "Moldex3D eDesign Mesh Files (*.mde)*")
            elif ".mfe" in MeshName:
                Aliases.MDXProject.dlgOpen.OpenFile(ModelPath + "\\" + MeshName, "Moldex3D Solid Mesh Files (*.mfe)*")
        else:
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327701.NewMesh.ClickItem(MeshName)
        #Run Mesh -> Run Material
        Aliases.MDXProject.dlgRunWizard.btn_Next.Click()
    
    def RunMaterial(self):
        for m in MaterialList:
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327702.NewMTR.ClickItem(m[0], "---")
            oItems = Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327702.NewMTR.ComboBox.wItemList
            if m[1] not in str(oItems):
                Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327702.NewMTR.ComboBox.ClickItem("New")
                # Launch Material Wizard
                Aliases.MdxMat.wndAfx.Maximize()
                Aliases.MdxMat.wndAfx.AfxFrameOrView120.btn_MDX3DBank.ClickButton()
                Aliases.MdxMat.wndAfx.AfxFrameOrView120.MDX3DBankView.ClickItemR("|" + m[1])
                Aliases.MdxMat.wndAfx.AfxFrameOrView120.PopupMenu.Click("Add to Project")
                Aliases.MdxMat.dlgMoldex3D.btn_OK.ClickButton()
                Aliases.MdxMat.dlgMoldex3D.btn_No.ClickButton()
                Aliases.MdxMat.wndAfx.close()
            else:
                Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327702.NewMTR.ComboBox.ClickItem(m[1])
        #Run Material -> Run Process
        Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
        Aliases.MDXProject.dlgRunWizard.btn_Next.Click()

    def RunProcessIni(self):
        if "RIM" in AppModule:
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327704.NewPro.ClickItem("Create a RIM process file")
            self.Add_NewProcess()
        elif MeshName == "Lampholder.mfe":
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327704.NewPro.ClickItem("Create an injection process file")
            self.Add_NewProcess()
        elif Remark == "Ignore influences from 1st shot":
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327704.NewPro.ClickItem("%s_2.pro" % MeshName[:-13])
        else:    
            Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327704.NewPro.ClickItem("New")
            self.Add_NewProcess()

    def Add_NewProcess(self):
        SimpleMode = Aliases.MdxPro.wndAfx.SysTabControl32.WaitAliasChild("SimpleProcessMode", 3*sec)
        if SimpleMode.Exists:
            ChkProMode = Aliases.MdxPro.wndAfx.SysTabControl32.SimpleProcessMode
            ProModeInfo = aqObject.GetPropertyValue(ChkProMode,"Visible")
            if ProModeInfo == True:
                Aliases.MdxPro.wndAfx.btn_Option.ClickButton()
                Aliases.MdxPro.dlgOption.ProcessMode.ClickItem("Classic Mode")
                Aliases.MdxPro.dlgOption.btn_OK.ClickButton()
                Aliases.MdxPro.dlgMdxpro.btn_Yes.ClickButton()

def Check_Run_Data():  
    REPORTObj = Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327706.REPORT
    RUNDATACHECKINGREPORT = aqObject.GetPropertyValue(REPORTObj, "wText")
    if "=> OK!" not in RUNDATACHECKINGREPORT:
        Log.Error("RUN DATA CHECKING REPORT Failed")
    else:
        Log.Message(RUNDATACHECKINGREPORT)
        Aliases.MDXProject.dlgRunWizard.btn_Finish.ClickButton()