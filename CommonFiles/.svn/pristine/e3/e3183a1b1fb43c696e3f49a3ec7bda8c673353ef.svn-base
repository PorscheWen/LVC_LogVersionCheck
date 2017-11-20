import _winreg, re

def AutoReadMoldexVersion():
    # Read the Moldex3D installing address
    pyHKEY = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\CoreTechSystem\MDX_ParallelComputing')
    valueInfo = _winreg.QueryInfoKey(pyHKEY) # Read the value infomation(name & data) under the subKey
    
    versionPathList = []
    for i in range(0, valueInfo[1], 1):
        value = _winreg.EnumValue(pyHKEY, i)
        if "_INSTALLDIR" in value[0]:
            versionPathList.append(value[1])
    
    _winreg.CloseKey(pyHKEY)
    
    if versionPathList == []:
        return("MDX setting address Error !!")
    else:
        versionParentPath = str(versionPathList[-1])
    
    # Read the DailyBuild version
    with open(r"{}\Moldex3D.ver".format(versionParentPath), "r") as localfile :
        versionLine = localfile.read()
    patten = r"R[0-9]{2}[\w\s]+ 64-bit \(Build[0-9]{4}[.][0-9]{4}" # \w = [a-zA-Z0-9_]; \s = ""
    version = re.search(patten, versionLine).group().replace("64-bit (", "").replace(" ", "")
    return(version)

if __name__ == '__main__':
    
    mdxVersion = AutoReadMoldexVersion()
    print(mdxVersion)