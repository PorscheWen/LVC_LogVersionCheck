#-*- coding: utf-8 -*-　
import os
import sys
import re
import FeatureOutPut
import CompareFeature
import FeatureMethod
import ReadMoldexVersion_py27
import shutil
# 依照換行符號把log檔切割並放入list中
SplitA = []
# 定義是哪一種log
LogType = ""
#----------F/P----------
# 總共有幾行
totalLine = 0
findMark = "StartFind1"
# 儲存 StepNum 的 List
StepNumLsit = []
# nowLine:找<Summary>的當前行數,y:找"No   Time"的當前行數
nowLine = 0
y = 0
#是否發生 Error
OccurError = False



def CheckMDX3DRunJob(strLogsite):
  global OccurError
  #----------取得 MDX3DRunJob 位置----------
  path = r"C:\WorkingFolder\testCase\testModel"
  test = os.listdir(path)
  path2 = os.path.join(path,test[0])
  MDX3DRunJobSite = path2+"\\MDX3DRunJob.log"
  #check analysis done or not
  try:
    f = open(MDX3DRunJobSite)
    file_data = f.read()
    f.close()
    checkDone = 'Done!' in file_data
    if checkDone == True:
      #print "Successful: Find MDX3DRunJob!"
      FeatureOutPut.WriteOutPut("AnalysisResult","Done")
    else:
      match = re.search("Error(.+)(\))",file_data)
      if match:
        m1 = match.group()
        FeatureOutPut.WriteOutPut("AnalysisResult",m1)
        #是否發生Fail
        OccurError = True
  except IOError:
    print "XXX MDX3DRunJobSite Error!!"
  GetLogType(strLogsite)

def GetLogType(strLogsite):
  global LogType
  #----------LGF----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgf'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGF"
    print "It is LGF"
  #----------LGP----------
  pat = r'[-a-zA-Z0-9_ ]+[.](lgp$)'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGP"
    print "It is LGP"
  #----------LGC----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgc'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGC"
    print "It is LGC"
  #----------LGW----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgw'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGW"
    print "It is LGW"
  #----------LGO----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgo'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGO"
    print "It is LGO"
  #----------LGS(Stress)----------
  pat = r'[-a-zA-Z0-9_ ]+[.](lgs$)'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGS"
    print "It is LGS"
  #----------LGSF(HRS)----------
  pat = r'[-a-zA-Z0-9_ ]+[.](lgsf$)'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGSF"
    print "It is LGSF"
  #----------LGHC(Cph, Mold Preheat)----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lghc'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGHC"
    print "It is LGHC"
  #----------LGMD(Mold Deformation)----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgmd'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGMD"
    print "It is LGMD"
  #----------LGI(IC_Wire Sweep)----------
  pat = r'[-a-zA-Z0-9_ ]+[.]lgi'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGI"
    print "It is LGI"
  #----------LGPS(Paddle Shift)----------
  pat = r'[-a-zA-Z0-9_ ]+[.](lgps$)'
  string = strLogsite
  match = re.search(pat,string)
  if match:
    LogType = "LGPS"
    print "It is LGPS"
  # 寫出LogType結果
  FeatureOutPut.WriteOutPut("LogType",LogType)
  OpenLog(strLogsite)
  
def OpenLog(strLogsite):
  global SplitA
  global totalLine
  # 開啟log檔位置
  try:
    Logf = open(strLogsite, 'r')
    Loga = Logf.read()
    # 依照換行符號把log檔切割並放入list中
    SplitA = Loga.split('\n')
    # 總共有幾行
    totalLine = int(len(SplitA))
  except IOError:
    print "XXX  Input Error!! Can not find log!!"
  CheckLogStatus(strLogsite)

# 搜尋 Log檔中的 ERROR 訊息,找到後並寫出訊息
def findErrorLog():
  global SplitA
  global totalLine
  for i in range(totalLine):       
    match = re.search("XXX ERROR",SplitA[i], re.IGNORECASE)
    if match:
      FeatureOutPut.WriteOutPut("ErrorMessage",SplitA[i])
      
# 搜尋 Log檔中的 Warning  訊息,找到後並寫出訊息
def findWarningLog():
  global SplitA
  global totalLine
  for i in range(totalLine):
    match = re.search("!!! WARNING",SplitA[i], re.IGNORECASE)
    if match:
      FeatureOutPut.WriteOutPut("WarningMessage",SplitA[i])
      
