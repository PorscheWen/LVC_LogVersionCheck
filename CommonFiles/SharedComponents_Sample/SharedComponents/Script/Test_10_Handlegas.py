import ProPara_GAIM
import CMXPara_GAIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_GAIM.CAE_MaxPressure(147, 147)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        Inlet1 = ProPara_GAIM.InletSetting("#1")
        Inlet1.Set_InletType("Melt")
        Inlet1.Set_Nozzle("No")
        Inlet1.Set_PackTime(14.3)
        Inlet1.Set_Nozzle("Yes")
        Inlet1.Set_VPSwitch("By Volume(%) filled")
        Inlet1.Set_FlowTime(1.61068)
        Inlet1.Set_MeltTemp(205)
        Inlet1.Set_MoldTemp(50)
        Inlet1.Set_Nozzle("Yes")
        Inlet1.Set_VPSwitch("By Volume(%) filled")
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        pfMelt = ProPara_GAIM.ProfileSetting("Melt")
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfMelt.Set_CAEProfile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfMelt.Set_CAEProfile("InjactionPressure", tupTime, tupValue, SectionNo=1)   
        pfMelt.Set_CAEProfile("PackPressure", TypeTag="Packing Pressure (%) vs. Time (sec)")
        Inlet2 = ProPara_GAIM.InletSetting("#2")
        Inlet2.Set_InletType("Gas")
        Inlet2.Set_GasDelayTime(0.161068)
        Inlet2.Set_GasDurationTime(5)
        Inlet2.Set_GasPressure(20)
        Inlet2.Set_GasTemp(25)
        Inlet2.Set_GasEnterTime("By volume(%) filled")
        pfWater = ProPara_GAIM.ProfileSetting("Gas")
        tupTime = (5, 0)
        tupValue = (100, 100)
        pfWater.Set_CAEProfile("WaterPressure", SectionNo=1, TypeTag="Gas Pressure (%) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_GAIM.CoolPara(MBFlag=1, tCool=40, tMBOpen=5, AirTemp=25, EjTemp=150)
        CoolAdv = ProPara_GAIM.CoolPara_Adv()
        CoolAdv.CC(6, lstT=[50, 50, 50, 50, 50, 50])
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
    cmxFP = CMXPara_GAIM.TabFlowPack()
    cmxFP.Set_3DTimeStep(FP=[1.61+5.0, 0])
    cmxC = CMXPara_GAIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[40, 0], Opening=[5, 0])
    cmxC.Set_Solver()
    cmxTask = CMXPara_GAIM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()