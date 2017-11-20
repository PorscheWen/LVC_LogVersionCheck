#-*- coding: utf-8 -*-　
#import os
#import sys
import re
import FeatureOutPut
# 儲存 StepNum 的 List
StepNumLsit = []

#-------------Cycle Cool----------------------
#判斷是否為等差數列
def EqualDifferenceSeries(EDS_List):
  EDS_ListLen = len(EDS_List)
  for i in range(0, EDS_ListLen - 2):
    if EDS_List[i+1] - EDS_List[i] != EDS_List[i+2] - EDS_List[i+1]:
      return False
  return True

#用來判斷該字串是否可以轉成int
def CheckStrToInt(num):
  try:
    num = int(num)
    return num
  except ValueError:
    return
    #print "Cannot change to Int!!"

#用來判斷該字串是否可以轉成float
def CheckStrToFloat(num):
  try:
    num = float(num)
    return num
  except ValueError:
    return
    #print "Cannot change to Float!!"
    
# 找 Cycle Cool 的 總步數
def FindCycleCool_CycleStepNum(totalLine,SplitA,CycleNum):
  d = []
  #紀錄找到Cycle Summary的行數
  CycleSummaryLine = 0
  #紀錄找到IterNo的行數
  IterNoLine = 0
  #紀錄找到IterNo的次數
  IterNoTimes = 0
  #紀錄找到IterFinalLine的行數
  IterFinalLine = 0
  
  for i in range(totalLine, 0, -1):
    #找看有沒有Iter Final避免遇到各cycle寫在一起的log檔時會誤判
    pat = 'Iter Final'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      IterFinalLine = i
    #開始找起始點
    pat = 'IterNo +'+str(CycleNum)
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      IterNoLine = i
      IterNoTimes = IterNoTimes+1
      #print "Find ---No     Time(sec)      Ave   Max/Min(oC)    Ave   Max/Min(oC)  CPU(sec) at line:"+str(i)
      for j in range(i, totalLine, 1):
        pat = '<Cycle Summary>'
        string = SplitA[j-1]
        match = re.search(pat,string)
        if match:
          #print "Find <Cycle Summary> at line:"+str(j)
          #表示該log為各cycle接再一起之狀態
          if 0 < IterFinalLine < j:
            CycleSummaryLine = IterFinalLine
          elif IterFinalLine == 0:
            CycleSummaryLine = j
          else:
            CycleSummaryLine = j
          break
    # 取兩次避免有log檔只有標題之狀況
    if IterNoTimes >= 2 or IterNoTimes == 1:
      for k in range(IterNoLine, CycleSummaryLine, 1):
        #把"No     Time"到"<Cycle Summary>"依照空格去分割後存入c[]
        c = SplitA[k-1].split(" ")
        #刪除List中index之值為空白的元素
        z =[i for i in c if i!='']
        if z:
         #取出第一個元素且只有可以轉換成整數的才存入d[]
          num = CheckStrToInt(z[0])
          if num != None:
            d.append(num)
      #檢查是否為等差數列
      #print d
      MK = EqualDifferenceSeries(d)
      #若為等差數列則d[]的最後一個元素為總步數
      if MK == True:
        FeatureOutPut.WriteOutPut("CycleStepNum_CycleCool",d[len(d)-1])
      #若不是等差數列直接報錯,表示list中有異常數字
      else:
        FeatureOutPut.WriteOutPut("CycleStepNum_CycleCool","Error at FeatureMethod.py")
      break

def FindCycleCool_CycleNum(totalLine,SplitA):
  for i in range(totalLine):
    pat = 'IterNo[ ]?[0-9]+'
    string = SplitA[i]
    match = re.search(pat,string)
    if match:
      CycleNum = match.group()
      # 過濾掉非數字,只保留數字
      CycleNum = filter(str.isdigit,CycleNum)
      # 儲存 CycleNum
      FeatureOutPut.WriteOutPut("CycleNum_CycleCool",CycleNum)
  FindCycleCool_CycleStepNum(totalLine,SplitA,CycleNum)
#-------------Cycle Cool----------------------

