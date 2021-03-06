﻿import re
ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

with open(ModelPath + r"\StatsInfo.txt", "r") as file:
    data = file.read().split("\n")
with open(ModelPath + r"\ProjectInfo.txt", "r") as file:
    ProjectName = file.read().split("\n")[1]

    
class StatsData:

    def __init__(self, RunNume, infoRes):
        self.RunNume = RunNume
        self.resName = infoRes.split(" - ")[0]
        self.lstPhysQty = infoRes.split(" - ")[1].split(", ")
        self.dicStats = {}

    def Collecting(self):
        for PhysQty in self.lstPhysQty:
            if "*" not in PhysQty:
                self.click_ResItem(PhysQty)
                self.dicStats[PhysQty] = self.get_Data()
                self.close_ResultAdvisor()
            else:
                self.dicStats[PhysQty] = self.get_LogFileData(PhysQty)

    def get_Data(self):
        ResAdv = Aliases.MDXProject.dlgResultAdvisor
        valMin = aqObject.GetPropertyValue(ResAdv.Min, "wText")
        valMax = aqObject.GetPropertyValue(ResAdv.Max, "wText")
        valAvg = aqObject.GetPropertyValue(ResAdv.Avg, "wText")
        valSD = aqObject.GetPropertyValue(ResAdv.SD, "wText")
        return valMin, valMax, valAvg, valSD

    def click_ResItem(self, PhysQty):
        itemWorkspace = "|%s*|Run %s*|Result*|%s*|%s" % (
            ProjectName, self.RunNume, self.resName, PhysQty)
        Aliases.MDXProject.wndAfx.AfxControlBarLeft.Workspace.SysTabControl32.SysTreeView32.DblClickItem(
            itemWorkspace)

    def close_ResultAdvisor(self):
        Aliases.MDXProject.dlgResultAdvisor.btnOK.ClickButton()
        
    def get_LogFileData(self, PhysQty):
        LogPathformat = r"{0}\{1}\Analysis\Run01\{1}01.lgf"
        dicPhysQty = {
            "Melt Volume of Cavity*": "Melt Volume of Cavity #1.*=*.cc",
            "Water Volume of Cavity*": "Water Volume of Cavity #1.*=.*cc",
            "Gas Volume of Cavity*": "Gas Volume of Cavity #1.*=.*cc",
            "Clamping Force at EOF*": "Clamping Force at EOF.*=.*Ton"}
        with open(LogPathformat.format(ModelPath, ProjectName), "r") as LogFile:
            LogFileData = LogFile.read()
        patt = dicPhysQty.get(PhysQty)
        r = re.search(patt, LogFileData).group()
        val = re.search("[0-9]*\.[0-9]*", r).group()        
        return val

    def Export_ResultStats(self):
        if "/" in self.resName:
            self.resName = aqString.Replace(self.resName, "/", "_")
        with open(ModelPath + "\\Stats_%s\\" % ProjectName + self.resName + ".txt", "w") as file_stats:
            data_stast = []
            for PhysQty in self.lstPhysQty:
                if "*" not in PhysQty:
                    data_stast.append("%s = %s\n" %
                                      (PhysQty, ", ".join(self.dicStats[PhysQty])))
                else:
                    data_stast.append("%s = %s\n" %
                                      (PhysQty, self.dicStats[PhysQty]))                
            file_stats.writelines(data_stast)


def Collect_Data(RunNume = "1"):
    aqFileSystem.CreateFolder(ModelPath + r"\Stats_%s" % ProjectName)
    for infoRes in data[:-1]:
        Log.Message(infoRes)
        objstats = StatsData(RunNume, infoRes)
        objstats.Collecting()
        objstats.Export_ResultStats()
        
"""
def test():
    with open(r"{0}\{1}\Analysis\Run01\{1}01.lgf".format(ModelPath, "Fishing Buoy"), "r") as f:
        data = f.read()
    
    r = re.search("Water Volume of Cavity #1\s*=[\s0-9\.]*cc", data).group()
    Log.Message(re.search("[0-9]*\.[0-9]*", r).group())
"""
