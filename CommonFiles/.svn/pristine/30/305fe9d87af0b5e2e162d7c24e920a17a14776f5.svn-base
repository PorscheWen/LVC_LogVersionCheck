ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

with open(ModelPath + r"\ModelInfo.txt","r") as file:
    data = file.read().split("\n")
    ModelName = data[0]#[:len(data[0])-8]
    Meshtype = data[1]
        
def Main():
    Delay(1*sec)
    OpenApp()
    Delay(1*sec)
    if Meshtype == "eDN" or Meshtype == "BLM":
        ChooseMeshMethod()
        Delay(1*sec)
        ImportMdgFile_DSN()
        Delay(1*sec)
        if Meshtype == "eDN":
            Re_Generate()
        SaveMesh()
        CloseTestApps(Aliases.MDXDesigner.wndAfx2)
    elif "Rhino" in Meshtype:
        ImportMdgFile_Rhino()
        Delay(1*sec)
        SaveMesh_Rhino()
        Delay(1*sec)
        CloseTestApps(Aliases.Rhino.wndAfx)
    else:
        Log.Error("Read Meshtype Failed")

def OpenApp():
    if Meshtype == "eDN" or Meshtype == "BLM":
        app = TestedApps.MDXDesigner
    elif "Rhino" in Meshtype:
        app = TestedApps.Rhino
    app.Run()
    
def ChooseMeshMethod():
    wr = Aliases.MDXDesigner.ChooseMode.MeshingMethod.WaitProperty("Visible",True,3*sec)
    if wr == False:
        Log.Error("")
    if Meshtype == "eDN":
        Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.ClickButton()
        Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.Keys(" ")
    elif Meshtype == "BLM":
        Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_BLM.ClickButton()
        Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_BLM.Keys(" ")
    Aliases.MDXDesigner.ChooseMode.btn_OK.ClickButton()
    
def ImportMdgFile_DSN():
    Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.btn_Import.ClickButton()
    Log.Message(ModelPath + "\\" + ModelName + "(m).mdg")
    if Meshtype == "eDN":
        Aliases.MDXDesigner.dlgOpen.OpenFile(ModelPath + "\\" + ModelName, "All types of files (*.mdg;*.stl;*.igs; *.iges;*.stp; *.step;*.x_t; *.x_b;*.mdxpf;*.x_t;*.x_b)")
    elif Meshtype == "BLM":
        Aliases.MDXDesigner.dlgOpen.OpenFile(ModelPath + "\\" + ModelName, "All types of files (*.mdg;*.igs; *.iges;*.stp; *.step;*.3dm;*.x_t; *.x_b;*.mdxsf;*.jt;*.prt;*.prt;*.prt.*;*.catpart;*.x_t;*.x_b)")
    CheckMsgWnd("have been loaded")
    Log.Message("Import Mdg File Complete")
    
def Re_Generate():
    #Project.Variables.AddVariable("MyExportFilePath", "String")
    Aliases.MDXDesigner.wndAfx2.MDIClient.wndAfxFrameOrView120u.AfxFrameOrView120u.Keys("^4")
    Aliases.MDXDesigner.wndAfx2.GUIView.GUIView.GUIView.Keys("^4")
    Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step4.inTool.Meshing.btn_Generate.ClickButton()
    # check defect dlg:
    if Aliases.MDXDesigner.WaitAliasChild("ExportSuccess", 1*sec).Exists:
        if Aliases.MDXDesigner.ExportSuccess.WaitAliasChild("dlgInfo", 1*sec).Exists:
            Aliases.MDXDesigner.ExportSuccess.btn_defectNo.ClickButton()
        else:
            Log.Error("Unexpect dlg Apear")
    Aliases.MDXDesigner.ExportSuccess.btn_defectNo
    wr = Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step4.MeshingLV.btn_GreenCheck.WaitProperty("Visible",True,3*1000)
    if wr == True:
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step4.MeshingLV.btn_GreenCheck.ClickButton()
    CheckMsgWnd("Generate Solid Mesh...... done")
    Log.Message("Generate Mesh Complete")
    
def SaveMesh():
    Aliases.MDXDesigner.wndAfx2.MDIClient.wndAfxFrameOrView120u.AfxFrameOrView120u.Keys("^5")
    Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step5.inTool.Export.btn_SaveMeshFile.ClickButton()
    if Meshtype == "eDN":
        Aliases.MDXDesigner.dlgSaveAs.SaveFile("C:\\WorkingFolder\\testCase\\testModel\\%s.mde" % ModelName[:-7], "Moldex3D eDesign mesh file (*.mde)")
    elif Meshtype == "BLM":
        Aliases.MDXDesigner.dlgSaveAs.SaveFile("C:\\WorkingFolder\\testCase\\testModel\\%s.mfe" % ModelName[:-7], "Moldex3D solid mesh file (*.mfe)")
    Aliases.MDXDesigner.ExportSuccess.btn_Close.WaitProperty("Exists",True,60*1000)
    Aliases.MDXDesigner.ExportSuccess.btn_Close.ClickButton()
    Log.Message("Save Mesh Complete")
    
