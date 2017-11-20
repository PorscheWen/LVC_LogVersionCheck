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
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.ClickItem("Filling/Packing :  *")
        Aliases.MDXProject.wndCMX.pageFlowPack.SysListView32.btnEdit.ClickButton()    
        l = dicType.get("FP")
        Log.Message(l)
        if l != None:
            #tTotal = dicType["FP"][0] 
            ts1 = dicType["FP"][1]
            ts2 = dicType["Foaming"][1]
        Aliases.MDXProject.dlgDataEditor.SysListView32.ClickItem("%s Stage [0~*" % ("Filling/Packing"), "3")
        Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.SetText(str(ts1))
        Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.Keys("[Enter]")
        Aliases.MDXProject.dlgDataEditor.SysListView32.ClickItem("%s Stage [*" % ("Foaming"), "3")
        Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.SetText(str(ts2))
        Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.Keys("[Enter]")
        Aliases.MDXProject.dlgDataEditor.btn_OK.ClickButton()
        
class TabCool:
    
    def __init__(self):
        Aliases.MDXProject.wndCMX.SysTabControl32.ClickTab("Cool")
        
    def Set_TimeStep(self, **dicType):
        def Action():
            Aliases.MDXProject.wndCMX.pageCool.SysListView32.ClickItem("%s :  3" % str(Type), 0)
            Aliases.MDXProject.wndCMX.pageCool.SysListView32.btnEdit.ClickButton()
            Aliases.MDXProject.dlgDataEditor.SysListView32.ClickItem("%s [0~%s] sec" % (str(Type), str(tTotal)), "3")
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.SetText(str(ts))
            Aliases.MDXProject.dlgDataEditor.SysListView32.Edit.Keys("[Enter]")
            Aliases.MDXProject.dlgDataEditor.btn_OK.ClickButton()
        tupParaKey = ("Cooling", "Opening")
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