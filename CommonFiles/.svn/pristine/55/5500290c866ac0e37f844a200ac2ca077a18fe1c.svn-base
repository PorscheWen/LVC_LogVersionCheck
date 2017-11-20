# -*- coding: UTF-8 -*-
import os 
import time
import win32com.client
import win32com.client.dynamic


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


def Record_PPT_Item(OutputType, pptReportPath, ppt_Record_Path):
    
    App = win32com.client.Dispatch("PowerPoint.Application")
    App.Visible = 1
    presentation = App.Presentations.Open(pptReportPath)
    
    # Read the page counts in the PPT file
    page_Count = presentation.Slides.Count
    
    page_Count_Log = "Page_counts_in_the_PPT: {}".format(page_Count)
    with open(ppt_Record_Path, "w") as ppt_Record:
        ppt_Record.write(page_Count_Log + "\n") 
    
    for i in range(2, page_Count + 1):
        # Read the shape counts in the specific page
        pageSlides = presentation.Slides(i)
        shape_Count = pageSlides.Shapes.Count
        
        shape_Count_Log = "\nShape_counts_in_page_{}: {}".format(i, shape_Count)
        with open(ppt_Record_Path, "a") as ppt_Record:
            ppt_Record.write(shape_Count_Log + "\n") 
        
        # Read the page title text
        title_shape_Text = pageSlides.Shapes(1).TextFrame.TextRange.Text
            
        for j in range(1, shape_Count + 1):
            shape = pageSlides.Shapes(j)
            if j > 1:
                pre_shape = pageSlides.Shapes(j - 1)
            
            # [Text objects] in shape
            if shape.HasTextFrame: 
                shape_Text = shape.TextFrame.TextRange.Text
                
                # Page title attribute
                if "Title" in shape.Name:
                    shape_Result = "Page_Title : {}".format(shape_Text)
                # Else text objects
                else:
                    if title_shape_Text == "Summary" or "Summary -" in title_shape_Text: 
                        shape_Result = "Table_name : {}".format(shape_Text)
                    else:
                        shape_Result = "Item_remark : {}".format(shape_Text.replace("\r", " ").replace("\n", " "))
            
            # [Table objects] in shape
            elif shape.HasTable:
                if title_shape_Text == "Summary" or "Summary -" in title_shape_Text: 
                    pre_shape_Text = pre_shape.TextFrame.TextRange.Text
                    shape_Result = "Table_object : {}__Table".format(pre_shape_Text)
                    if OutputType == "PowerPointComp":
                        for k in range(2, 6):
                            runID_Text = shape.Table.Cell(1, k).Shape.TextFrame.TextRange.Text
                            shape_Result = "{}\nTable_text : {}".format(shape_Result, runID_Text)
                else:
                    table_Cell_1_1_Text = shape.Table.Cell(1, 1).Shape.TextFrame.TextRange.Text
                    shape_Result = "Table_name : {}".format(table_Cell_1_1_Text)
            
            # [Picture objects] in shape    
            elif "Picture" in shape.Name: 
                shape_Result = "Table_object : {}__Picture".format(pre_shape.Table.Cell(1, 1).Shape.TextFrame.TextRange.Text)
            
            with open(ppt_Record_Path, "a") as ppt_Record:
                ppt_Record.write(shape_Result + "\n") 
        
    #App.Quit()

if __name__ == "__main__":
    
    OutputType = raw_input()
    #OutputType = "PowerPoint"
    
    # Read project name & combine to Site_Project
    testModelPath = r"C:\WorkingFolder\testCase\testModel"
    projectNameList = os.listdir(testModelPath)
    for name in projectNameList:
        if os.path.isdir(r"{}\{}".format(testModelPath, name)) == 1:
            projectName = name
    Site_Project = r"{}\{}".format(testModelPath, projectName)
    
    # Read run ID in the project
    if OutputType == "PowerPoint":
        RunIDList = AutoReadRunID(Site_Project) 
    elif OutputType == "PowerPointComp":
        RunIDList = ["01"]    

    # Start record text from PPT file
    for ID in RunIDList:
        pptReportPath = r"{}\Report\PPT Report\Run{runID}\PPT Report-Run{runID}.ppt".format(Site_Project, runID = ID)
        ppt_Record_Path = pptReportPath.replace(".ppt", ".txt")
        Record_PPT_Item(OutputType, pptReportPath, ppt_Record_Path)
    
    # Waiting record
    waitting_Time= 0
    while os.path.exists(r"{}\Report\PPT Report\Run{runID}\PPT Report-Run{runID}.ppt".format(Site_Project, runID = RunIDList[-1])) == 0:
        time.sleep(1)
        waitting_Time += 1
        if waitting_Time > 180:
            print("Record PowerPoint_to_text...Failed !")
        
    print("Record PowerPoint_to_text... done.")
    