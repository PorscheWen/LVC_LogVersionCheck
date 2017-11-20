# -*- coding: utf-8 -*-

import os
import subprocess
import argparse
import time
import sys

import pywinauto
sys.dont_write_bytecode = True


def check_os_locale():
    cmd = "systeminfo |findstr System"
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = res.communicate()
    if str("en-us") in out:
        return True
    return False


class Regshot(object):

    def __init__(self, isEN=True):
        self.isEN = isEN
        if isEN:
            self.strSave = u"&Save"
            self.strOpen = u"&Open"
        else:
            self.strOpen = "開啟舊檔".decode("utf-8")
            self.strSave = "存檔".decode("utf-8")
        self.App = pywinauto.application.Application()

    def LaunchRegShot(self):
        self.App.Start(r"C:\work\XenTools\VM_Require_Tools\RegshotPortable\Regshot.exe")

    def ExitRegshot(self):
        Dlg_Regshot = self.App.window_(title_re="Regshot")
        Dlg_Regshot.MenuItem(u'&File->&Quit').Click()
        print "Exit Regshot"

    def InitHive(self):
        Dlg_Regshot = self.App.window_(title_re="Regshot")
        Dlg_Regshot.MenuItem(u'&1st shot->Whole registry').Click()
        Dlg_Regshot.MenuItem(u'&1st shot->Save...').Click()
        Dlg_SaveAs = self.App.Dialog
        Dlg_SaveAs.edit.SetText("C:\\initial_shot.hive")
        Dlg_SaveAs[self.strSave].Click()

    def LoadInitHive(self):
        Dlg_Regshot = self.App.window_(title_re="Regshot")
        Dlg_Regshot.MenuItem(u'&1st shot->Open...').Click()
        Dlg_Open = self.App.Dialog
        Dlg_Open.edit.SetText("C:\\initial_shot.hive")
        Dlg_Open[self.strOpen].Click()

    def Get2ndShot(self):
        Dlg_Regshot = self.App.Window_(title_re="Regshot")
        Dlg_Regshot.Edit.Click()
        Dlg_Regshot.Edit.SetText(r"C:\Work\LOG\{}".format(self.TestName))
        Dlg_Regshot.Edit2.Click()
        Dlg_Regshot.Edit2.SetText(self.TestName)
        Dlg_Regshot.MenuItem(u'2nd shot->Whole registry').Click()

    def main_initial(self):
        os.system("del /q C:\\initial_shot.hive")
        self.LaunchRegShot()
        # pywinauto.timings.WaitUntilPasses(timeout=60, retry_interval=1, func=self.OpenAbout)
        self.InitHive()
        self.ExitRegshot()

    def main_restore(self, TestName):
        self.TestName = TestName
        self.LaunchRegShot()
        self.LoadInitHive()
        self.Get2ndShot()
        self.KillIE()
        # self.ExitRegshot()
        self.UndoRegistry()

    def KillIE(self):
        while "iexplore.exe" not in os.popen("tasklist").read():
            time.sleep(0.2)
        os.system("taskkill /t /f /im iexplore.exe")
        os.system("taskkill /t /f /im Regshot.exe" )

    def UndoRegistry(self):
        RegPath = r"C:\Work\LOG\{0}\{0}.1.Undo.reg".format(self.TestName)
        os.system("reg import \"{}\"".format(RegPath))


def main():
    descrpt = """
    This program is for Auto Test, execute me you can get registry snapshot
    for your auto test.
    E.X. :
    Regshot.py -tn TestName # take a snapshot and save file in c:\\work\\<TestName>  .

    """

    parser = argparse.ArgumentParser(description=descrpt)
    parser.add_argument("-i", "--initial", action='store_true',
                        help="Take a initial snapshot & save files in C:\\Users\\Administrator\\Documents\\")
    parser.add_argument("-tn", "--TestName", help="Take a snapshot & save files in c:\\work\\<TestName>")
    args = parser.parse_args()

    if check_os_locale():
        AutoRegshot = Regshot()
    else:
        AutoRegshot = Regshot(isEN=False)

    if args.initial:
        AutoRegshot.main_initial()

    if args.TestName:
        AutoRegshot.main_restore(args.TestName)

    # AutoRegshot.main_initial()
    # AutoRegshot.main_restore("test")

    print "RegShot done"


if __name__ == "__main__":
    main()
