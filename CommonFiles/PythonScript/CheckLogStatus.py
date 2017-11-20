
class CheckSpecialCase(object):
    __SpecialCaseNum_Dict = {"2":"WARNING  W111550",
                             "3":"WARNING  W111545",
                             "4":"WARNING  W132005"}
    def __init__(self, siteForStatus, SpecialCase, siteForLog, isCheckMultiLog=False):
        self.siteForStatus = siteForStatus
        self.SpecialCase = SpecialCase
        self.isCheckMultiLog = isCheckMultiLog
        self.siteForLog = siteForLog
    def StartToCheckLog(self):
        if self.isCheckMultiLog:
            Result = self.CheckMultiAnalysisLog()
            print Result
            return Result
        elif not self.isCheckMultiLog:
            with open(siteForStatus, "r") as CheckAnalysisLog_F:
                CheckAnalysisLog_data = CheckAnalysisLog_F.read()
                self.CheckAnalysisLog_data = CheckAnalysisLog_data
            Result = self.CheckSingleAnalysisLog()
            return Result

    def CheckMDX3DRunJob(self):
        print "Start CheckMDX3DRunJob!"
        #check analys is done or not
        try:
            with open(self.siteForLog, "r") as MDX3DRunJob_F:
                MDX3DRunJob_data = MDX3DRunJob_F.read() 
            KeyWord = ["Cancel","Error" ,"Warning"]
            if all(w not in MDX3DRunJob_data for w in KeyWord) and "Done" in MDX3DRunJob_data:
                print "Successful: Find MDX3DRunJob!"
                return "Successful"
            else:
                print "Fail: MDX3DRunJob is Error!"
                return "Failed"
        except IOError:
            print "XXX Check MDX3DRunJob is Fail !!"   
            return "Failed"
            
    def CheckSingleAnalysisLog(self):
        Result = CheckIsErrorOrNot()
        Result = CheckIsWarningOrNot()
    
    def CheckMultiAnalysisLog(self):
        print "Start CheckFullCoupleAnalysisLog!"
        logtype = [".lgf", ".lgc", ".lgw"]
        for i in logtype:
            var_New_siteForStatus = self.siteForStatus.split(".", 1)
            var_New_siteForStatus = var_New_siteForStatus[0]+i
            with open(var_New_siteForStatus, "r") as CheckAnalysisLog_F:
                CheckAnalysisLog_data = CheckAnalysisLog_F.read()
                self.CheckAnalysisLog_data = CheckAnalysisLog_data
                Result = self.CheckIsErrorOrNot()
                if Result == "Successful":
                    Result = self.CheckIsWarningOrNot()
                else:
                    return Result
        return Result

    def CheckIsErrorOrNot(self):
        checkError = 'ERROR' in self.CheckAnalysisLog_data
        if not checkError:
            return "Successful"
        else:
            #print "Finding ERROR in log!"
            return "Failed"
            
    def CheckIsWarningOrNot(self):
        if not self.SpecialCase:
            checkWarning = 'WARNING' in self.CheckAnalysisLog_data
            if not checkWarning:
                return "Successful"
            else:
                return "Failed"
        elif self.SpecialCase:
            for var_specialcasenum in SpecialCaseList:
                for i in self.__SpecialCaseNum_Dict:
                    if i == var_specialcasenum:
                        for num, line in enumerate(self.CheckAnalysisLog_data, 1):
                            if "WARNING" in line:
                                print 'found WARNING at line:', num
                                if self.__SpecialCaseNum_Dict[i] in line:
                                    pass
                                else:
                                    return "Failed"
        return "Successful"

if __name__ == '__main__':
    pass














