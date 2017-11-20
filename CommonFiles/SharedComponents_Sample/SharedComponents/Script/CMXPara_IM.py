ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

class TabFlowPack:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Flow/Pack")    
    
    def Set_Solver(Self, Solver):
        Aliases.MDXProject.wndCMX.pageFlowPack.Solver.ClickItem(Solver)

    def Set_Analysis(self, AnalysisType, check=[]):
        dicAnalysis = {
            "Standard" : lambda: Aliases.MDXProject.wndCMX.pageFlowPack.StandardAnalysis.ClickButton(),
            "Fast"     : lambda: Aliases.MDXProject.wndCMX.pageFlowPack.FastAnalysis.ClickButton(),
            "Customize": lambda: Aliases.MDXProject.wndCMX.pageFlowPack.Customize.ClickButton()
        }.get(AnalysisType)()
        if check:
            Aliases.MDXProject.wndCMX.pageFlowPack.checkStabilizedCalculation.ClickButton(check[0])
            Aliases.MDXProject.wndCMX.pageFlowPack.checkNonisothermal.ClickButton(check[1])
            Aliases.MDXProject.wndCMX.pageFlowPack.checkStabilizedCalculation.ClickButton(check[2])
            Aliases.MDXProject.wndCMX.pageFlowPack.checkNonnewtonianFlow.ClickButton(check[3])
            Aliases.MDXProject.wndCMX.pageFlowPack.checkCompressibleFlow.ClickButton(check[4])

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
        
    def Check_ExtendPack(self, relativeXY):
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Extend Packing Calculation to cooling phase", 0)
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.Click(relativeXY[0], relativeXY[1])
    
    def Check_ParticleTracer(self, relativeXY1=None, relativeXY2=None):
        if relativeXY1:
            Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Particle tracking from : ...", 0)
            Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.Click(relativeXY1[0], relativeXY1[1])
        if relativeXY2:
            Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Weld line particle", 0)
            Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.Click(relativeXY2[0], relativeXY2[1])

    def Check_CrystallEffect(self, relativeXY):
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Consider crystallization effect", 0)
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.Click(relativeXY[0], relativeXY[1])

class AdvancedFlowPack:
    def __init__(self):
        Aliases.MDXProject.wndCMX.pageFlowPack.Advanced.ClickButton()

    def Set_TabAccuracy(self, sType, iCustom=None):
        Aliases.MDXProject.dlgAdvancedFPSolver.SysTabControl32.ClickTab("Accuracy/Performance")
        obj = Aliases.MDXProject.dlgAdvancedFPSolver.SysTabControl32.pageAccuracy
        dicOption = {
            "Default": lambda: obj.Default.ClickButton(),
            "Accurate": lambda: obj.Accurate.ClickButton(),
            "Customized": lambda: obj.Customized.ClickButton()
            }.get(sType)()
        if iCustom:
            obj.Edit.SetText(str(iCustom))
        Aliases.MDXProject.dlgAdvancedFPSolver.btn_OK.ClickButton()

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

    def Set_Solver(self, iMaxCyc=10, Criteria="Maximum variation of mold temperature", StdValue=["ByTempDiff", 1]):
        Aliases.MDXProject.wndCMX.pageCool.SysListView32.ClickItem("Solver parameters*", 0)
        Aliases.MDXProject.wndCMX.pageCool.SysListView32.btn_Edit.ClickButton()
        Aliases.MDXProject.dlgDataEditor.MaxCyc.SetText(str(iMaxCyc))
        Aliases.MDXProject.dlgDataEditor.CriteriaList.ClickItem(Criteria)
        if StdValue[0] == "ByTempDiff":
            Aliases.MDXProject.dlgDataEditor.ByTempDiff.ClickButton()
            Aliases.MDXProject.dlgDataEditor.DiffValue.SetText(str(StdValue[1]))
        elif StdValue[0] == "ByTempDiffRatio":
            Aliases.MDXProject.dlgDataEditor.ByTempDiffRatio.ClickButton()
            Aliases.MDXProject.dlgDataEditor.DiffRatioValue.SetText(str(StdValue[1]))
        Aliases.MDXProject.dlgDataEditor.btn_OK.ClickButton()
              
class TabMCM:
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("MCM")

    def Set_CoreShift(self, Type):
        Aliases.MDXProject.wndCMX.pageMCM.CoreShiftCalculation.ClickButton(cbChecked)
        Aliases.MDXProject.wndCMX.pageMCM.CoreShiftCalculationType.ClickItem(Type)
        Aliases.MDXProject.wndCMX.pageMCM.btn_CoreSettings.ClickButton()

    def Set_PreviousShot(self, iRunNum, sMethod="Current project"):
        Aliases.MDXProject.wndCMX.pageMCM.LinkPreviousShot.ClickButton(cbChecked)
        Aliases.MDXProject.wndCMX.pageMCM.LinkMethod.ClickItem(sMethod)
        Aliases.MDXProject.wndCMX.pageMCM.LinkRun.ClickItem(str("Run0%i" % iRunNum))

class TabWarp:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Warp")

class TabOptics:

    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("VE/Optics")
        self.Obj = Aliases.MDXProject.wndCMX.pageVEOptics

    def Check_ResidualStress(self):
        Aliases.MDXProject.wndCMX.pageVEOptics.SysListView32.Click(11, 34)
        Aliases.MDXProject.wndCMX.pageVEOptics.SysListView32.Click(11, 53)

    def Set_OpticsProperty(self, iID, tupPropagation):
        self.Obj.EstimateOptics.btn_EstimateOptics.ClickButton(cbChecked)
        for i in range(3):
            self.Obj.Propagation.ClickItem(str(iID), i + 1)
            self.Obj.Propagation.Edit.SetText(tupPropagation[i])
            self.Obj.Propagation.Edit.Keys("[Enter]")

    def Set_RunnerEffect(self, isRemoved=True):
        if isRemoved:
            self.Obj.RemoveRunnerEffect.ClickButton(cbChecked)
        else:
            self.Obj.RemoveRunnerEffect.ClickButton(cbUnchecked)
            Aliases.MDXProject.dlgMoldex3D.btn_Yes.ClickButton()

    def Set_Polariscope(self, sField="Dark"):
        if sField == "Dark":
            self.Obj.DarkField.ClickButton()
        elif sField == "Light":
            self.Obj.LightField.ClickButton()

    def Set_WaveLength(self, iLambda=590):
        self.Obj.WaveLength.SetText(str(iLambda))

    def Set_Output3rdSW(self, isOuput=False):
        if not isOuput:
            self.Obj.OutputToOpticalSoftware.ClickButton(cbUnchecked)
        else:
            self.Obj.OutputToOpticalSoftware.ClickButton(cbChecked)

        
class TabTask:
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Task Manager")
    
    def Set_TaskNo(self, numCPU):
        Aliases.MDXProject.wndCMX.pageTask.No.SetText(str(numCPU))

class CoreShitBC:

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
        
    def close_DSNSBC(self):
        wr = Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.EditSBC.btn_OK.WaitProperty("Visible", True, 5*sec)
        Aliases.MDXDesigner.wndAfx2.Workspace.Workspace.Step.Step.Step1.EditSBC.btn_OK.ClickButton()
        Aliases.MDXDesigner.ChooseMode.btn.ClickButton()