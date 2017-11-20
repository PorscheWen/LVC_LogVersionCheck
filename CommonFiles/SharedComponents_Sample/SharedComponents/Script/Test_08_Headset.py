﻿import ProPara_CoIM
import CMXPara_CoIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_CoIM.CAE_MaxPressure(250, 250)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        Inlet1 = ProPara_CoIM.InletSetting("Skin")
        Inlet1.Set_FlowTime(0.1)
        Inlet1.Set_MaxFlowRate(17.5634)
        Inlet1.Set_MeltTemp(220)
        Inlet1.Set_MoldTemp(40)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        pf1 = ProPara_CoIM.ProfileSetting("Skin")
        tupTime = (100, 0)
        tupValue = (100, 100)
        pf1.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pf1.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)   
        Inlet2 = ProPara_CoIM.InletSetting("Core")
        Inlet2.Set_VPSwitch("By volume(%) filled")
        Inlet2.Set_RefPackPr("End of filling pressure")
        Inlet2.Set_CoreEnter("By volume(%) filled")
        Inlet2.Set_FlowTime(0.1)
        Inlet2.Set_MaxFlowRate(17.5634)
        Inlet2.Set_PackTime(0)
        Inlet2.Set_MeltTemp(200)
        Inlet2.Set_VPSwitchValue(98)
        Inlet2.Set_CoreEnterTime(80)
        tupTime = (100, 0)
        tupValue = (100, 100)
        pf2 = ProPara_CoIM.ProfileSetting("Core")
        pf2.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pf2.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_CoIM.CoolPara(MBFlag=1, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=110)
        CoolAdv = ProPara_CoIM.CoolPara_Adv()
        CoolAdv.MoldMetalMTR(1, "P6")
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFP()
    SubStage_SetCool()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_CoIM.TabFlowPack()
    cmxFP.Set_TimeStep(FP=[0.1+0.1-0.1*(1-0.8), 0])
    cmxC = CMXPara_CoIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[20, 0], Opening=[5, 0])
    cmxC.Set_Solver()
    cmxTask = CMXPara_CoIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()