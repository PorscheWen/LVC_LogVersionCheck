import ProPara_GAIM
import CMXPara_GAIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_GAIM.CAE_MaxPressure(191, 191)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_GAIM.FlowPackTime(0.85, 5)
        ProPara_GAIM.tpMeltMoldTemp(225, 60)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        ProPara_GAIM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_GAIM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (5, 0)
        tupValue = (100, 100)        
        ProPara_GAIM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetGasIn():
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()    
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_GAIM.CoolPara(MBFlag=0, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=90.85)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_Summary():
        # Summary
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFP()
    SubStage_SetGasIn()
    SubStage_SetCool()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_GAIM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=[0.85, 0], Packing=[5, 0])
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()