def CheckMsgWnd(CheckStr):
    if "Rhino" in Meshtype:
        MsgWndObj = Aliases.Rhino.wndAfx.ControlBar.MsgWnd.MsgContent
    else:
        MsgWndObj = Aliases.MDXDesigner.wndAfx2.File.MsgWnd.MsgContent
    MsgResult = aqObject.GetPropertyValue(MsgWndObj,"wText")
    while CheckStr not in MsgResult:
        Delay(1*sec)
        MsgResult = aqObject.GetPropertyValue(MsgWndObj,"wText")
    Log.Message(MsgResult)
    Log.Message("Check Message [%s] Complete" % CheckStr)
    
def ImportMdgFile_Rhino():
    Aliases.Rhino.wndAfx.WaitProperty("Exists", True, 60*sec)
    Aliases.Rhino.wndAfx.WaitProperty("Visible", True, 60*sec)
    Aliases.Rhino.wndAfx.Maximize()
    CheckMsgWnd("is already open.")
    Aliases.Rhino.wndAfx.ControlBar.ToolBar.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.click(41,13)
    Aliases.Rhino.dlgOpen.OpenFile(ModelPath + "\\" + ModelName, "All compatible file types (*.*)")    
    CheckMsgWnd("successfully read")
    Log.Message("Import 3dm File Complete")


def SaveMesh_Rhino():
    Aliases.Rhino.wndAfx.ControlBar.ToolBar.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.Click(573, 12)
    if "3D" in Meshtype:
        # Export Solid Mesh
        if "FC" in Meshtype:
            Aliases.Rhino.wndAfx.Rhinoceros.MDXToolbar_Solid.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.ClickR(10, 572)
        elif "SC" in Meshtype or "noMB" in Meshtype:
            Aliases.Rhino.wndAfx.Rhinoceros.MDXToolbar_Solid.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.Click(10, 572)
        Aliases.Rhino.dlgSaveAs.btnSave.ClickButton()
        if "noMB" in Meshtype: 
            if "X-Axis" in Meshtype:
                Aliases.Rhino.PartingDirectionSetting.Axis.ClickItem("X Axis")
            elif "Y-Axis" in Meshtype:
                Aliases.Rhino.PartingDirectionSetting.Axis.ClickItem("Y Axis")
            elif "Z-Axis" in Meshtype:
                Aliases.Rhino.PartingDirectionSetting.Axis.ClickItem("Z Axis")
            Aliases.Rhino.PartingDirectionSetting.btn_OK.ClickButton()            
    elif "2D" in Meshtype:
        # Export Shell Mesh
        Aliases.Rhino.wndAfx.Rhinoceros.MDXToolbar_Shell.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.Click(13, 433)
        Aliases.Rhino.dlgSaveAs.btnSave.ClickButton()
        if "noMB" in Meshtype:
            #Mesh do not contain Moldbase
            Aliases.Rhino.PartingDirectionSetting.btn_OK.ClickButton()            
            Aliases.Rhino.ExportSuccess.btnYes.ClickButton()
        elif "FC" in Meshtype:
            # Export Shell Mesh
            pass
    wr = Aliases.Rhino.WaitAliasChild("ExportSuccess", 120*sec)
    #wr = Aliases.Rhino.ExportSuccess.btn_OK.WaitProperty("Visible",True,60*sec)
    if wr.Exists:
        Log.Message("Save Mesh Complete")
        wr = Aliases.Rhino.ExportSuccess.WaitAliasChild("btn_OK", 120*sec)
        if wr.Exists:
            Aliases.Rhino.ExportSuccess.btn_OK.ClickButton()
    else:
        Log.Error("Save Mesh Failed")
        
def WaitObjectVisible(Obj):
    wr = Obj.WaitProperty("Exists",True,1*sec)
    while wr != True:
        wr = Obj.WaitProperty("Exists",True,1*sec)
    wr = Obj.WaitProperty("Visible",True,1*sec)
    while wr != True:
        wr = Obj.WaitProperty("Visible",True,1*sec)
    Log.Message("Object appear")
      
def CloseTestApps(Obj):
    Obj.Close()
    Log.Message("")
    

def Test1():
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.ClickButton()
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.Keys(" ")

def Test2():
    Aliases.Rhino.wndAfx.Rhinoceros.MDXToolbar_Solid.CDotNetControlBar.ControlAxSourcingSite.ToolBarGroupDockBarControl.ToolBarGroupControl.ToolBarControl.ClickR(13, 548)
