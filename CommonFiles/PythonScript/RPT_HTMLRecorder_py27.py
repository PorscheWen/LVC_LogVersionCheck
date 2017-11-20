import os, time, urllib2
from HTMLParser import HTMLParser

def AutoReadRunID(Site_Project):
    RunIDList = []
    site_Analysis = Site_Project + r"\Analysis"
    for site, folder, files in os.walk(site_Analysis): 
        for ID in folder:
            if ID[0:3] == "Run":
                RunIDList.append(ID[3:5]) 
    if len(RunIDList) == 4:
        return(RunIDList[0:2])
    else:
        return(RunIDList)


def GetAnalysizeStep(projectName):
    projectName_dict = {"SolidAHR"  : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics", "_Hot Runner Steady"],
                        "SolidBiIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidCFM"  : ["_Filling", "_Cooling", "_Warpage"],
                        "SolidCM"   : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics"],
                        "SolidCoIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidGAIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidEncapsulation" : ["_Filling", "_Cooling","_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Curing", "_Paddle Shift"],
                        "SolidICCM" : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Paddle Shift"],
                        "SolidICM"  : ["_Filling_Packing", "_Cooling", "_Warpage", "_Stress", "_Optics"],
                        "SolidIM"   : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Optics", "_Mold Deformation"],
                        "SolidMCIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "SolidPIM"  : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "SolidRIM"  : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Curing"],
                        "SolidRTM"  : ["_Filling_Curing"],
                        "SolidWAIM" : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "eDesignPIM" : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "eDN-RIM"    : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Curing"],
                        "eDesignAHR" : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress"],
                        "eDN-CFM"    : ["_Filling", "_Cooling", "_Warpage"],
                        "eDesignCM"  : ["_Filling", "_Cooling","_Mold Preheat", "_Warpage","_Stress"],
                        "eDesign IC" : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep", "_Curing"],
                        "eDN-ICCM"   : ["_Filling", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress", "_Wire Sweep"],
                        "eDN-IM"     : ["_Filling", "_Packing", "_Cooling", "_Mold Preheat", "_Warpage", "_Stress"],
                        "eDN-MCIM"   : ["_Filling_Packing", "_Cooling", "_Warpage"],
                        "Shell_GAIM" : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "Shell_IM"   : ["_Filling", "_Packing", "_Cooling", "_Warpage"],
                        "Shell_RIM"  : ["_Filling", "_Curing"]
                       } 
    analysize_step = projectName_dict.get( projectName, 0)
    analysize_step.insert(0, "_Model")
    return analysize_step


def ChangeToHTMLStep( projectName, analysize_step):
    originalStepList = [ "_Model", "_Filling", "_Packing", "_Curing", "_Filling_Packing", "_Filling_Curing", "_Cooling", "_Warpage", "_Optics", "_Paddle Shift", "_Wire Sweep"]
    htmlStepList     = [ "_Mesh", "_Flow", "_Pack", "_Cure", "_Flow", "_Flow", "_Cool", "_Warp", "_Optic", "_PaddleShift", "_WireSweep"]
    html_step = ["_Report"]
    for i in analysize_step: 
        if i in originalStepList:
            iindex = originalStepList.index(i)
            html_step.append(htmlStepList[iindex])
        else:
            html_step.append(i)
    if projectName == "eDesign IC" or projectName == "SolidEncapsulation":
        html_step.remove( "_Cure")
        html_step.append( "_Pack")    
    return html_step