#-------------Transient Cool----------------------
# 找 Transient Cool 的 總步數
def FindTransientCool_CycleStepNum(totalLine,SplitA,CycleNum):
  d = []
  #紀錄找到Cycle Summary的行數
  CycleSummaryLine = 0
  #紀錄找到CycleNo的行數
  CycleNoLine = 0  
  #紀錄找CycleNo的次數
  CycleNoTimes = 0  
  for i in range(totalLine, 0, -1):
    pat = 'Cycle +'+str(CycleNum)
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      CycleNoLine = i
      CycleNoTimes = CycleNoTimes+1
      #print "Find ---No     Time(sec)      Ave   Max/Min(oC)    Ave   Max/Min(oC)  CPU(sec) at line:"+str(i)
      for j in range(i, totalLine, 1):
        pat = '<Cycle Summary>'
        string = SplitA[j-1]
        match = re.search(pat,string)
        if match:
          #print "Find <Cycle Summary> at line:"+str(j)
          CycleSummaryLine = j
          break
    # 取兩次避免有log檔只有標題之狀況
    if CycleNoTimes == 2 or CycleNoTimes == 1:
      for k in range(CycleNoLine, CycleSummaryLine, 1):
        #把"No     Time"到"<Cycle Summary>"依照空格去分割後存入c[]
        c = SplitA[k-1].split(" ")
        #刪除List中index之值為空白的元素
        z =[i for i in c if i!='']
        if z:
         #取出第一個元素且只有可以轉換成整數的才存入d[]
          num = CheckStrToInt(z[0])
          if num != None:
            d.append(num)
      #檢查是否為等差數列
      #print d
      MK = EqualDifferenceSeries(d)
      #若為等差數列則d[]的最後一個元素為總步數
      if MK == True:
        FeatureOutPut.WriteOutPut("CycleStepNum",d[len(d)-1])
      #若不是等差數列直接報錯,表示list中有異常數字
      else:
        FeatureOutPut.WriteOutPut("CycleStepNum","Error at FeatureMethod.py")
      break
      
def FindTransientCool_CycleNum(totalLine,SplitA):
  for i in range(totalLine):
    pat = 'Cycle[ ]+[0-9]+'
    string = SplitA[i]
    match = re.search(pat,string)
    if match:
      CycleNum = match.group()
      # 過濾掉非數字,只保留數字
      CycleNum = filter(str.isdigit, CycleNum)
      # 儲存 CycleNum
      FeatureOutPut.WriteOutPut("CycleNum",CycleNum)
  FindTransientCool_CycleStepNum(totalLine,SplitA,CycleNum)
#-------------Transient Cool----------------------

def CoolType(totalLine,SplitA):
  for i in range(totalLine):
    pat = 'Analysis Type.+Cycle-Average '
    string = SplitA[i]
    match = re.search(pat,string)
    if match: 
      #Cycle-Average
      #print "Find Analysis Type = Cycle-Average at line: "+str(i+1)
      AnalysisType = "Cycle-Average"
      FindCycleCool_CycleNum(totalLine,SplitA)
  for i in range(totalLine):
    pat = 'Analysis Type.+Transient'
    string = SplitA[i]
    match = re.search(pat,string)
    if match: 
      #Transient Cool
      #print "Find Analysis Type = Transient at line: "+str(i+1)
      AnalysisType = "Transient"
      FindTransientCool_CycleNum(totalLine,SplitA)

#檢查Flow的步數是否連續
def CheckFlowNum(FlowList):
  for i in range(0, len(FlowList)-1, 1):
    if FlowList[i]+1 != FlowList[i+1]:
      print "XXXXX"
      return False,i+1
  return True,None
#檢查氣輔水輔的充填百分比是否有連續,無忽大忽小之狀況
def CheckFluidFill(FluidList):
  for i in range(0, len(FluidList)-1, 1):
    if FluidList[i] > FluidList[i+1]:
      print "XXXXX"
      return False,i+1
  return True,None


