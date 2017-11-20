sec = 1000

def Stage_000_IniteDN():    
    app = TestedApps.MDXDesigner
    app.Params.SimpleParams.CommandLineParameters = ""
    app.Run()
    WaitObjectVisible(Aliases.MDXDesigner.ChooseMode.MeshingMethod)
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.ClickButton()
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_eDesign.Keys(" ")
    Aliases.MDXDesigner.ChooseMode.btn_OK.ClickButton()
    Aliases.MDXDesigner.wndAfx2.close()
    
def Stage_000_InitBLM():
    app = TestedApps.MDXDesigner
    app.Params.SimpleParams.CommandLineParameters = ""    
    app.Run()
    WaitObjectVisible(Aliases.MDXDesigner.ChooseMode.MeshingMethod)  
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_BLM.ClickButton()
    Aliases.MDXDesigner.ChooseMode.MeshingMethod.btn_BLM.Keys(" ")
    Aliases.MDXDesigner.ChooseMode.btn_OK.ClickButton()
    Aliases.MDXDesigner.wndAfx2.close()

def Stage_000_InitProj():
    app = TestedApps.MDXProject
    app.Params.SimpleParams.CommandLineParameters = ""
    app.Run(1, True)
    WaitObjectVisible(Aliases.MDXProject.wndAfx)
    app.Terminate()

def Stage_000_InitRhino():
    app = TestedApps.Rhino
    app.Params.SimpleParams.CommandLineParameters = ""
    app.Run()
    WaitObjectVisible(Aliases.Rhino.wndAfx)
    Aliases.Rhino.wndAfx.Maximize()
    Aliases.Rhino.wndAfx.close()
    
def WaitObjectVisible(Obj):
    wr = Obj.WaitProperty("Exists",True,1*sec)
    if wr != True:
        wr = Obj.WaitProperty("Exists",True, 120*sec)
        if wr == False:
            Log.Error("Wait Object Exists Time Out")
    wr = Obj.WaitProperty("Visible",True,1*sec)
    if wr != True:
        wr = Obj.WaitProperty("Visible",True, 120*sec)
        if wr == False:
            Log.Error("Wait Object Exists Time Out")        
    Log.Message("Object appear")
