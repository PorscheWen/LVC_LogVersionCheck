ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

class TabFlowPack:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Flow/Pack")    
    
    def Set_Solver(Self, Solver):
        Aliases.MDXProject.wndCMX.pageFlowPack.Solver.ClickItem(Solver)
        
    def Set_Analysis(self, AnalysisType):
        dicAnalysis = {
            "Standard" : lambda: Aliases.MDXProject.wndCMX.pageFlowPack.Customize.ClickButton(),
            "Fast"     : lambda: Aliases.MDXProject.wndCMX.pageFlowPack.FastAnalysis.ClickButton(),
            "Customize": lambda: Aliases.MDXProject.wndCMX.pageFlowPack.FastAnalysis.ClickButton()
        }.get(AnalysisType)()
        
    def Set_Thickness(self, Thickness):    
        Aliases.MDXProject.wndCMX.pageFlowPack.Thickness.SetText(Thickness)
        
    def Set_TimeStep(self, **dicType):
        def Action():
            Aliases.MDXProject.dlgDataEditor.SysListView32.ClickItem("%s Analysis [0~%s] sec" % (str(Type), str(tTotal)), "3")
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.SetText(str(ts))
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.Keys("[Enter]")
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Setting Method: Filling Time (sec)", 0)
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.btnEdit.ClickButton()
        tupParaKey = ("Filling", "Packing")
        for k in tupParaKey:
            l = dicType.get(k)
            Log.Message(l)
            if l != None:
                Type = k
                tTotal = dicType[k][0]
                ts = dicType[k][1]
                Action()
        Aliases.MDXProject.dlgDataEditor.btn_OK.ClickButton()
        
class TabCool:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Cool")
        
    def Set_TimeStep(self, **dicType):
        def Action():
            Type_space = aqString.Replace(Type, "_", " ")
            Aliases.MDXProject.wndCMX.pageCool.SysListView32.ClickItem("%s :  3" % str(Type_space), 0)
            Aliases.MDXProject.wndCMX.pageCool.SysListView32.btnEdit.ClickButton()
            Aliases.MDXProject.dlgDataEditor.SysListView32.ClickItem("%s [0~%s] sec" % (str(Type_space), str(tTotal)), "3")
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.SetText(str(ts))
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.Keys("[Enter]")
            Aliases.MDXProject.dlgDataEditor.btn_OK.ClickButton()
        tupParaKey = ("Cooling", "Opening", "Mold_preheating")
        for k in tupParaKey:
            l = dicType.get(k)
            Log.Message(l)
            if l != None:
                Type = k
                tTotal = dicType[k][0]
                ts = dicType[k][1]
                Action()
                
class TabWarp:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Warp")
        
class TabTask:
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Task Manager")
    
    def Set_TaskNo(self, numCPU):
        Aliases.MDXProject.wndCMX.pageTask.No.SetText(str(numCPU))
        
        
class TabStress:
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Stress")

    def Set_SBC(self):
        Aliases.MDXProject.wndCMX.pageStress.SysListView32.ClickItem("Stress boundary condition : (Edit...)", 0)
        Aliases.MDXProject.wndCMX.pageStress.SysListView32.btnEdit.ClickButton()
        
class StressBC:

    def __init__(self):
        CheckStr = "< Edit stress boundary condition >"
        MsgWndObj = Aliases.MDXDesigner.wndAfx2.File.MsgWnd.MsgContent
        MsgResult = aqObject.GetPropertyValue(MsgWndObj,"wText")
        i = 0
        while CheckStr not in MsgResult:
            i += 1
            Delay(1*sec)
            MsgResult = aqObject.GetPropertyValue(MsgWndObj,"wText")
            if i > 60:
                Log.Error("Wait [%s] time out" % CheckStr)
        Log.Message("Check Message [%s] Complete" % CheckStr)
        
        Aliases.MDXDesigner.wndAfx2.File.Graphics.CheckItem(45042, False, False)

    def add_Force(self):
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.btn_Import.ClickButton()

    def add_Pressure(self):
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.btn_Pressure.ClickButton()

    def add_Displacement(self):
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.btn_Displacement.ClickButton()

    def zoom_In(self, OriXY, RegionXY):
        # Fit to window, reset view region
        Aliases.MDXDesigner.wndAfx2.File.ToolbarWindow32.ClickItem(45025, False)
        Aliases.MDXDesigner.wndAfx2.File.ToolbarWindow32.ClickItem(45025, False)
        # Click Zoom In Icon
        Aliases.MDXDesigner.wndAfx2.File.ViewOption.CheckItem(45024, True, False)
        Aliases.MDXDesigner.wndAfx2.GUIView.GUIView.GUIView.Drag(OriXY[0], OriXY[1], RegionXY[0], RegionXY[1])

    def click_Mesh(self, XY):
        GUIViewobj = Aliases.MDXDesigner.wndAfx2.GUIView.GUIView.GUIView
        GUIViewobj.Click(XY[0], XY[1], skShift)

    def modify_fz(self, valF):
        obj = Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Afx.Property.Fz
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.LdandBC.ClickItem("|Loads|force1")
        obj.Click(80, 10)
        obj.SetText(str(valF))
        self.check_val(obj, valF)

    def modify_pr(self, valP):
        obj = Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Afx.Property.Pr
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.inTool.Import.LdandBC.ClickItem("|Loads|pressure1")
        obj.Click(80, 10)
        obj.SetText(str(valP))
        self.check_val(obj, valP)

    def check_Add(self):
        Aliases.MDXDesigner.wndAfxSBC.btn_OK.ClickButton()
        
    def close_DSNSBC(self):
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.EditSBC.btn_OK.ClickButton()
        Aliases.MDXDesigner.ExportSuccess.btn.ClickButton()
        
    def check_val(self, obj , valInput):
        strUIShow = aqObject.GetPropertyValue(obj, "wText")
        if strUIShow != str(valInput):
            Log.Error("Value UI Shown is not eq. to Value TC Input ")        
