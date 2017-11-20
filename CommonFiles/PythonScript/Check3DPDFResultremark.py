from My3DPDFtools.pdfminer.pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from My3DPDFtools.pdfminer.pdfminer.converter import TextConverter
from My3DPDFtools.pdfminer.pdfminer.layout import LAParams
from My3DPDFtools.pdfminer.pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os


# Convert PDF to txt using My3DPDFtools, return the whole content
def convert(fname, pages = None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams = LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return(text)


# Read the result title from the text
def TXTread(txtLocation):
    # difpage: Record the line number with "\x0c" mark
    # lineCount: Record how many line in the file.txt    
    difpage = []
    lineCount = 0
    with open(txtLocation, 'r') as fileRead:
	txtTemplage = fileRead.read().split('\n')
    
    for line in txtTemplage:
	if "\x0c" in line:
	    difpage.append(lineCount)
	lineCount += 1
    
    # first_Line_Number_List: Record the first line number in each page, Given an initial number 0 and delete the last line number 
    # last_Line_Number_List : Record the last line number in each page    
    first_Line_Number_List = [0]
    last_Line_Number_List = []    
    for i in difpage:
        first_Line_Number_List.append(i + 1)
        last_Line_Number_List.append(i)
    first_Line_Number_List.pop()
    
    Title_results = []
    for j in range(0, len(difpage)):
        frontnumber = first_Line_Number_List[j]
        backnumber = last_Line_Number_List[j]
	
        pageRange_0 = txtTemplage[frontnumber : backnumber]
        pageRange = list(filter(lambda x:x !='', pageRange_0))
	
        Title_results.append(pageRange[0].strip()) # Record: pageRange[0] = page title
    
    return(Title_results)


# Given the content in single page, and get the remark string
def Record_remark_in_One_Page(content_One_Page):
    pageTemp = content_One_Page.split('\n')
    ResultremarkStart = pageTemp.index('Result remark')
    count1 = 0
    
    for x in pageTemp[ResultremarkStart + 1 : ]:
        if x == '':
            ResultremarkEnd = ResultremarkStart + count1
            #count1 += 1
            break
        else:
            count1 += 1
    
    # Print ResultremarkEnd
    str1 = pageTemp[ResultremarkStart + 1 : ResultremarkEnd + 1]
    total_Remark = ''
    
    for line in str1:
        bbc = str(line)
        total_Remark = total_Remark + bbc

    return(total_Remark)


if __name__ == "__main__":
    #Site_Projecttest = r"C:\WorkingFolder\testCase\testModel\SolidWAIM"
    #str1 = Site_Projecttest + '@@' + '01'
    str1 = raw_input()
    dic1 = {}
    [Site_Project, ID] = str1.split('@@')
    
    folder_path = Site_Project + r"\Report\PDF Report\Testing_Result"
    projectName = os.path.basename(Site_Project)
    
    site_PDF = r"{}\Report\PDF Report\Run{runID}\PDF Report-Run{runID}.pdf".format(Site_Project, runID = ID)
    site_TXT = site_PDF.replace(".pdf", ".txt")
    Title_results = TXTread(site_TXT)
    
    # Make a folder to save Result remark
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    foutName = folder_path + '\\' + 'temp.ini'
    fout = open(foutName, 'w')         
    
    # Convert pdf to txt    
    a = convert(site_PDF)
    eachPage = a.split('\x0c')
    totalPage = len(eachPage) - 1
   
    for x in range(0, totalPage):
        if "Result remark" in eachPage[x]:
            Result_remark_temp = Record_remark_in_One_Page(eachPage[x])
            dic1[Title_results[x].strip()] = Result_remark_temp.strip()
            
    first_Line = '[Root]\n'
    secont_Line = '[' + projectName + ']\n'
    fout.write(first_Line)
    fout.write(secont_Line)
    
    for key in Title_results:
        if key in dic1:
            Result_remark_str = key + ' = ' + dic1[key] + '\n'
            fout.write(Result_remark_str)

    fout.close()
