# -*- coding: utf-8 -*-
import os
import openpyxl
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.styles import colors

pathSrcXlsx = r"C:\WorkingFolder\testCase\testModel\Sample.xlsx"


class UnifyStatsData:

    def __init__(self):
        """
        Load & active source xlsx
        Setting style format
        """
        self.wb = load_workbook(pathSrcXlsx)
        self.wb.active
        self.lstSheetName = self.wb.get_sheet_names()[1:]
        self.ft = Font(name="微軟正黑體".decode("utf-8"),
                       size=12, color=colors.BLACK)
        self.al = Alignment(horizontal="center", vertical="center")
        self.bg = PatternFill(
            fill_type="solid", start_color="B7DEE8", end_color="B7DEE8")
        self.er = PatternFill(
            fill_type="solid", start_color=colors.YELLOW, end_color=colors.YELLOW)
        # Deep Gray
        self.ver1 = PatternFill(
            fill_type="solid", start_color="BFBFBF", end_color="BFBFBF")
        # light Gray
        self.ver2 = PatternFill(
            fill_type="solid", start_color="F2F2F2", end_color="F2F2F2")

    def Unifying(self):
        # lstSheetName = ["Cell Phone", "Dashboard", "Front Cover", "Bumper", "Metal",
        #                 "Recharger cover", "Specimen", "Mobile Phone Cover", "Medical box",
        #                 "Keypad", "Fan", "Fishing Buoy", "Turbocharger",  "Disk","Handle-gas",
        #                 "IC", "Head set", "Plates", "Handle", "Screw Driver", "Multi-component",
        #                 "Lens", "Lampholder", "Gear"]
        for sheet in self.lstSheetName:
            self.ws = self.wb[sheet]
            self.maxRow = self.ws.max_row
            self.maxCol = self.ws.max_column
            self.reset_ptfill()
            self.anchor_img(sheet)
            self.get_dic_ResLocation()
            if  os.path.isdir(r".\testModel\Stats_%s" % sheet):
                self.wirte_Data(sheet)
                self.write_Version()
                self.write_StatsTag()
            else:
                print "%s Stats Data not found" % sheet

    def Save(self):
        self.wb.save(r".\testModel\Sample_New.xlsx")
        self.wb.close()

    def anchor_img(self, sheetname):
        """
        Re-load image for Pic data
        Load_workbook do not load img data from source xlsx
        """
        img = Image(r".\testModel\Pic\%s.png" % sheetname)
        self.ws.add_image(img, "A1")

    def get_dic_ResLocation(self):
        """
        Find Result Item Loccation in worksheet & storing in a dict
        """
        self.dicResLocation = {}
        # Scan Row=2, Get Cell Column Dict
        for i in xrange(self.maxCol - 2):
            cellvalue = self.ws.cell(row=2, column=i + 3).value
            if cellvalue:
                self.dicResLocation[cellvalue] = (2, i + 3)

    def wirte_Data(self, sheetname):
        """
                Loop1: Get Result Item, Filling, Packing, etc.
                        Loop2: Get Physical Quantity, Pressure, Temperature, etc.
                                Loop3: Write Statistic Data
        """
        # if  not os.path.isdir(r".\Stats_%s" % sheetname):
        #     return 
        lstResTXT = os.listdir(r".\testModel\Stats_%s" % sheetname)
        tupPhysQty = ()
        for ResTXT in lstResTXT:
            with open(r".\testModel\Stats_%s\%s" % (sheetname, ResTXT), "r") as resfile:
                data = resfile.read().split("\n")[:-1]
            # 結果項名稱含'/'字元處理
            if "_" in ResTXT:
                ResTXT = ResTXT.replace("_", "/")
            # 讀取該工作表每個結果項的欄位
            tempCol = self.dicResLocation.get(ResTXT[:-4])[1]
            
            for PhysQtyStats in data:
                # PhysQty = PhysQtyStats.split(" = ")[0]
                # if ResTXT == "Filling.txt":
                #     print PhysQtyStats.split(" = ")[0]
                #     print tempRow, tempCol
                lstQtyStats = PhysQtyStats.split(" = ")[1].split(", ")
                tempRow = self.maxRow
                if "*" in PhysQtyStats.split(" = ")[0]:
                    _cell = self.ws.cell(row=tempRow + 1, column=tempCol)
                    _cell.value = float(lstQtyStats[0])
                    _cell.font = self.ft
                    _cell.alignment = self.al
                    _cell.number_format = "0.000"
                    self.ws.merge_cells(start_row=tempRow + 1, start_column=tempCol, end_row=tempRow + 4, end_column=tempCol)
                    self.check_VerDiff(tempRow + 1, tempCol)
                else:
                    for QtyStats in lstQtyStats:
                        # 從 maxRow 開始填入統計數據 Min, Max, Avg, SD
                        tempRow += 1
                        _cell = self.ws.cell(row=tempRow, column=tempCol)
                        _cell.value = float(QtyStats)
                        _cell.font = self.ft
                        _cell.alignment = self.al
                        # 數字格式
                        bSpecial_PhysQty = "Shear" in PhysQtyStats.split(" = ")[0]
                        bSpecial_PhysQty = bSpecial_PhysQty or "Cell Density" in PhysQtyStats.split(" = ")[0]
                        if (tempRow % 4 == 3) or bSpecial_PhysQty:
                            _cell.number_format = "0.000E+00"
                        else:
                            _cell.number_format = "0.000"
                        self.check_VerDiff(tempRow, tempCol)
                    # 每寫一個物理量之後欄位加1
                tempCol += 1

    def check_VerDiff(self, CURRow, CURCol):
        """
        檢查與前一版本差異是否大於 10 %，若是則充填黃色背景
        """
        CURCell = self.ws.cell(row=CURRow, column=CURCol)
        PRECell = self.ws.cell(row=CURRow - 4, column=CURCol)
        if type(CURCell.value).__name__ == "NoneType":
            print type(CURCell.value).__name__
        if PRECell.value != 0:
            criteria = (CURCell.value - PRECell.value) / PRECell.value
            if abs(criteria) >= 0.2:
                PRECell.fill = self.er
                CURCell.fill = self.er

    def write_Version(self):
        """
        Write Version Name
        """
        # 判斷已寫入版本數量，選擇對應的充填格式
        
        if (self.maxRow - 3) / 4 & 1:
            verbg = self.ver2
        else:
            verbg = self.ver1
        # 以版本名"R16 Beta1"測試
        self.ws["A%s" % str(self.maxRow + 1)].value = self.get_MDXVer()[0]
        self.ws["A%s" % str(self.maxRow + 1)].font = self.ft
        self.ws["A%s" % str(self.maxRow + 1)].alignment = self.al
        self.ws["A%s" % str(self.maxRow + 1)].fill = verbg
        # 跨欄處理版本名儲存格
        self.ws.merge_cells("A%s:A%s" %
                            (str(self.maxRow + 1), str(self.maxRow + 4)))

    def write_StatsTag(self):
        """
        Copy B4:B7 Stats Tag to New Rows
        """
        for i in xrange(4):
            row_n = str(self.maxRow + i + 1)
            row_p = str(i + 4)
            self.ws["B%s" % row_n].value = self.ws["B%s" % row_p].value
            self.ws["B%s" % row_n].font = self.ft
            self.ws["B%s" % row_n].alignment = self.al

    def get_MDXVer(self):
        """
        Get Build Information
        """
        r = os.popen("reg query \"%s\"" %
                     r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\CoreTechSystem\MDX_ParallelComputing").read().split("\n")
        for i in r:
            if "_INSTALLDIR" in i and "R16" in i:
                pathVerFile = i.split("    ")[3]
        # Read the DailyBuild version
        with open(r"%s\Moldex3D.ver" % pathVerFile, "r") as verfile:
            VerData = verfile.read().split("\n")
        MDXver = VerData[1].split(" ")
        return " ".join([MDXver[1][:3], MDXver[1][3:]]), "".join(MDXver[3].strip("()").split("."))

    def reset_ptfill(self):
        """
        Reset Pattern Fill After Release MDX
        """
        unfill = PatternFill()
        for i in range(self.maxRow):
            for j in range(self.maxCol):
                self.ws.cell(row=i + 4, column=j + 3).fill = unfill

if __name__ == '__main__':
    objunify = UnifyStatsData()
    objunify.Unifying()
    objunify.Save()
