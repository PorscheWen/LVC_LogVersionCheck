﻿ModelPath = r"C:\WorkingFolder\testCase\testModel"
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
        Obj.FlowTime.SetText(str(tPack))

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
        tupParaKey = ("CoolMethod", "IniMBTemp", "AirTemp", "EjTemp", "tCool", "tMBOpen", "MBpreheat")
        Action()
    elif MBFlag == 0:
        cp1st = (285, 36) 
        tupParaKey = ("AirTemp","EjTemp","tCool","tMBOpen")
        Action()
                
def CAE_Profile(ProfileTag, tupTime, tupValue, **dicProfile):
    tupParaKey = ("TypeTag", "SectionNo", "ptTypeTag")
    def ActionProfileTag():
        if ProfileTag == "FlowRate":
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileFlowRate.ClickButton()
        elif ProfileTag == "InjactionPressure":
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfileInjectionPressure.ClickButton()
        elif ProfileTag == "PackPressure":
            Aliases.MdxPro.wndAfx.SysTabControl32.SetFP.ProfilePackingPressure.ClickButton()
        else:
            Log.Error("ProfileTag Parameter Error" )
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
        
class Foaming:

    def __init__(self):
        pass
        
    def Shot_Weight_Ctrl(self, valSet, strMethod="Volume percentage"):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetFoam.ShotWeightCtrl.ClickItem(strMethod)
        Aliases.MdxPro.wndAfx.SysTabControl32.SetFoam.ShotWeight.SetText(str(valSet))
        
    def Initial_Gas_Concentration(self, valSet, strMethod="Gas dosage amount*"):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetFoam.InitGasConcentration.ClickItem(strMethod)
        Aliases.MdxPro.wndAfx.SysTabControl32.SetFoam.ConcentrationVal.SetText(str(valSet))
        
    def Solid_Part_Weight(self, valSet):
        Aliases.MdxPro.wndAfx.SysTabControl32.SetFoam.SolidPartWeight.SetText(str(valSet))