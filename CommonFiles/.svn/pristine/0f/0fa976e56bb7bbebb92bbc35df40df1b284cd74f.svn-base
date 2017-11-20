import ProPara_BiIM
import CMXPara_BiIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_BiIM.CAE_MaxPressure(240, 240)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        Inlet1 = ProPara_BiIM.InletSetting("1")
        Inlet1.Set_VPSwitch("By volume(%) filled")
        Inlet1.Set_RefPackPr("Machine pressure")
        Inlet1.Set_FlowTime(0.3)
        Inlet1.Set_MaxFlowRate(78.8443)
        Inlet1.Set_PackTime(0.5)
        Inlet1.Set_MeltTemp(330)
        Inlet1.Set_MoldTemp(100)
        Inlet1.Set_VPSwitchValue(90)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        pf1 = ProPara_BiIM.ProfileSetting()
        tupTime = (100, 0)
        tupValue = (100, 100)
        pf1.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pf1.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)   
        tupTime = (0.5, 0)
        tupValue = (79.9999, 79.9999)
        pf1.Set_CAEProfile("PackPressure", TypeTag="Packing Pressure (%) vs. Time (sec)")
        Inlet2 = ProPara_BiIM.InletSetting("2")
        Inlet2.Set_VPSwitch("By volume(%) filled")
        Inlet2.Set_RefPackPr("Machine pressure")
        Inlet2.Set_FlowTime(0.3)
        Inlet2.Set_MaxFlowRate(80)
        Inlet2.Set_PackTime(0.5)
        Inlet2.Set_MeltTemp(330)
        Inlet2.Set_VPSwitchValue(90)
        tupTime = (100, 0)
        tupValue = (100, 100)
        pf2 = ProPara_BiIM.ProfileSetting()
        pf2.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pf2.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)   
        tupTime = (0.5, 0)
        tupValue = (79.9999, 79.9999)
        pf2.Set_CAEProfile("PackPressure", TypeTag="Packing Pressure (MPa) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_BiIM.CoolPara(MBFlag=1, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=143.85)
        CoolAdv = ProPara_BiIM.CoolPara_Adv()
        CoolAdv.MoldMetalMTR(1, "P6")
        CoolAdv.MoldMetalMTR(2, "P6")
        CoolAdv.MoldMetalMTR(3, "P6")
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
    cmxFP = CMXPara_BiIM.TabFlowPack()
    cmxFP.Set_TimeStep(FP=[0.3+0.5, 0])
    cmxC = CMXPara_BiIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[20, 0], Opening=[5, 0])
    cmxC.Set_3DCool(1, "Run 3D solid cooling channel analysis")
    cmxC.Set_Solver()
    cmxTask = CMXPara_BiIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()