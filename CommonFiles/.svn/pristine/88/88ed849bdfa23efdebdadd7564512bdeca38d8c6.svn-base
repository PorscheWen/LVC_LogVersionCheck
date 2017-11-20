ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000


def ChooseMachine(iMchnMode, sMachine):
    Aliases.MdxPro.wndAfx.SysTabControl32.SetBasic.SetMode.ClickItem("Machine mode %i*" % iMchnMode)
    Aliases.MdxPro.wndAfx.SysTabControl32.SetBasic.MachineSetting.ClickItem("<New...>")
    Aliases.MdxPro.dlgSelectInjectionMachine.SysTreeView32.ClickItem(sMachine)
    Aliases.MdxPro.dlgSelectInjectionMachine.btn_OK.ClickButton()
    Aliases.MdxPro.dlgMdxpro.btn_No.ClickButton()

def CAE_MaxPressure(maxpInjection=None, maxpPacking=None):
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetBasic.MaxP
    # Modify Maximun Injection Pressure
    if maxpInjection != None:
        Obj.Click(245, 22)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(maxpInjection))
    # Click Maximun Packing Pressure
    if maxpPacking != None:
        Obj.Click(245, 57)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(maxpPacking))


def FlowPackTime(tFlow=None, tPack=None):
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetFP
    if tFlow != None:
        Obj.FlowTime.SetText(str(tFlow))
    if tPack != None:
        Obj.PackTime.SetText(str(tPack))


def tpMeltMoldTemp(tMelt=None, tMold=None):
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.Temp
    # Modify Melt Temp.
    if tMelt != None:
        Obj.Click(196, 15)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tMelt))
    # Modify Mold Temp.
    if tMold != None:
        Obj.Click(193, 50)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tMold))


def tsMeltMoldTemp(tMelt=None, tMold=None, cvInital=None):
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetFC.Temp
    # Modify Melt Temp.
    if tMelt != None:
        Obj.Click(195, 12)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tMelt))
    # Modify Mold Temp.
    if tMold != None:
        Obj.Click(195, 35)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tMold))
    # Modify Initial Conversion.
    if cvInital != None:
        Obj.Click(195, 60)
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(cvInital))

def VPSwitch(iVPVal=98, sVPType="By volume(%) filled"):
    Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.VPSwitchOver.ClickItem(sVPType)
    Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.VPSwitchValue.SetText(str(iVPVal))

def CoolPara(MBFlag, **dicParaValue):
    def Action():
        i = 0
        for k in tupParaKey:
            l = dicParaValue.get(k)
            if l != None:
                Obj.Click(cp1st[0], cp1st[1] + i)
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(l))
                Obj.Edit.Keys("[Enter]")
                W = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 0.3*sec)
                if W.Exists:
                    Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
            i += 23
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.Custom1
    if MBFlag == 1:
        cp1st = (280, 59 + 23)
        tupParaKey = ("AirTemp", "EjTemp", "tCool", "tMBOpen")
        Action()
    elif MBFlag == 0:
        cp1st = (285, 36)
        tupParaKey = ("AirTemp", "EjTemp", "tCool", "tMBOpen")
        Action()


def CAE_Profile(ProfileTag, tupTime, tupValue, RefPackPr=None, **dicProfile):
    tupParaKey = ("TypeTag", "SectionNo", "ptTypeTag")
    def ActionProfileTag():
        if ProfileTag == "FlowRate":
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileFlowRate.ClickButton()
        elif ProfileTag == "InjactionPressure":
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileInjectionPressure.ClickButton()
        elif ProfileTag == "PackPressure":
            if RefPackPr:
                Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.RefPressure.ClickItem(
                    "Packing pressure refers to machine pressure")
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfilePackingPressure.ClickButton()
        else:
            Log.Error("ProfileTag Parameter Error")
        ActionTypeTag(dicProfile.get(tupParaKey[0]))
        ActionSectionNo(dicProfile.get(tupParaKey[1]))
        ActionptTypeTag(dicProfile.get(tupParaKey[2]))
        CAE_ModifyProfileValue(tupTime, tupValue)
        Aliases.MdxPro.dlgProfile.btn_OK.ClickButton()
    def ActionTypeTag(GetParam):
        #GetParam = dicProfile.get(tupParaKey[0])
        if GetParam != None:
            Aliases.MdxPro.dlgProfile.Type.ClickItem(GetParam)
        else:
            Log.Message("Profile Type do not changed")

    def ActionSectionNo(GetParam):
        #GetParam = dicProfile.get(tupParaKey[1])
        if GetParam != None:
            Aliases.MdxPro.dlgProfile.SectionNo.SetText(str(GetParam))
        else:
            Log.Message("Section No. do not changed")

    def ActionptTypeTag(GetParam):
        #GetParam = dicProfile.get(tupParaKey[2])
        if GetParam == "Stepwise":
            Aliases.MdxPro.dlgProfile.ptStepwise.ClickButton()
        elif GetParam == "Polyline":
            Aliases.MdxPro.dlgProfile.ptPolyline.ClickButton()
        else:
            Log.Message("Section No. do not changed")
    ActionProfileTag()


