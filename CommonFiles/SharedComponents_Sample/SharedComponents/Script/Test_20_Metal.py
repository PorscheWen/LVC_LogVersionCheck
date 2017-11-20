import ProPara_PIM
import CMXPara_PIM
sec = 1000

def Stage_004_SetProcess():
    def SubStage_SetProject():
        # Porject Setting: 
        ProPara_PIM.CAE_MaxPressure(256, 256)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetFP():
        # Flow/Pack Setting:
        ProPara_PIM.FlowPackTime(0.1, 5)
        ProPara_PIM.tpMeltMoldTemp(180, 80)
        #   1st Argv is Profile Type: "FlowRate", InjactionPressure", "PackPressure"
        #   2nd Argv Template: TypeTag=, SectionNo=, ptTypeTag=
        tupTime = (100, 0)
        tupValue = (50, 50)
        ProPara_PIM.CAE_Profile("FlowRate", tupTime, tupValue, SectionNo=1)
        tupTime = (100, 0)
        tupValue = (70, 70)
        ProPara_PIM.CAE_Profile("InjactionPressure", tupTime, tupValue, SectionNo=1)
        tupTime = (5, 0)
        tupValue = (100, 100)        
        ProPara_PIM.CAE_Profile("PackPressure", tupTime, tupValue, SectionNo=1)
        Aliases.MdxPro.wndAfx.btn_Next.ClickButton()
    def SubStage_SetCool():
        # Cool Setting:
        # CoolPara:
        #   1st Argv is MBFlag
        #   2nd Argv Template: CoolMethod=, IniMBTemp=, AirTemp=, EjTemp=, tCool=, tMBOpen=, MBpreheat=
        ProPara_PIM.CoolPara(MBFlag=1, tCool=20, tMBOpen=5, AirTemp=25, EjTemp=120)
        CoolAdv = ProPara_PIM.CoolPara_Adv()
        CoolAdv.HR(iRod=4, lstT=[80, 80, 80, 80])
        CoolAdv.MoldMetalMTR(1, "P6")
        CoolAdv.EjectCriteria(6, lstCriteria=[120, 120, 120, 120, 120, 120])
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
    cmxFP = CMXPara_PIM.TabFlowPack()
    cmxFP.Set_TimeStep(Filling=[0.1, 0], Packing=[5, 0])
    cmxC = CMXPara_PIM.TabCool()
    cmxC.Set_TimeStep(Cooling=[20, 0], Opening=[5, 0], Mold_preheating=["*", 0])
    cmxTask = CMXPara_PIM.TabTask()
    cmxTask.Set_TaskNo(1)
    cmxS = CMXPara_PIM.TabStress()
    cmxS.Set_SBC()
    SBC = MyStressBC()
    SBC.Set_Force()
    SBC.Set_Pressure()
    SBC.Set_Displacement()
    SBC.close_DSNSBC()
    Aliases.MDXProject.wndCMX.btn_OK.ClickButton()
    Aliases.MDXProject.dlgRunWizard.btn_Next.ClickButton()

class MyStressBC(CMXPara_PIM.StressBC):

    def Set_Force(self):
        super(MyStressBC, self).add_Force()
        super(MyStressBC, self).zoom_In((330, 272), (44, 21))
        super(MyStressBC, self).click_Mesh((245, 310))
        super(MyStressBC, self).click_Mesh((665, 310))
        super(MyStressBC, self).check_Add()
        super(MyStressBC, self).modify_fz(1)

    def Set_Pressure(self):
        super(MyStressBC, self).add_Pressure()
        super(MyStressBC, self).zoom_In((510, 520), (70, 40))
        super(MyStressBC, self).click_Mesh((400, 285))
        super(MyStressBC, self).check_Add()
        super(MyStressBC, self).modify_pr(1)

    def Set_Displacement(self):
        super(MyStressBC, self).add_Displacement()
        super(MyStressBC, self).zoom_In((235, 400), (30, 30))
        super(MyStressBC, self).click_Mesh((944/2, 786/2))
        super(MyStressBC, self).zoom_In((480, 480), (40, 30))
        super(MyStressBC, self).click_Mesh((455, 280))
        super(MyStressBC, self).zoom_In((660, 405), (9, 9))
        super(MyStressBC, self).click_Mesh((646, 517))
        super(MyStressBC, self).check_Add()