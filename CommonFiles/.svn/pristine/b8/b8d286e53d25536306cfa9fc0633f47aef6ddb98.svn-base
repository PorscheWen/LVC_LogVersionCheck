import time
import os


def CheckLog(site1,site2,SpecialCase):
  if SpecialCase == "0":
  # check analysis done or not
    if os.path.exists(site1) == True:
      f = open(site1)
      file_data = f.read()
      f.close()
      checkDone = 'Done!' in file_data
      if checkDone == True:
        Result = "Successful"
      else:
        Result = "Failed"
        return Result
    else:
      Result = "Failed"
      return Result
      
  # check analysis status(error or warning)
    if os.path.exists(site2) == True:
      f = open(site2)
      file_data = f.read()
      f.close()
      checkError = 'ERROR' in file_data
      if checkError == False:
        Result = "Successful"
      else:
        Result = "Failed"
        return Result
      checkWarning = 'WARNING' in file_data
      if checkWarning == False:
        Result = "Successful"
      else:
        Result = "Failed"
        return Result
    else:
      Result = "Failed"
      return Result
    
    return Result
  
  elif SpecialCase == "1":
    #Log.Message("Suppose it is an exception")
    #check analysis done or not
    if os.path.exists(site1) == True:
      f = open(site1)
      file_data = f.read()
      f.close()
      checkDone = 'Done!' in file_data
      if checkDone == True:
        Result = "Successful"
      else:
        print (">>> Check Done Failed...")
        Result = "Failed"
        return Result
    else:
      print (">>> Job Log file not exist...")
      Result = "Failed"
      return Result
      
  # check LGF analysis status(error or warning)
    if os.path.exists(site2[0]) == True:
      f = open(site2[0])
      file_data = f.read()
      f.close()
      checkError = 'ERROR' in file_data
      if checkError == False:
        Result = "Successful"
      else:
        print (">>> Check ERROR Failed")
        Result = "Failed"
        return Result
      checkWarning = 'WARNING' in file_data
      if checkWarning == False:
        Result = "Successful"
      else:
        print (">>> Check WARNING Failed")
        Result = "Failed"
        return Result
    else:
      print (">>> Solver Log file not exist...")
      Result = "Failed"
      return Result
   # check LGC analysis status(error or warning)
    if os.path.exists(site2[1]) == True:
      f = open(site2[1])
      file_data = f.read()
      f.close()
      checkError = 'ERROR' in file_data
      if checkError == False:
        Result = "Successful"
      else:
        print (">>> Check ERROR Failed")
        Result = "Failed"
        return Result
      checkWarning = 'WARNING' in file_data
      if checkWarning == False:
        Result = "Successful"
      else:
        print (">>> Check WARNING Failed")
        Result = "Failed"
        return Result
    else:
      print (">>> Solver Log file not exist...")
      Result = "Failed"
      return Result   

   # check LGW analysis status(error or warning)
    if os.path.exists(site2[2]) == True:
      f = open(site2[2])
      file_data = f.read()
      f.close()
      checkError = 'ERROR' in file_data
      if checkError == False:
        Result = "Successful"
      else:
        print (">>> Check ERROR Failed")
        Result = "Failed"
        return Result
      checkWarning = 'WARNING' in file_data
      if checkWarning == False:
        Result = "Successful"
      else:
        print (">>> Check WARNING Failed")
        Result = "Failed"
        return Result
    else:
      print (">>> Solver Log file not exist...")
      Result = "Failed"
      return Result   
    
    return Result    
