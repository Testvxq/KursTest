import os as simCncOs
import platform as simCncPlatform
from tkinter import messagebox as simCncMessageBox
from tkinter import Tk as simCncTk

class Msg(object):

  def info( self, txt, head="Info"):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    simCncMessageBox.showinfo(head,txt)
    root.destroy()

  def wrn( self, txt, head = "Warning" ):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    simCncMessageBox.showwarning(head,txt)
    root.destroy()

  def err( self, txt, head = "Error" ):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    simCncMessageBox.showerror(head,txt)
    root.destroy()

  def askYesNo( self, txt, head = "ask" ):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    res = simCncMessageBox.askyesno(head,txt)
    root.destroy()
    return res

  def askOkCancel( self, txt, head = "ask" ):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    res = simCncMessageBox.askokcancel(head,txt)
    root.destroy()
    return res

  def askRetryCancel( self, txt, head = "ask" ):
    root = simCncTk()
    root.withdraw()
    if(simCncPlatform.system().lower() == 'darwin'):
      simCncOs.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    res = simCncMessageBox.askretrycancel(head,txt)
    root.destroy()
    return res
