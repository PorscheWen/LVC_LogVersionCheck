import time
import os


def CheckLog(site1,site2,Exception):
  if Exception == "0":
  # check analysis done or not
    if os.path.exists(site1) == True:
      f = open(site1)
      file_data = f.read()
      f.close()
      checkDone = 'Done!' in file_data
      if checkDone == True:
        Log.Message("Check Analysis Done!")
      else:
        Log.Error("Test Fail!")
    else:
      Log.Error("Test Fail!")
      
  # check analysis status(error or warning)
    if os.path.exists(site2) == True:
      f = open(site2)
      file_data = f.read()
      f.close()
      checkError = 'ERROR' in file_data
      if checkError == False:
        Log.Message("Check no Error!")
      else:
        Log.Error("Test Fail!(checkError)")
      checkWarning = 'WARNING' in file_data
      if checkWarning == False:
        Log.Message("Check no Warning!")
      else:
        Log.Error("Test Fail!")
    else:
      Log.Error("Test Fail!")  
  
  elif Exception == "1":
    Log.Message("Suppose it is an exception")
    
