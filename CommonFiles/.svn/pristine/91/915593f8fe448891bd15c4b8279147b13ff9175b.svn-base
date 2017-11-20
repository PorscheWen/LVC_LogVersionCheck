#-*- coding: utf-8 -*-　
import time
import os
import re
from threading import Thread
Killcommand = "taskkill /f /t /im WerFault.exe"

def CheckCrashProcessIsLive(ProcessName):
  ISLive = False
  #找程式並存成List
  Listcommand = os.popen("tasklist |find "+"\""+ProcessName+"\"").read().split('\n')
  #依照空格去切割List
  Listcommand = Listcommand[0].split(" ")
  #刪除List中index之值為空白的元素
  Listcommand =[i for i in Listcommand if i!='']
  #沒有找到 WerFault.exe(即無Crash)
  if len(Listcommand) == 0:
    print "Cannot FIND!"
    ISLive = False
    return ISLive
  else:
    #找到 WerFault.exe(即有Crash)
    #print len(Listcommand)
    if Listcommand[0] == ProcessName:
      print "FIND!"
      ISLive = True
      return ISLive

def CreateMDXdata():
  fileMDXdata = open(r'C:\WorkingFolder\testCase\MDXdata.ini', 'w')
  fileMDXdata.write("None")
  fileMDXdata.close()
  
def OverWriteMDXData():
# change ini  (BOWEN)
  fileR = open(r'C:\WorkingFolder\testCase\MDXdata.ini', 'r')
  MDXcontent = fileR.read()
  fileR.close()
  #表示發生過crash
  if "Fail" in MDXcontent:
    print "Ever Crash!!"
  #無發生Crash,把中繼檔寫入Done
  else:
    fileMDXdata = open('C:\\WorkingFolder\\testCase\\MDXdata.ini', 'w')
    print "Start to write done"
    fileMDXdata.write("Done")
    fileMDXdata.close()

def RunScriptTime(StartTime,EndTime):
  TotalRunScriptTime = EndTime-StartTime
  RunScriptTimeStr = "Total RunScript Time: "+str(int(TotalRunScriptTime))+" (s)"
  #Create time.txt
  Tfile = open('C:\\WorkingFolder\\testCase\\RunScriptTime.txt', 'w')
  Tfile.write(RunScriptTimeStr)
  Tfile.close()
  
def KillCrashAgain():
  KillcommandNum = os.system(Killcommand)
  
def CheckCrash(checkCrashMark):
    while checkCrashMark == "0":
        file = open(r'C:\WorkingFolder\testCase\MDXdata.ini', 'r')
        MDXcontent = file.read()
        file.close()
        if "None" in MDXcontent:
          ISLive = CheckCrashProcessIsLive("WerFault.exe")
          #無發生crash,等2秒後再繼續偵測
          if ISLive == False:
            time.sleep(5)
          #發生crash,刪除Crash視窗
          elif ISLive == True:
            KillcommandNum = os.system(Killcommand)
            #print KillcommandNum 
            #KillcommandNum=0 means kill the WerFault.exe;KillcommandNum's type is int not String
            if KillcommandNum == 0:
              print("Crashing!!!! Has Killed WerFault.exe")
              #Write "Failed" to MDXdtat ini
              file = open(r'C:\WorkingFolder\testCase\MDXdata.ini', 'w')
              print("Start to Write Fail")
              file.write("Done,Fail")
              print("Stop Write Fail")
              file.close()
              #再多檢查一次看是否還有Crash視窗
              ISLive = CheckCrashProcessIsLive("WerFault.exe")
              if ISLive == True:
                print "AGAIN"
                KillCrashAgain()
                checkCrashMark = "1"
              else:
                checkCrashMark = "1"
                print ("All WerFaults had been killed and no WerFault need to check!")
        #停止偵測crash
        elif "Done" in MDXcontent:
          print "123"
          checkCrashMark = "1"

    print "STOP!!!"

#define the function which wiil be called by thread
def myCheckCrashFunction():
  CheckCrash("0")

#define the Thread function  
def StartToCallmyCheckCrashFunction():
  myThread01 = Thread(target=myCheckCrashFunction, name="myThread01") 
#myThread01.setDaemon(True)    
  myThread01.start()