# Record result item in each analysis step from HTML into text
def RecordHTMLItem( Site_Project, OutputType, RunIDList, htmlReport_step):
    
    # Build record folder 
    isExists = os.path.exists( Site_Project + r"\Report\HTML Report\Testing_Result")
    if not isExists:
        os.makedirs( Site_Project + r"\Report\HTML Report\Testing_Result")
    
    for ID in RunIDList: 
        for ResultName in htmlReport_step:
            htmlReportPath_0 = "{}\Report\HTML Report\Run{}\Run{}.htm".format(Site_Project, ID, ID + ResultName)
            if os.path.exists(htmlReportPath_0) == 1:
                
                class Label_CAPTION_List(HTMLParser):
                    is_label = ""
                    name = []
                    def handle_starttag(self, tag, attrs):
                        if tag == "caption":
                            self.is_label = 1
                    def handle_endtag(self, tag):
                        if tag == "caption":
                            self.is_label = ""
                    def handle_data(self, data):
                        if self.is_label:
                            self.name.append(data) 
                
                class Label_A_List(HTMLParser):
                    is_label=""
                    name=[]    
                    def handle_starttag(self, tag, attrs):
                        if tag == "a":
                            self.is_label = 1
                    def handle_endtag(self, tag):
                        if tag == "a":
                            self.is_label= ""
                    def handle_data(self, data):
                        if self.is_label:
                            self.name.append(data) 
  
                class Label_TH_List(HTMLParser):
                    is_label = ""
                    name = []
                    def handle_starttag(self, tag, attrs):
                        if tag == "th":
                            self.is_label = 1
                    def handle_endtag(self, tag):
                        if tag == "th":
                            self.is_label = ""
                    def handle_data(self, data): 
                        if self.is_label:
                            self.name.append(data) 
                
                class Label_TD_List(HTMLParser):
                    is_label=""
                    name=[]
                    def handle_starttag(self, tag, attrs):
                        if tag == "td":
                            self.is_label = 1
                    def handle_endtag(self, tag):
                        if tag == "td":
                            self.is_label=""
                    def handle_data(self, data): 
                        if self.is_label:
                            self.name.append(data) 
                
                class Label_IMG_SRC_List(HTMLParser):
                    def __init__(self):
                        HTMLParser.__init__(self)
                        self.links = []
                 
                    def handle_starttag(self, tag, attrs):
                        if tag == "img":
                            if len(attrs) == 0: 
                                pass
                            else:
                                for (variable, value)  in attrs:
                                    if variable == "src":
                                        self.links.append(value) 
                
                htmlReportPath = r"file:///{}#".format(htmlReportPath_0)
                content = urllib2.urlopen(htmlReportPath).read().decode('UTF-8')
                
                # Step1: Item
                if ResultName == "_Report":
                    # Catch summary item from label_Caption
                    labelCAPTION = Label_CAPTION_List()
                    labelCAPTION.feed(content)
                    # Catch material & process item from label_TH 
                    labelTH = Label_TH_List()
                    labelTH.feed(content)
                    
                    graphItem = []
                    for item in labelTH.name:
                        if "-Material " in item or "-Process " in item:
                            graphItem.append(item[6:])
                    result = labelCAPTION.name + graphItem 
                
                else:
                    # Catch all Label_A in current result step
                    labelA = Label_A_List()
                    labelA.feed(content)
                    
                    result=[]
                    reportStart = labelA.name.index("1. Table of content") 
                    for item in labelA.name[reportStart + 2:]:
                        if "2. " in item:
                            break
                        else:
                            result.append(item) 
                
                # Record items from HTML into text
                recordPath = r"{}\Report\HTML Report\Testing_Result\Run{}.txt".format(Site_Project, ID + ResultName)
                with open(recordPath, "w") as reportItem:
                    for i in result:
                        reportItem.write( i.strip() + "\n") 
                
                
                # Step 2: Remarks & statistics plot
                if OutputType == "HTML":
                    if ResultName not in ["_Report", "_Mesh"]:
                        # Label TD for HTML remark
                        labelTD = Label_TD_List()
                        labelTD.feed(content)
                        
                        remarkResult = []
                        stopPoint = labelTD.name.index("Copyright ") - 1
                        for item in labelTD.name[:stopPoint]:
                            remarkResult.append(item.replace("\r", " ").replace("\n", " ")) 
                        
                        # Label TH for HTML statistics plot
                        labelTH = Label_TH_List() 
                        labelTH.feed(content) 
                        
                        statPlotResult = []
                        for item in labelTH.name:
                            if item == "Statistics plot" or item not in statPlotResult:
                                statPlotResult.append(item)  
                        
                        # Record remarks from HTML into text
                        recordPath_remark = r"{}\Report\HTML Report\Testing_Result\Run{}-Remark.txt".format(Site_Project, ID + ResultName)
                        with open(recordPath_remark, "w") as reportRemark:
                            for i in remarkResult:
                                reportRemark.write( i.strip() + "\n")                        

                        recordPath_StatPlot = r"{}\Report\HTML Report\Testing_Result\Run{}-StatisticsPlot.txt".format(Site_Project, ID + ResultName)
                        with open(recordPath_StatPlot, "w") as reportStatPlot:
                            for i in statPlotResult:
                                reportStatPlot.write( i.strip() + "\n")  
                
                elif OutputType == "HTMLComp":
                    if ResultName != "_Report":
                        # Label TH for HTML remark & statistics plot
                        labelTH = Label_TH_List() 
                        labelTH.feed(content) 
                        
                        remarkResult = []
                        for item in labelTH.name:
                            remarkResult.append(item.replace("\r", " ").replace("\n", " "))  
                        
                        recordPath_remark = r"{}\Report\HTML Report\Testing_Result\Run{}-StatisticsPlot_Remark.txt".format(Site_Project, ID + ResultName) 
                        
                        with open(recordPath_remark, "w") as reportRemark:
                            for i in remarkResult:
                                reportRemark.write( i.strip() + "\n")     
                
                
                # Step 3: Image links
                # Label img src for HTML links
                labelLink = Label_IMG_SRC_List()
                labelLink.feed(content) 
                
                # Record links from HTML into text
                recordPath_link = r"{}\Report\HTML Report\Testing_Result\Run{}-Link.txt".format(Site_Project, ID + ResultName)
                with open(recordPath_link, "w") as reportLink:
                    for i in labelLink.links:
                        reportLink.write( i.strip() + "\n") 


if __name__ == '__main__':
    
    OutputType = raw_input()
    
    # Read project name & combine to Site_Project
    testModelPath = r"C:\WorkingFolder\testCase\testModel"
    projectNameList = os.listdir(testModelPath)
    for name in projectNameList:
        if os.path.isdir(r"{}\{}".format(testModelPath, name)) == 1:
            projectName = name
    Site_Project = r"{}\{}".format(testModelPath, projectName)
    '''
    #OutputType = "HTML"
    #Site_Project = r"C:\Users\Administrator\Desktop\WAIM\SolidWAIM001-HTML\SolidWAIM"
    OutputType = "HTMLComp" 
    Site_Project = r"C:\Users\Administrator\Desktop\HTMLComp_Report\SolidWAIM"
    projectName = os.path.basename(Site_Project)
    '''
    
    if OutputType == "HTML":
        RunIDList = AutoReadRunID(Site_Project) 
    elif OutputType == "HTMLComp":
        RunIDList = ["01"]
    
    # Read project analysize_step
    analysize_step = GetAnalysizeStep( projectName)
    
    # Read project html_step
    htmlReport_step = ChangeToHTMLStep( projectName, analysize_step)
    
    # Record all items in Project
    RecordHTMLItem( Site_Project, OutputType, RunIDList, htmlReport_step)
    
    while os.path.exists(Site_Project + r"\Report\HTML Report\Testing_Result") == 0:
        time.sleep(1)
    
    time.sleep(3)
