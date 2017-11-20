import ProPara_Encapsulation
import CMXPara_Encapsulation
sec = 1000


def Stage_004_SetProcess():
    def SubStage_SetEncapsTM():
        # Porject Setting:
        EcsTM = ProPara_Encapsulation.EncapsTM("Transfer Molding")
        # Encapsulation Setting:
        EcsTM.Set_Other((85, 175, 7, 7, 5, 7, 98, 0))
        EcsTM.Set_InitConvers("Constant")
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        pfFR = ProPara_Encapsulation.ProfileSetting("FlowRate")
        pfFR.Set_CAEProfile(tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfTFPr = ProPara_Encapsulation.ProfileSetting("TransferPressure")
        pfTFPr.Set_CAEProfile(tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        pfCrPr = ProPara_Encapsulation.ProfileSetting("CurePressure", "Curing pressure refers to end of filling pressure")
        pfCrPr.Set_CAEProfile(tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_Encapsulation.CoolPara(MBFlag=0, tMBOpen=5, AirTemp=25)
        CoolAdv = ProPara_Encapsulation.CoolPara_Adv()
        CoolAdv.PIInitTemp([30, 30])
        Aliases.MdxPro.wndAfx.btn_Finish.ClickButton()
        wr = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 3 * sec)
        if wr.Exists:
            Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
    SubStage_SetEncapsTM()
    SubStage_SetCool()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

def Stage_005_SetCMX():
    Aliases.MDXProject.dlgRunWizard.SysTabControl32.page327705.btn_ViewEdit.ClickButton()
    cmxFC = CMXPara_Encapsulation.TabFlowCure()
    cmxFC.Set_TimeStep(Filling=[7, 0], Curing=[5, 0])
    cmxC = CMXPara_Encapsulation.TabCool()
    cmxC.Set_TimeStep(Opening=[5, 0])
    cmxC.Set_Solver()
    cmxEcps = CMXPara_Encapsulation.TabEncapsulation()
    cmxEcps.Set_TimeStep(Wire_sweep=[6, 7, 0], Paddle_shift=[12, 7, 0])
    cmxEcps.Set_ClickItem(("Drag force model", "Takaisi's model"), "Takaisi's model")
    cmxEcps.Set_ClickItem(("Geometry", "Non-linear"), "Linear")
    cmxEcps.Set_ClickItem(("Material Model", "Linear"), "Linear")
    cmxEcps.Set_ClickItem(("Paddle shift analysis", "One-way"), "One-way")
    cmxEcps.Set_ClickItem(("Analysis type", "Linear"), "Linear")
    cmxTask = CMXPara_Encapsulation.TabTask()
    cmxTask.Set_TaskNo(1)
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.WaitProperty("Enabled", True, 3*sec)
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()