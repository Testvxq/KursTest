import sys as simCncSys

class LoggerOut:

    class __Logger:
        def __init__(self):
            self.log_destination = []
            self.log_destination.append(simCncSys.stdout)
            self.comm = {}
            self.commRefs = {}

        def add_log_file(self, stream):
            self.log_destination.append(stream)

        def write(self, message):
            for item in self.log_destination:
                item.write(message.encode().decode("ascii", "ignore"))
            for k, v in self.comm.items():
                v.console(message)

        def flush(self):
            for item in self.log_destination:
                item.flush()

        def addComm(self, comm):
            appAddr = comm.getAppAddr()
            if appAddr[0] != '127.0.0.1':
                appAddr = ('localhost', appAddr[1])
            if appAddr[0] != 'localhost':
                return
            if appAddr not in self.comm:
                self.comm[appAddr] = comm
            if appAddr not in self.commRefs:
                self.commRefs[appAddr] = 1
            else:
                self.commRefs[appAddr] = self.commRefs[appAddr] + 1

        def removeComm(self, comm):
            appAddr = comm.getAppAddr()
            if appAddr in self.commRefs:
                if self.commRefs[appAddr] > 1:
                    self.commRefs[appAddr] = self.commRefs[appAddr] - 1
                else:
                    self.commRefs.pop(appAddr, None)
                    self.comm.pop(appAddr, None)

    instance = None

    def __init__(self):
        if not LoggerOut.instance:
            LoggerOut.instance = LoggerOut.__Logger()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def addComm(self, comm):
        LoggerOut.instance.addComm(comm)

    def removeComm(self, comm):
        LoggerOut.instance.removeComm(comm)


class LoggerErr:

    class __Logger:
        def __init__(self):
            self.log_destination = []
            self.log_destination.append(simCncSys.stderr)
            self.comm = {}
            self.commRefs = {}

        def add_log_file(self, stream):
            self.log_destination.append(stream)

        def write(self, message):
            for item in self.log_destination:
                item.write(message)
            for k, v in self.comm.items():
                v.console(message)

        def flush(self):
            for item in self.log_destination:
                item.flush()

        def addComm(self, comm):
            appAddr = comm.getAppAddr()
            if appAddr not in self.comm:
                self.comm[appAddr] = comm
            if appAddr not in self.commRefs:
                self.commRefs[appAddr] = 1
            else:
                self.commRefs[appAddr] = self.commRefs[appAddr] + 1

        def removeComm(self, comm):
            appAddr = comm.getAppAddr()
            if appAddr in self.commRefs:
                if self.commRefs[appAddr] > 1:
                    self.commRefs[appAddr] = self.commRefs[appAddr] - 1
                else:
                    self.commRefs.pop(appAddr, None)
                    self.comm.pop(appAddr, None)

    instance = None

    def __init__(self):
        if not LoggerErr.instance:
            LoggerErr.instance = LoggerErr.__Logger()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def addComm(self, comm):
        LoggerErr.instance.addComm(comm)

    def removeComm(self, comm):
        LoggerErr.instance.removeComm(comm)

