import ProPara_WAIM
import CMXPara_WAIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_WAIM.CAE_MaxPressure(145, 145)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        Inlet1 = ProPara_WAIM.InletSetting("#1")
        Inlet1.Set_InletType("Melt")
        Inlet1.Set_FlowTime(0.466336)
        Inlet1.Set_MeltTemp(220)
        Inlet1.Set_MoldTemp(40)
        Inlet1.Set_Nozzle("Yes")
        Inlet1.Set_VPSwitch("By Volume(%) filled")
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        pfMelt = ProPara_WAIM.ProfileSetting("Melt")
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfMelt.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfMelt.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)   
        pfMelt.Set_CAEProfile("PackPressure", TypeTag="Packing Pressure (%) vs. Time (sec)")
        Inlet2 = ProPara_WAIM.InletSetting("#2")
        Inlet2.Set_InletType("Water")
        Inlet2.Set_WaterDelayTime(0.1)
        Inlet2.Set_WaterDurationTime(6)
        Inlet2.Set_WaterPressure(5)
        Inlet2.Set_WaterTemp(25)
        Inlet2.Set_WaterEnterTime("By volume(%) filled")
        Inlet2.Set_WaterEnterType("By pressure")
        pfWater = ProPara_WAIM.ProfileSetting("Water")
        tupTime = (6, 0)
        tupValue = (100, 100)
        pfWater.Set_CAEProfile("WaterPressure", SectionNo=1, TypeTag="Water Pressure (%) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_WAIM.CoolPara(MBFlag=1, tCool=40, tMBOpen=5, AirTemp=25, EjTemp=145)
        CoolAdv = ProPara_WAIM.CoolPara_Adv()
        CoolAdv.CC(8, lstT=[40, 40, 40, 40, 40, 40, 40, 40])
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
    cmxFP = CMXPara_WAIM.TabFlowPack()
    cmxFP.Set_TimeStep(FP=[0.47+6.0, 0])
    cmxC = CMXPara_WAIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[40, 0], Opening=[5, 0])
    cmxC.Set_Solver()
    cmxTask = CMXPara_WAIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()