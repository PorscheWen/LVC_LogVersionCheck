import ProPara_RIM
import CMXPara_RIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_RIM.CAE_MaxPressure(150.1, 150.1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFC():
        # Flow/Pack Setting:
        ProPara_RIM.FlowCureTime(4.19, 23.3)
        ProPara_RIM.tsMeltMoldTemp(20, 120, 0)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 92.98, 29.82, 0)
        tupValue = (54, 95, 30, 30)
        ProPara_RIM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=3)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_RIM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (23.3, 18.64, 13.98, 0)
        tupValue = (46.08, 57.6, 72, 72)
        ProPara_RIM.CAE_Profile("Curing Pressure", tupTime, tupValue, SectionNo=3)
        ProPara_RIM.FlowCureTime(None, 23.3)
        ProPara_RIM.CAE_Profile("Curing Pressure", tupTime, tupValue, SectionNo=3)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_Summary():
        # Summary
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetProject()
    SubStage_SetFC()
    SubStage_Summary()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFP = CMXPara_RIM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=[4.19, 0], Curing=[23.3, 0])
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()