ModelPath = r"C:\WorkingFolder\testCase\testModel"
sec = 1000

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
        #UI NameMapping Changed
        Obj.VPSwitchValue.SetText(str(tFlow))
    if tPack != None:
        Obj.NozzleIsShutOff.ClickButton(cbUnchecked)
        Obj.FlowTime.SetText(str(tPack[1]))
        if tPack[0] == "Yes":
            Obj.NozzleIsShutOff.ClickButton(cbChecked)
            
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
        
def tsMeltMoldTemp(tMelt=None, tMold=None, tInital=None):
    pass
        
def CoolPara(MBFlag,**dicParaValue):
    def Action():
        i = 0
        for k in tupParaKey:
            l = dicParaValue.get(k)
            if l != None:
                Obj.Click(cp1st[0], cp1st[1] + i)
                Obj.Keys("[F2]")
                Obj.Edit.SetText(str(l))
                Obj.Edit.Keys("[Enter]")
            i += 23
    Obj = Aliases.MdxPro.wndAfx.SysTabControl32.SetCool.Custom1
    if MBFlag == 1:
        cp1st = (285, 82)
        tupParaKey = ("AirTemp","EjTemp","tCool","tMBOpen")
        Action()
    elif MBFlag == 0:
        cp1st = (285, 36) 
        tupParaKey = ("AirTemp","EjTemp","tCool","tMBOpen")
        Action()
        
class Compression:

    def __init__(self):
        self.WndObj = Aliases.MdxPro.wndAfx.SysTabControl32.SetCompression

    def Set_ClickItem(self, lstItem):
        self.WndObj.CompressDirection.ClickItem(lstItem[0])
        self.WndObj.CompressSwitchBy.ClickItem(lstItem[1])
        
    def Set_Value(self, lstVal):
        self.WndObj.CompressTime.SetText(str(lstVal[0]))
        self.WndObj.CompressGap.SetText(str(lstVal[1]))
        self.WndObj.CompressSwitchValue.SetText(str(lstVal[2]))
        self.WndObj.DelayTime.SetText(str(lstVal[3]))
        self.WndObj.CompressSpeed.SetText(str(lstVal[4]))
        self.WndObj.MaxCompressForce.SetText(str(lstVal[5]))

class ProfileSetting:
    
    def __init__(self, ProfileTag):
        dicProfile = {
            "FlowRate": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileFlowRate.ClickButton(),
            "InjactionPressure": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileInjectionPressure.ClickButton(),
            "PackPressure": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfilePackingPressure.ClickButton(),
            "Speed": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetCompression.ProfileCompressSpeed.ClickButton(),
            "Force": lambda: Aliases.MdxPro.wndAfx.SysTabControl32.SetCompression.ProfileCompressForce.ClickButton()
        }.get(ProfileTag)()
        if ProfileTag == "Speed" or ProfileTag == "Force":
            Project.Variables.ProfileWndCaption = "Compression*"

    def Set_CAEProfile(self, tupTime=None, tupValue=None, **dicProfile):
        tupParaKey = ("TypeTag", "SectionNo", "ptTypeTag")
        valTypeTag = dicProfile.get(tupParaKey[0])
        valSectionNo = dicProfile.get(tupParaKey[1])
        valptType = dicProfile.get(tupParaKey[2])
        if valTypeTag != None:
            Aliases.MdxPro.dlgProfile.Type.ClickItem(valTypeTag)
        if valSectionNo != None:
            Aliases.MdxPro.dlgProfile.SectionNo.SetText(str(valSectionNo))
        if valptType != None:
            Aliases.MdxPro.dlgProfile.Type.ClickItem(valTypeTag)
        if valptType == "Stepwise":
            Aliases.MdxPro.dlgProfile.ptStepwise.ClickButton()
        elif valptType == "Polyline":
            Aliases.MdxPro.dlgProfile.ptPolyline.ClickButton()
        self.modify_ProfileValue(tupTime, tupValue)
        Aliases.MdxPro.dlgProfile.btn_OK.ClickButton()

    def modify_ProfileValue(self, tupTime, tupValue, Obj=Aliases.MdxPro.dlgProfile.TableEdit):
        if tupTime and tupValue:
            # Obj = Aliases.MdxPro.dlgProfile.TableEdit
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
            self.objCustom.Keys("[Up]")
        for i in range(self.iCont):
            self.objCustom.Keys("[F2]")
            self.objCustom.Edit.SetText(str(self.lstValue[i]))
            self.objCustom.Keys("[Enter]")
            self.objCustom.Keys("[Down]")

    def custom_Combobox(self, tupXY):
        for i in range(self.iCont):
            self.objCustom.Click(tupXY[0], tupXY[1] + i * 24)
            self.objCustom.Keys("[F2]")
            self.objCustom.ComboBox.ClickItem(self.lstItem[i])

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
