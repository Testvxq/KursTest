import sys as simCncSys

class Argv:

    def getArg(self, index):
        return simCncSys.argv[index]

    def getFilePath(self):
        return self.getArg(1)

    def getAppNr(self):
        return int(self.getArg(2))

    def getStartActSource(self):
        return self.getArg(3)

    def getSecretCode(self):
        return self.getArg(4)

    def getDebugId(self):
        return int(self.getArg(5))

    def getSimCncArgvLen(self):
        return 6

    def isSimCncArgvLen(self):
        return len(simCncSys.argv) == self.getSimCncArgvLen()

    def getSimCncSecretCode(self):
        return "Super secret code"

    def argumentsContainSecretCode(self):
        return self.getSecretCode() == self.getSimCncSecretCode()

    def isRunFromSimCnc(self):
        return self.isSimCncArgvLen() and self.argumentsContainSecretCode()
