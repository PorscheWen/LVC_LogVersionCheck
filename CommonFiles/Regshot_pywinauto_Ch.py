# -*- coding: utf-8 -*-


import pywinauto
import os

class Moldex3DProjectTesting:
    def __init__(self):
        self.App = pywinauto.application.Application()
        
    def LaunchMoldex3DProject(self):
        self.App.Start_(r"C:\Moldex3D\R14.0\Bin\MDXProject.exe")
                
    def OpenAboutMoldex3D(self):
        Dlg_Moldex3DProject = self.App.window_(title_re = ".*Moldex3D  x64.*")
        Dlg_Moldex3DProject.MenuItem(u'&Help->&About Moldex3D...').Click()
            
    def VerifyAboutMoldex3D(self):
        try:
            Dlg_AboutMoldex3D = self.App.AboutMoldex3D
            Properties = Dlg_AboutMoldex3D.GetProperties()
            if (Properties['IsVisible'] == True):
                print "AboutMoldex3D is visible..."
            else:
                print "AboutMoldex3D is not visible..."
        except Exception as E:
            print "AboutMoldex3D does not exist..."
    
    def ExitAboutMoldex3D(self):
        Dlg_AboutMoldex3D = self.App.AboutMoldex3D
        Dlg_AboutMoldex3D.OK.Click()
        
    def ExitMoldex3DProject(self):
        Dlg_Moldex3DProject = self.App.window_(title_re = ".*Moldex3D  x64.*")
        Dlg_Moldex3DProject.MenuItem(u'&File->E&xit').Click()
        
        Dlg_Confirm = self.App.Confirm
        Dlg_Confirm.Yes.Click()
                        
    def Main(self):
        #Step1:Launch Moldex3D Project...
        self.LaunchMoldex3DProject()
        #Step2:Open About Moldex3D...(with wait function)
        pywinauto.timings.WaitUntilPasses(timeout=60, retry_interval=1, func=self.OpenAboutMoldex3D)
        #Step3:Verify About Moldex3D exist or not...
        self.VerifyAboutMoldex3D()
        #Step4:Click OK Button to Exit...
        self.ExitAboutMoldex3D()
        #Step5:Exit Moldex3D Project...
        self.ExitMoldex3DProject()
        

class Regshot(object):
    
    def __init__(self):
        self.App = pywinauto.application.Application()

    def LaunchRegShot(self):
        self.App.Start(r"C:\work\XenTools\VM_Require_Tools\RegshotPortable\Regshot.exe")

    def InitHive(self):
        Dlg_Regshot = self.App.window_(title_re = "Regshot")
        Dlg_Regshot.MenuItem(u'&1st shot->Whole registry').Click()
        Dlg_Regshot.MenuItem(u'&1st shot->Save...').Click()
        Dlg_SaveAs = self.App.Dialog
        Dlg_SaveAs.edit.SetText("C:\\initial_shot.hive")
        Dlg_SaveAs["存檔".decode("utf-8")].Click()

    def LoadInitHive(self):
        Dlg_Regshot = self.App.window_(title_re = "Regshot")
        Dlg_Regshot.MenuItem(u'&1st shot->Open...').Click()
        Dlg_Open = self.App.Dialog
        Dlg_Open.edit.SetText("C:\\initial_shot.hive")
        Dlg_Open["開啟舊檔".decode("utf-8")].Click()

    def Get2ndShot(self):
        TestName = "Test_pywinauto"
        Dlg_Regshot = self.App.Window_(title_re = "Regshot")
        Dlg_Regshot.Edit.Click()
        Dlg_Regshot.Edit.SetText(r"C:\Work\LOG\{}".format(TestName))
        Dlg_Regshot.Edit2.Click()
        Dlg_Regshot.Edit2.SetText(TestName)
        Dlg_Regshot.MenuItem(u'2nd shot->Whole registry').Click()

    def undoRegistry(self):
        TestName = "Test_pywinauto"
        RegPath = r"C:\Work\LOG\{0}\{0}.1.Undo.reg".format(TestName)
        os.system("reg import \"{}\"".format(RegPath))

    def ExitRegshot(self):
        Dlg_Regshot = self.App.window_(title_re = "Regshot")
        Dlg_Regshot.MenuItem(u'&File->&Quit').Click()

    def Main(self):
        os.system("del /q C:\\initial_shot.hive")
        self.LaunchRegShot()
        self.InitHive()
        self.ExitRegshot()
        self.LaunchRegShot()
        self.LoadInitHive()
        self.Get2ndShot()
        

if __name__ == "__main__":
    AutoRegshot = Regshot()
    AutoRegshot.Main()
    