def CAE_ModifyProfileValue(tupTime, tupValue):

    Obj = Aliases.MdxPro.dlgProfile.TableEdit
    Obj.Click(473, 47)
    i = 0
    while i < len(tupTime) - 1:
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tupTime[i]))
        Obj.Edit.Keys("[Enter]")
        Obj.Keys("[Left]")
        i += 1
    Obj.Click(473, 74)
    i = 0
    while i < len(tupValue) - 1:
        Obj.Keys("[F2]")
        Obj.Edit.SetText(str(tupValue[i]))
        Obj.Edit.Keys("[Enter]")
        Obj.Keys("[Left]")
        i += 1

class ProfileSetting():

    def __init__(self, ProfileTag, RefPackPr=None):
        # Project.Variables.ProfileWndCaption = "*prfile*"
        if RefPackPr:
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.RefPressure.ClickItem(RefCurePr)
        else:
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.RefPressure.ClickItem("Packing pressure refers to end of filling pressure")
        dicProfile = {
            "FlowRate": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileFlowRate.ClickButton(),
            "InjectionPressure": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileInjectionPressure.ClickButton(),
            "PackPressure": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfilePackingPressure.ClickButton(),
        }.get(ProfileTag)()

    def Set_CAEProfile(self, tupTime=None, tupValue=None, **dicProfile):
        tupParaKey = ("TypeTag", "SectionNo", "ptTypeTag")
        self.modify_TypeTag(dicProfile.get(tupParaKey[0]))
        self.modify_SectionNo(dicProfile.get(tupParaKey[1]))
        self.modify_ptTypeTag(dicProfile.get(tupParaKey[2], "Stepwise"))
        self.modify_ProfileValue(tupTime, tupValue)
        Aliases.MdxPro.dlgProfile.btn_OK.ClickButton()

    def Set_MachineProfile(self, tupTime=None, tupValue=None, **dicProfile):
        tupParaKey = ("TypeTag", "SectionNo", "ptTypeTag", "RamDir")
        self.modify_TypeTag(dicProfile.get(tupParaKey[0]))
        self.modify_SectionNo(dicProfile.get(tupParaKey[1]))
        self.modify_ptTypeTag(dicProfile.get(tupParaKey[2], "Stepwise"), )
        self.modify_RamDir(dicProfile.get(tupParaKey[3], "L"))
        self.modify_ProfileValue2(tupTime, tupValue)
        Aliases.MdxPro.dlgProfile.btn_OK.ClickButton()
        pass

    def modify_SectionNo(self, GetParam):
        if GetParam:
            Aliases.MdxPro.dlgProfile.SectionNo.SetText(str(GetParam))

    def modify_TypeTag(self, GetParam):
        if GetParam:
            Aliases.MdxPro.dlgProfile.Type.ClickItem(GetParam)

    def modify_ptTypeTag(self, GetParam):
        if GetParam == "Stepwise":
            Aliases.MdxPro.dlgProfile.ptStepwise.ClickButton()
        elif GetParam == "Polyline":
            Aliases.MdxPro.dlgProfile.ptPolyline.ClickButton()

    def modify_RamDir(self, GetParam):
        if GetParam == "R":
            Aliases.MdxPro.dlgProfile.dri_RtoL.ClickButton()
        elif GetParam == "L":
            Aliases.MdxPro.dlgProfile.dri_LtoR.ClickButton()

    def modify_ProfileValue(self, tupTime, tupValue):
        if tupTime and tupValue:
            Obj = Aliases.MdxPro.dlgProfile.TableEdit
            Obj.Click(473, 47)
            i = 0
            while i < len(tupTime) - 1:
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(tupTime[i]))
                Obj.Edit.Keys("[Enter]")
                Obj.Keys("[Left]")
                i += 1
            Obj.Click(473, 74)
            i = 0
            while i < len(tupValue) - 1:
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(tupValue[i]))
                Obj.Edit.Keys("[Enter]")
                Obj.Keys("[Left]")
                i += 1

    def modify_ProfileValue2(self, tupTime, tupValue):
        if tupTime and tupValue:
            Obj = Aliases.MdxPro.dlgProfile.TableEdit
            Obj.Click(473, 47)
            # Obj.Keys("[Left]")
            i = 0
            while i < len(tupTime) - 1:
                Obj.Keys("[Left]")
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(tupTime[-i-1]))
                Obj.Edit.Keys("[Enter]")
                # Obj.Keys("[Left]")
                i += 1
            Obj.Click(473, 74)
            # Obj.Keys("[Left]")
            i = 0
            while i < len(tupValue) - 1:
                Obj.Keys("[Left]")
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(tupValue[-i-1]))
                Obj.Edit.Keys("[Enter]")
                # Obj.Keys("[Left]")
                i += 1