# 判斷水輔充填是否有忽大忽小之狀況
def WaterInjection(totalLine,SplitA,SummaryLine,NoTimeLine):
  #紀錄 No 欄位資訊
  d = []
  #紀錄 WaterFill 欄位資訊
  h = []
  #紀錄找到 WaterFill 的行數
  WaterFillLine = 0
  print "Is WaterFill"
  for i in range(totalLine, 0, -1):
    pat = 'WaterFill'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      #print "find WaterFill at line:"+str(i)
      WaterFillLine = i
  for k in range(WaterFillLine, SummaryLine, 1):
    #把"No  Time"到"<Summary>"依照空格去分割後存入c[]
    c = SplitA[k-1].split(" ")
    #刪除List中index之值為空白的元素
    z =[i for i in c if i!='']
    
    if len(z)>=5:
      num = CheckStrToFloat(z[0])
      if num != None:
        d.append(num)
      num = CheckStrToFloat(z[3])
      if num != None:
        h.append(num)
  FluidFillIsOk,ErrorFluidFillNo = CheckFluidFill(h)
  if FluidFillIsOk == True:
    # 充填百分比之值
    #print h[len(h)-1]
    FeatureOutPut.WriteOutPut("FillError","No")
  # Fill 發生異常(ex:忽大忽小)
  else:
    FeatureOutPut.WriteOutPut("FillError","Yes")
    #print ErrorFluidFillNo
    FeatureOutPut.WriteOutPut("FillErrorStepNum",int(d[ErrorFluidFillNo]))

# 判斷氣輔充填是否有忽大忽小之狀況
def GasInjection(totalLine,SplitA,SummaryLine,NoTimeLine):
  #紀錄 No 欄位資訊
  d = []
  #紀錄 GasFill 欄位資訊
  h = []
  #紀錄找到 GasFill 的行數
  GasFillLine = 0
  print "Is GasFill"
  for i in range(totalLine, 0, -1):
    pat = 'GasFill'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      #print "find GasFill at line:"+str(i)
      GasFillLine = i
  for k in range(GasFillLine, SummaryLine, 1):
    #把"No  Time"到"<Summary>"依照空格去分割後存入c[]
    c = SplitA[k-1].split(" ")
    #刪除List中index之值為空白的元素
    z =[i for i in c if i!='']
    
    if len(z)>=5:
      num = CheckStrToFloat(z[0])
      if num != None:
        d.append(num)
      num = CheckStrToFloat(z[3])
      if num != None:
        h.append(num)
  FluidFillIsOk,ErrorFluidFillNo = CheckFluidFill(h)
  if FluidFillIsOk == True:
    # 充填百分比之值
    #print h[len(h)-1]
    FeatureOutPut.WriteOutPut("FillError","No")
  # Fill 發生異常(ex:忽大忽小)
  else:
    FeatureOutPut.WriteOutPut("FillError","Yes")
    #print ErrorFluidFillNo
    FeatureOutPut.WriteOutPut("FillErrorStepNum",int(d[ErrorFluidFillNo]))
  
#判斷是否為液輔或氣輔
def FluidType(totalLine,SplitA,SummaryLine,NoTimeLine):
  for i in range(totalLine):
    pat = 'Fluid Material'
    string = SplitA[i]
    match = re.search(pat,string)
    if match:
      #print "Fluid Material at line:"+str(i+1)
      pat = 'Water'
      string = SplitA[i]
      match = re.search(pat,string)
      if match:
        WaterInjection(totalLine,SplitA,SummaryLine,NoTimeLine)
      else:
        pat = 'Gas'
        string = SplitA[i]
        match = re.search(pat,string)
        if match:
          GasInjection(totalLine,SplitA,SummaryLine,NoTimeLine)
      
      
