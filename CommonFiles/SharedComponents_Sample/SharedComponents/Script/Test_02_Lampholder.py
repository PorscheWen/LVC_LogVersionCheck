import ProPara_RIM
import CMXPara_RIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_RIM.CAE_MaxPressure(142, 142)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_RIM.FlowCureTime(7, 40)
        ProPara_RIM.tsMeltMoldTemp(30, 155, 0)
        ProPara_RIM.VPSwitch(98)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfFR = ProPara_RIM.ProfileSetting("FlowRate")
        pfFR.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Flow Rate (%) vs. Time (%)")
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfIP = ProPara_RIM.ProfileSetting("InjactionPressure")
        pfIP.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Injection Pressure (%) vs Time (%)")
        tupTime = (40, 0)
        tupValue = (100, 100)
        pfCrPr = ProPara_RIM.ProfileSetting("CurePressure", "Curing pressure refers to end of filling pressure")
        pfCrPr.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Curing pressure (%) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_RIM.CoolPara(MBFlag=0, tMBOpen=5, AirTemp=25)     
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_Summary():
        # Summary
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFP()
    SubStage_SetCool()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFC = CMXPara_RIM.TabFlowPack()
    cmxFC.Set_TimeStep(Filling=[7, 0], Curing=[40, 0])
    cmxC = CMXPara_RIM.TabCool()
    cmxC.Set_TimeStep(Opening=[5, 0], Mold_preheating=["*", 0])
    cmxC.Set_Solver()
    cmxTask = CMXPara_RIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()