class CoolPara_Adv():

    def __init__(self):
        pass

    def CC(self, iEC, lstT=None, lstQ=None, lstCCCoolant=None):
        self.iCont = iEC
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.CoolingChannelHeatingRod.ClickButton()
        self.objCustom = Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page32770.CC
        if lstT:
            self.lstValue = lstT
            self.custom_Edit((136, 36))
        if lstQ:
            self.lstValue = lstQ
            self.custom_Edit((210, 36))
        if lstCCCoolant:
            self.lstItem = lstCCCoolant
            self.custom_Combobox((300, 36))
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()

    def HR(self, iRod, lstMethod=None, lstT=None):
        self.iCont = iRod
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.CoolingChannelHeatingRod.ClickButton()
        self.objCustom = Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page32770.HR
        if lstMethod:
            self.lstItem = lstMethod
            self.custom_Combobox((215, 36))
        if lstValue:
            self.lstValue = lstT
            self.custom_Edit((342, 36))
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()

    def custom_Edit(self, tupXY):
        self.objCustom.Click(tupXY[0], tupXY[1])
        if self.iCont > 6:
            self.objCustom.VScroll.Pos = 0
        for i in range(self.iCont):
            self.objCustom.Keys("[F2]")
            self.objCustom.Edit.SetText(str(self.lstValue[i]))
            self.objCustom.Keys("[Enter]")
            W = Aliases.MdxPro.WaitAliasChild("dlgMdxpro", 0.3*sec)
            if W.Exists:
                Aliases.MdxPro.dlgMdxpro.btn_OK.ClickButton()
            self.objCustom.Keys("[Down]")

    def custom_Combobox(self, tupXY):
        for i in range(self.iCont):
            self.objCustom.Click(tupXY[0], tupXY[1] + i * 24)
            self.objCustom.Keys("[F2]")
            self.objCustom.ComboBox.ClickItem(self.lstItem[i])

    def MIInitTemp(self, iMI, lstT=None, lstType=None):
        self.iCont = iMI
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.MoldInsertInitialTemperature.ClickButton()
        self.objCustom = Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327705.MIInitTemp
        if lstT:
            self.lstValue = lstT
            self.custom_Edit((240, 36))
        if lstType:
            self.lstItem = lstType
            self.custom_Combobox((400, 36))
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()

    def MoldMetalMTR(self, xthMTR, CutomizeMTR):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.MoldMetalMaterial.ClickButton()
        Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327702.MoldMetalMTR.Click(
            362, 36 + (xthMTR - 1) * 24)
        Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327702.MoldMetalMTR.Keys(
            "[F2]")
        Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327702.MoldMetalMTR.ComboBox.ClickItem(
            CutomizeMTR)
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()

    def EjectCriteria(self, numSNID, lstCriteria):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.EjectCriteria.ClickButton()
        for i in range(numSNID):
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.SNID.Click(
                70, 36 + i * 22)
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.btn_Add.ClickButton()
        Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.CriTemp.Click(
            202, 36)
        for i in range(numSNID):
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.CriTemp.Keys(
                "[F2]")
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.CriTemp.Edit.SetText(
                str(lstCriteria[i]))
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.CriTemp.Edit.Keys(
                "[Enter]")
            Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327703.CriTemp.Keys(
                "[Down]")
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()

    def PIInitTemp(self, lstT):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.PartInsertInitialTemperature.ClickButton()
        obj = Aliases.MdxPro.dlgCoolingAdvancedSetting.SysTabControl32.page327704.PIInitTemp
        obj.Click(360, 36)
        for i in range(len(lstT)):
            obj.Keys("[F2]")
            obj.Edit.SetText(str(lstT[i]))
            obj.Keys("[Enter]")
            obj.Keys("[Down]")
        Aliases.MdxPro.dlgCoolingAdvancedSetting.btn_OK.ClickButton()