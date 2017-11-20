import ProPara_MCIM
import CMXPara_MCIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_MCIM.CAE_MaxPressure(158, 158)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_MCIM.FlowPackTime(0.7, 0.1)
        ProPara_MCIM.tpMeltMoldTemp(250, 60)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        ProPara_MCIM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_MCIM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (0.1, 0)
        tupValue = (100, 100)        
        ProPara_MCIM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFoam():
        MF = ProPara_MCIM.Foaming()
        MF.Shot_Weight_Ctrl(95)
        MF.Solid_Part_Weight(49.157)
        MF.Initial_Gas_Concentration(0.5)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_MCIM.CoolPara(MBFlag=0, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=89.85)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_Summary():
        # Summary
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFP()
    SubStage_SetFoam()
    SubStage_SetCool()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_MCIM.TabFlowPack()
    cmxFP.Set_TimeStep(FP=[0.7+0.1, 0], Foaming=[20, 0])
    cmxC = CMXPara_MCIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[20, 0], Opening=[5, 0])
    cmxTask = CMXPara_MCIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()