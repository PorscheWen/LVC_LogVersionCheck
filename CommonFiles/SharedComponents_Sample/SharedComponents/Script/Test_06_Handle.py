import ProPara_IM
import CMXPara_IM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_IM.CAE_MaxPressure(270, 270)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_IM.FlowPackTime(0.9, 4)
        ProPara_IM.tpMeltMoldTemp(250, 45)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        ProPara_IM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_IM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (4, 3.2, 2.4, 0)
        tupValue = (51.2, 64, 80, 80)        
        ProPara_IM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=3)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_IM.CoolPara(MBFlag=0, tCool=13.7, tMBOpen=5, AirTemp=25, EjTemp=164.85)
        CoolAdv = ProPara_IM.CoolPara_Adv()
        CoolAdv.PIInitTemp([30])
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
    cmxFP = CMXPara_IM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=[0.9, 0], Packing=[4, 0])
    cmxFP.Check_ExtendPack((27, 162))
    cmxC = CMXPara_IM.TabCool()
    cmxC.Set_TimeStep(Cooling=[13.7, 0], Opening=[5, 0])
    cmxC.Set_Solver()
    cmxMCM = CMXPara_IM.TabMCM()
    cmxMCM.Set_CoreShift("Two-way (FSI)")
    CSBC = CMXPara_IM.CoreShitBC()
    CSBC.close_DSNSBC()
    cmxTask = CMXPara_IM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()