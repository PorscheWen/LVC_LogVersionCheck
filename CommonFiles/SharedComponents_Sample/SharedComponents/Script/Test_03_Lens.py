﻿import ProPara_IM
import CMXPara_IM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_IM.CAE_MaxPressure(150, 150)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_IM.FlowPackTime(1.8, 5)
        ProPara_IM.tpMeltMoldTemp(310, 100)
        ProPara_IM.VPSwitch(90)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfFR = ProPara_IM.ProfileSetting("FlowRate")
        pfFR.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Flow Rate (%) vs. Time (%)")
        tupTime = (100, 0)
        tupValue = (70, 50)
        pfIP = ProPara_IM.ProfileSetting("InjectionPressure")
        pfIP.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Injection Pressure (%) vs Time (%)")
        tupTime = (5, 4, 3, 0)
        tupValue = (59.8, 74.75, 93.4375, 93.4375)
        pfPP = ProPara_IM.ProfileSetting("PackPressure")
        pfPP.Set_CAEProfile(tupTime, tupValue, SectionNo=3, TypeTag="Packing Pressure (%) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_IM.CoolPara(MBFlag=1, tCool=25, tMBOpen=5, AirTemp=25, EjTemp=143.85)
        CoolAdv = ProPara_IM.CoolPara_Adv()
        CoolAdv.CC(4, [80, 80, 80, 80])
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
    SubStage_SetCool()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_IM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=[1.8, 0], Packing=[5, 0])
    cmxFP.Check_ExtendPack((27, 162))
    cmxC = CMXPara_IM.TabCool()
    cmxC.Set_TimeStep(Cooling=[25, 0], Opening=[5, 0], Mold_preheating=["*", 0])
    cmxC.Set_Solver()
    cmxO = CMXPara_IM.TabOptics()
    cmxO.Check_ResidualStress()
    cmxO.Set_OpticsProperty(1, ("0.00", "1.00", "0.00"))
    cmxO.Set_RunnerEffect()
    cmxO.Set_Polariscope()
    cmxO.Set_WaveLength()
    cmxO.Set_Output3rdSW()
    cmxTask = CMXPara_IM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()