import ProPara_IM
import CMXPara_IM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_IM.CAE_MaxPressure(244, 244)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_IM.FlowPackTime(0.5, 8)
        ProPara_IM.tpMeltMoldTemp(340, 90)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        ProPara_IM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_IM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (8, 0)
        tupValue = (100, 100)        
        ProPara_IM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_IM.CoolPara(MBFlag=1, tCool=30, tMBOpen=5, AirTemp=25, EjTemp=250)
        CoolAdv = ProPara_IM.CoolPara_Adv()
        CoolAdv.CC(1, lstT=[70], lstQ=None, lstCCCoolant=None)
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
    cmxFP.Set_TimeStep(Filling=[0.5, 0], Packing=[8, 0])
    cmxFP.Check_ExtendPack((27, 162))
    cmxC = CMXPara_IM.TabCool()
    cmxC.Set_TimeStep(Cooling=[30, 0], Opening=[5, 0], Mold_preheating=["*", 0])
    cmxC.Set_Solver()
    cmxTask = CMXPara_IM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()
    
def Stage_010_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_IM.ChooseMachine(2, "|System|FANUC|S-2000i100A")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_IM.FlowPackTime(10)
        ProPara_IM.tpMeltMoldTemp(230, 60)
        ProPara_IM.VPSwitch(1, "By ram position")
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (0, 53.9273)
        tupValue = (50, 50)
        pfFR = ProPara_IM.ProfileSetting("FlowRate")
        pfFR.Set_MachineProfile(tupTime, tupValue, SectionNo=1, TypeTag="Injection Velocity (%) vs. Ram Position (mm)")
        tupTime = (0, 53.9273)
        tupValue = (70, 50)
        pfIP = ProPara_IM.ProfileSetting("InjectionPressure")
        pfIP.Set_MachineProfile(tupTime, tupValue, SectionNo=1, TypeTag="Injection Pressure (%) vs Ram Position (mm)*")
        tupTime = (9.6085, 0)
        tupValue = (100, 100)
        pfPP = ProPara_IM.ProfileSetting("PackPressure")
        pfPP.Set_CAEProfile(tupTime, tupValue, SectionNo=1, TypeTag="Packing Pressure (%) vs. Time (sec)")
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_IM.CoolPara(MBFlag=1, tCool=40, tMBOpen=5, AirTemp=25, EjTemp=111.15)
        CoolAdv = ProPara_IM.CoolPara_Adv()
        CoolAdv.CC(2, lstT=(60, 60), lstQ=(120, 120), lstCCCoolant=("Water", "Water"))
        CoolAdv.MoldMetalMTR(1, "P20")
        CoolAdv.MoldMetalMTR(2, "P20")
        CoolAdv.MoldMetalMTR(3, "P20")
        CoolAdv.MoldMetalMTR(4, "P20")      
        CoolAdv.PIInitTemp([30])
        CoolAdv.MIInitTemp(3, (60, 60, 60), ("Regular", "Regular", "Regular"))
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

def Stage_011_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_IM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=["*", 0], Packing=["*", 0])
    cmxFP.Check_ExtendPack((27, 162))
    cmxC = CMXPara_IM.TabCool()
    cmxC.Set_TimeStep(Cooling=[40, 0], Opening=[5, 0], Mold_preheating=["*", 0])
    cmxC.Set_Solver()
    cmxMCM = CMXPara_IM.TabMCM()
    cmxMCM.Set_PreviousShot(1)
    cmxTask = CMXPara_IM.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgMoldex3D.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()