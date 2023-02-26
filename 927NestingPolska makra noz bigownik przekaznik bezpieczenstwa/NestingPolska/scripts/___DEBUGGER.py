import logging as simCncLogging
import time as simCncTime
import os as simCncOs
from ___ARGV import Argv as simCncArgv

class Debugger:

    def getTimestamp(self):
        return int(simCncTime.time())

    def addTimeStamp(self, txt):
        return str(self.getTimestamp()) + ": " + txt

    def getDebugId(self):
        return self.debugId

    def getScriptName(self):
        return self.scriptName

    def getValuesFromArgv(self):
        argv = simCncArgv()
        self.debugId = argv.getDebugId()
        self.scriptName = simCncOs.path.basename(argv.getFilePath())

    def getModifiedScriptName(self):
        return self.getScriptName().replace(".", "_").replace(" ", "_")

    def getNotDebuggedSripts(self):
        return ["test.py", "___GUIUPD.py"]

    def isDebuggedScript(self):
        return self.getScriptName() not in self.getNotDebuggedSripts()

    def createFileName(self, name):
        return str(self.getTimestamp()) + "_" + self.getModifiedScriptName() + "_" + name + "_" + str(self.getDebugId()) + ".log"

    def getDebugDirName(self):
        return "dbg/scripts"

    def getDebugDirPath(self):
        return "./" + self.getDebugDirName()

    def getDebugFilePrefix(self):
        return "_script_log_"

    def getFilePath(self, name):
        return self.getDebugDirPath() + "/" + self.getDebugFilePrefix() + self.createFileName(name)

    def configLogger(self, name):
        simCncLogging.basicConfig(filename= self.getFilePath(name), level=simCncLogging.DEBUG)

    def configDebugOn(self):
        self.debugOn = self.getDebugId() > 0

    def isDebugOn(self):
        return self.debugOn and self.isDebuggedScript()

    def createDbgDirIfNotExists(self):
        dirPath = self.getDebugDirPath()
        if not simCncOs.path.exists(dirPath):
            simCncOs.makedirs(dirPath)        

    def config(self, name):
        self.configDebugOn()
        if self.isDebugOn():
            self.createDbgDirIfNotExists()
            self.configLogger(name)
        
    def __init__(self, name):
        self.getValuesFromArgv()
        self.config(name)

    def dbg(self, txt):
        if self.isDebugOn():
            simCncLogging.debug( self.addTimeStamp(txt) )       

    def off(self):
        self.debugOn = False