﻿import ProPara_IM
import CMXPara_IM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_IM.CAE_MaxPressure(300, 300)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_IM.FlowPackTime(0.5, 3)
        ProPara_IM.tpMeltMoldTemp(235, 50)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 44, 0)
        tupValue = (85, 15, 15)
        ProPara_IM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=2)
        tupTime = (100, 0)
        tupValue = (125, 125)
        ProPara_IM.CAE_Profile("InjactionPressure", tupTime, tupValue, TypeTag="Injection Pressure (MPa) vs Time (%)", SectionNo=1)
        tupTime = (3.0, 0)
        tupValue = (90, 90)        
        ProPara_IM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_IM.CoolPara(MBFlag=1, tCool=10.6, tMBOpen=5, AirTemp=25, EjTemp=99.85)
        CoolAdv = ProPara_IM.CoolPara_Adv()
        CoolAdv.MoldMetalMTR(1, "P6")
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
    cmxFP.Set_Analysis("Customize", [1, 1, 1, 1, 1])
    cmxFP.Set_TimeStep(Filling=[0.5, 0], Packing=[3, 0])
    cmxFP.Check_ExtendPack((27, 162))
    cmxC = CMXPara_IM.TabCool()
    cmxC.Set_TimeStep(Cooling=[10.6, 0], Opening=[5, 0], Mold_preheating=["*", 0])
    cmxTask = CMXPara_IM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()