def find_FP_FinalStep(totalLine,SplitA):
  d = []
  #紀錄找到Summary的行數
  SummaryLine = 0
  #紀錄找到IterNo的行數
  NoTimeLine = 0
  for i in range(totalLine, 0, -1):
    pat = '<Summary>'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      #print "find <Summary> at line:"+str(i)
      SummaryLine = i
      for j in range(i, 0, -1):
        pat='No +Time'
        string= SplitA[j-1]
        match = re.search(pat,string)
        if match:
          #print "Find ---No   Time(sec)   Q(cc/sec) Fill(%)    CPU(sec) at line:"+str(j)
          NoTimeLine = j
      for k in range(NoTimeLine, SummaryLine, 1):
        #把"No  Time"到"<Summary>"依照空格去分割後存入c[]
        c = SplitA[k-1].split(" ")
        #刪除List中index之值為空白的元素
        z =[i for i in c if i!='']
        if z:
         #取出第一個元素且只有可以轉換成整數的才存入d[]
          num = CheckStrToInt(z[0])
          if num != None:
            d.append(num)
  FlowNumIsOk,ErrorStepNo = CheckFlowNum(d)
  if FlowNumIsOk == True:
    FeatureOutPut.WriteOutPut("TotalStepNum",d[len(d)-1])
  else:
    FlowStepMSG = "The Flow Step Error at NO: "+str(ErrorStepNo)
    FeatureOutPut.WriteOutPut("TotalStepNum",FlowStepMSG)
  #FluidType(totalLine,SplitA,SummaryLine,NoTimeLine)

#-------------LGHC(Cph)----------------------
# 找 LGHC 的 總步數
def FindMoldPreheat_StepNum(totalLine,SplitA):
  d = []
  #紀錄找到Cycle Summary的行數
  CycleSummaryLine = 0
  #紀錄找到IterNo的行數
  NoLine = 0
  for i in range(totalLine, 0, -1):
    pat = '<Cycle Summary>'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      #print "find <Cycle Summary> at line:"+str(i)
      CycleSummaryLine = i
      for j in range(i, 0, -1):
        pat='No +Time'
        string= SplitA[j-1]
        match = re.search(pat,string)
        if match:
          #print "Find ---No     Time(sec)      Ave   Max/Min(oC)    Ave   Max/Min(oC)  CPU(sec) at line:"+str(j)
          NoLine = j
      for k in range(NoLine, CycleSummaryLine, 1):
        #把"No     Ave"到"<Cycle Summary>"依照空格去分割後存入c[]
        c = SplitA[k-1].split(" ")
        #刪除List中index之值為空白的元素
        z =[i for i in c if i!='']
        if z:
         #取出第一個元素且只有可以轉換成整數的才存入d[]
          num = CheckStrToInt(z[0])
          if num != None:
            d.append(num)
      #檢查是否為等差數列
      MK = EqualDifferenceSeries(d)
      #若為等差數列則d[]的最後一個元素為總步數
      if MK == True:
        FeatureOutPut.WriteOutPut("TotalStepNum",d[len(d)-1])
      #若不是等差數列直接報錯,表示list中有異常數字
      else:
        FeatureOutPut.WriteOutPut("TotalStepNum","Error at FeatureMethod.py")
      break

# 看 Hot Runner Steady 的步數是否正確(LGSF)
def FindSteadyStateInterationNo(totalLine,SplitA):
  d = []
  #紀錄找到Summary的行數
  SummaryLine = 0
  #紀錄找到IterNo的行數
  NoTimeLine = 0
  for i in range(totalLine, 0, -1):
    pat = '<Summary>'
    string = SplitA[i-1]
    match = re.search(pat,string)
    if match:
      #print "find <Summary> at line:"+str(i)
      SummaryLine = i
      for j in range(i, 0, -1):
        pat='Iteration +No'
        string= SplitA[j-1]
        match = re.search(pat,string)
        if match:
          #print "Find ---Iteration No.    Relative Error   CPU(sec) at line:"+str(j)
          NoTimeLine = j
      for k in range(NoTimeLine, SummaryLine, 1):
        #把"No  Time"到"<Summary>"依照空格去分割後存入c[]
        c = SplitA[k-1].split(" ")
        #刪除List中index之值為空白的元素
        z =[i for i in c if i!='']
        if z:
         #取出第一個元素且只有可以轉換成整數的才存入d[]
          num = CheckStrToInt(z[0])
          if num != None:
            d.append(num)
  FlowNumIsOk,ErrorStepNo = CheckFlowNum(d)
  if FlowNumIsOk == True:
    FeatureOutPut.WriteOutPut("TotalStepNum",d[len(d)-1])
  else:
    FlowStepMSG = "The Flow Step Error at NO: "+str(ErrorStepNo)
    FeatureOutPut.WriteOutPut("TotalStepNum",FlowStepMSG)