#檢查log檔是否有出現error或warning字樣
def CheckLogStatus(strLogsite):
  global OccurError
  # check analysis status(error or warning)
  try:
    f = open(strLogsite)
    file_data = f.read()
    f.close()
    checkError = 'ERROR' in file_data
    if checkError == False:
      #print "Successful No Error"
      FeatureOutPut.WriteOutPut("Error","No")
    else:
      print "ERROR Failed"
      FeatureOutPut.WriteOutPut("Error","Yes")
      findErrorLog()
      OccurError = True
    checkWarning = 'WARNING' in file_data
    if checkWarning == False:
      #print "Successful No Warning"
      FeatureOutPut.WriteOutPut("Warning","No")
    else:
      print "WARNING Failed"
      FeatureOutPut.WriteOutPut("Warning","Yes")
      findWarningLog()
      OccurError = True
  except IOError:
    print "XXX Input Error!!"
    OccurError = True
  CheckReCalculate(OccurError)

#看是否有發生 Re-calculate
def CheckReCalculate(OccurError):
  global totalLine
  if OccurError == False:
    for i in range(totalLine):
      pat = 'Re-calculate'
      string = SplitA[i]
      match = re.search(pat,string)
      if match:
        writeContent = "Yes; at line: "+str(i+1)
        FeatureOutPut.WriteOutPut("Re-calculate",writeContent)
        break;
    if FeatureOutPut.d["Re_calculate"] == "--":
      FeatureOutPut.WriteOutPut("Re_calculate","No")
      StartToFindFeature()

#依照LogType去掃特徵
def StartToFindFeature():
  global LogType
  print "OK"
  if LogType == "LGF":
    FeatureMethod.find_FP_FinalStep(totalLine,SplitA)
  elif LogType == "LGP":
    FeatureMethod.find_FP_FinalStep(totalLine,SplitA)
  elif LogType == "LGC":
    FeatureMethod.CoolType(totalLine,SplitA)
  elif LogType == "LGSF":
    FeatureMethod.FindSteadyStateInterationNo(totalLine,SplitA)
  elif LogType == "LGHC":
    FeatureMethod.FindMoldPreheat_StepNum(totalLine,SplitA)

#siteForStatus = "C:\\WorkingFolder\\testCase\\testModel\\FlowPackSolverTest\\Analysis\\Run01\\FlowPackSolverTest01.lgf"
def CreateDir():
  Path = r"C:\WorkingFolder\testCase\RunScriptV2.py"
  NetPath = r"\\192.168.120.8\Public\Bug&Request\Bug\147001-148000\147891"
  Mold = ""

  Logf = open(Path, 'r')
  Loga = Logf.read()
  SplitA = Loga.split('\n')
  for i in range(0,int(len(SplitA)),1):  
    pat = "from testScript import"
    string = SplitA[i]
    match = re.search(pat,string)
    if match:
      c = SplitA[i].split(" ")
      store = c[int(len(c))-1]
      print store
      
      for j in range(0,int(len(SplitA)),1):  
        pat = "t1 *= *\""
        string = SplitA[j]
        match = re.search(pat,string)
        if match:
          d = SplitA[j].split("\"")
          Mold = d[1]
          print Mold
          dir_name = Mold+"_"+store
          print dir_name
          NetPath = r"\\192.168.120.8\Public\Bug&Request\Bug\147001-148000\147891"
          dir_name = NetPath+"\\"+dir_name
          if not os.path.exists(dir_name):    
           os.makedirs(dir_name)
           #Copy feature file
           FeaturePath = 'C:\\WorkingFolder\\testCase\\ManualFeatureTable.txt'
           FeaturePath = FeaturePath.replace("\\","/")
           shutil.copy(FeaturePath,dir_name)
# 自動測試使用
def CheckLog(siteForLog,siteForStatus,SpecialCase):
  CheckMDX3DRunJob(siteForStatus)
  # 把版號寫入特徵表中
  mdxVersion = ReadMoldexVersion_py27.AutoReadMoldexVersion()
  FeatureOutPut.WriteOutPut("MDXVersion",mdxVersion)
  #產出特徵表
  FeatureOutPut.WriteResult()
  
  #----0615----
  CreateDir()
  #比對兩份特徵表內容
  #Result = CompareFeature.AnalysisResult()
  Result = "Successful"
  return Result
  #----0615----
  
#表示為手動去觸發特徵工具產生特徵表
if __name__ == '__main__':
  CreateDir()
elif __name__ == 'InPutLog':
  print "Import!!!"
