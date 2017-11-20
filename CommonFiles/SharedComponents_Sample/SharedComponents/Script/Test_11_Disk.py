import ProPara_ICM
import CMXPara_ICM
sec = 1000


def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting:
        ProPara_ICM.CAE_MaxPressure(300, 300)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_ICM.FlowPackTime(0.6, ("Yes", 5))
        ProPara_ICM.tpMeltMoldTemp(190, 55)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfFR = ProPara_ICM.ProfileSetting("FlowRate")
        pfFR.Set_CAEProfile(tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfIjPr = ProPara_ICM.ProfileSetting("InjactionPressure")
        pfIjPr.Set_CAEProfile(tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCompress():
        cm = ProPara_ICM.Compression()
        cm.Set_ClickItem(("CompressionRegion (0.00,0.00,1.00)", 1))
        cm.Set_Value((0.1, 0.25, 90.1074, 0, 10, 60))
        tupTime = (0.1, 0)
        tupValue = (5, 5)
        pfSpd = ProPara_ICM.ProfileSetting("Speed")
        pfSpd.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Compression speed (mm/sec) vs. Compression Time (sec)")
        tupTime = (0.1, 0)
        tupValue = (60, 60)
        pfF = ProPara_ICM.ProfileSetting("Force")
        pfF.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Compression force (tf) vs. Compression Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_ICM.CoolPara(MBFlag=1, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=89.1)
        CoolAdv = ProPara_ICM.CoolPara_Adv()
        CoolAdv.MoldMetalMTR(1, "P20")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_Summary():
        # Summary
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFP()
    SubStage_SetCompress()
    SubStage_SetCool()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_ICM.TabFlowPack()
    cmxFP.Set_TimeStep(FP=[0.1 + 0.1, 0])
    cmxC = CMXPara_ICM.TabCool()
    cmxC.Set_TimeStep(Cooling=[20, 0], Opening=[5, 0])
    cmxTask = CMXPara_ICM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()
