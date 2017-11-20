#-*- coding: utf-8 -*-　
import math

SplitA = []
SplitB = []

def AnalysisResult():
  global SplitA, SplitB
# initial 
  fileA = open('C:\\WorkingFolder\\testCase\\ManualFeatureTable.txt', 'r')
  A = fileA.read()
  SplitA = A.split('\n')
  fileB = open('C:\\WorkingFolder\\testCase\\AutoTestFeatureTable.txt', 'r')
  B = fileB.read()
  SplitB = B.split('\n')
  fileA.close()
  fileB.close()
# AnalysisResult
  x = SplitA[1]
  x = x.split(': ')
  y = SplitB[1]
  y = y.split(': ')
  if x[1] != y[1]:
    #print"error"
    Result = "Failed"
    return Result
  else:
    Result = CheckWarning()
    return Result
    
def CheckWarning():
  y = SplitB[2]
  y = y.split(': ')
  if y[1] == "No":
    Result = CheckError()
    return Result
  else:
    Result = "Failed"
    return Result
    
def CheckError():
  y = SplitB[4]
  y = y.split(': ')
  if y[1] == "No":
    Result = CompareReCalculate()
    return Result
  else:
    Result = "Failed"
    return Result

def CompareReCalculate():
  x = SplitA[6]
  x = x.split(': ')
  y = SplitB[6]
  y = y.split(': ')
  if y[1] == "No":
    Result = CompareTotalStepNum()
    return Result
  else:
    Result = "Failed"
    return Result
      
def CompareTotalStepNum():
  x = SplitA[7]
  x = x.split(': ')
  y = SplitB[7]
  y = y.split(': ')
  if "The Flow Step Error at NO" in x[1] or "The Flow Step Error at NO" in y[1]:
    Result = "Failed"
    return Result
  if x[1] == y[1]:
    Result = CompareCycleNum_C()
    return Result
    #print "OK"
  else:
    if x[1] == "--" or y[1] == "--":
      #print "error"
      Result = "Failed"
      return Result
    else:
        numA = round(float(x[1])+(float(x[1])/10)) 
        numB = round(float(x[1])-(float(x[1])/10)) 
        if numB <= float(y[1]) <= numA:
          Result = CompareCycleNum_C()
          return Result
          #print "OK!"
        else:
          #print "error"
          Result = "Failed"
          return Result
          
def CompareCycleNum_C():
  x = SplitA[8]
  x = x.split(': ')
  y = SplitB[8]
  y = y.split(': ')
  #Cycle Num要相同才算PASS
  if x[1] == y[1]:
    Result = CompareCycleStepNum_C()
    return Result
  else:
    Result = "Failed"
    return Result
    
# 步數誤差10%
def CompareCycleStepNum_C():
  x = SplitA[9]
  x = x.split(': ')
  y = SplitB[9]
  y = y.split(': ')
  if x[1] == "Error at FeatureMethod.py" or y[1] == "Error at FeatureMethod.py":
    Result = "Failed"
    return Result
  if x[1] == y[1]:
    Result = CompareCycleNum_Ct()
    return Result
    #print "OK"
  else:
    if x[1] == "--" or y[1] == "--":
      #print "error"
      Result = "Failed"
      return Result
    else:
        numA = round(float(x[1])+(float(x[1])/10)) 
        numB = round(float(x[1])-(float(x[1])/10)) 
        if numB <= float(y[1]) <= numA:
          Result = CompareCycleNum_Ct()
          return Result
          #print "OK!"
        else:
          #print "error"
          Result = "Failed"
          return Result
      
def CompareCycleNum_Ct():
  x = SplitA[10]
  x = x.split(': ')
  y = SplitB[10]
  y = y.split(': ')
  if x[1] == "Error at FeatureMethod.py" or y[1] == "Error at FeatureMethod.py":
    Result = "Failed"
    return Result
  if x[1] == y[1]:
    Result = CompareCycleStepNum_Ct()
    return Result
  else:
      Result = "Failed"
      return Result

def CompareCycleStepNum_Ct():
  x = SplitA[11]
  x = x.split(': ')
  y = SplitB[11]
  y = y.split(': ')
  if x[1] == y[1]:
    Result = CompareFillPercentageDiscontinuous()
    return Result
    #print "OK"
  else:
    if x[1] == "--" or y[1] == "--":
      #print "error"
      Result = "Failed"
      return Result
    else:
        numA = round(float(x[1])+(float(x[1])/10)) 
        numB = round(float(x[1])-(float(x[1])/10)) 
        if numB <= float(y[1]) <= numA:
          Result = CompareFillPercentageDiscontinuous()
          return Result
          #print "OK!"
        else:
          #print "error"
          Result = "Failed"
          return Result

def CompareFillPercentageDiscontinuous():
  x = SplitA[12]
  x = x.split(': ')
  y = SplitB[12]
  y = y.split(': ')
  if x[1] != y[1]:
    #print"error"
    Result = "Failed"
    return Result
  else:
    if y[1] == "Yes":
      #print"error"
      Result = "Failed"
      return Result
      #兩者皆為預設值或皆沒有發生不連續之情形
    else:
      Result = DiscontinuousAtStepNum()
      return Result

def DiscontinuousAtStepNum():
  x = SplitA[13]
  x = x.split(': ')
  y = SplitB[13]
  y = y.split(': ')
  if x[1] == y[1]:
    Result = "Successful"
    return Result
  else:
    if x[1] == "--" or y[1] == "--":
      Result = "Failed"
      return Result
    else:
        numA = round(float(x[1])+(float(x[1])/10)) 
        numB = round(float(x[1])-(float(x[1])/10)) 
        if numB <= float(y[1]) <= numA:
          Result = "Successful"
          return Result
        else:
          Result = "Failed"
          return Result














