
import sys as simCncSys
import os as simCncOs
from ___DEBUGGER import Debugger as simCncDebugger
from ___ARGV import Argv as simCncArgv
from ___DEVICE import *
from ___MSG import Msg

d=Device()
msg=Msg()

def exit(exitCode):
    d.getComm().sendScriptFinished()
    sys.exit(exitCode)

#moze nie byc modulu ___GUI (np. w trakcie uruchamiania test.py), poniewaz w python/defaultScripts nie ma ___GUI.py
#___GUI.py jest generowany przez ___GUIUPD.py na podstawie gui.json z profilu uzytkownika
try :
    from ___GUI import Gui
    gui=Gui( d.getComm() )
except :
    pass

try :
    from autotester.___AUTOTESTER import Autotester
    t = Autotester(d, gui)
except :
    pass

fileName = simCncArgv().getFilePath()

if simCncOs.path.basename(fileName) == '___GUIUPD.py' :
    from ___GUIUPD import generateGui
    generateGui( d.getComm() )
else :
    dir = simCncOs.path.dirname(fileName)
    simCncOs.chdir(dir)
    simCncSys.path.insert(0, dir)    
    exec(open(fileName, encoding='utf-8').read())
        