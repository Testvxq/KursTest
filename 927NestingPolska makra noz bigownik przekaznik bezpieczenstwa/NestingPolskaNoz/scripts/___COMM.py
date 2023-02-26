import sys as simCncSys
import socket as simCncSocket
import binascii as simCncBinascii
from ___DEBUGGER import Debugger as simCncDebugger
from ___LOGGER import LoggerOut as simCncLoggerOut
from ___LOGGER import LoggerErr as simCncLoggerErr
from ___ARGV import Argv as simCncArgv
import base64

class SimCncException(Exception):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)

class Comm:

	_comm_instances = 0

	def __init__(self, simCncIp, simCncPort, simCncPassword):
		Comm._comm_instances += 1
		self.instance_number = Comm._comm_instances
		argv = simCncArgv()
		self.isRunFromSimCnc = argv.isRunFromSimCnc()
		if self.isRunFromSimCnc:
			#normalnie uruchomiony skrypt z simCNC
			self.debugger = simCncDebugger("COMM")
			self.debugger.dbg("START")
			self.appNr = argv.getAppNr()
			self.startActSrc = argv.getStartActSource()
		else:
			self.appNr = 0
			self.startActSrc = "externalProgram 0"
		self.password = simCncPassword
		self.appAddr = ( simCncIp, simCncPort )
		self.socket = simCncSocket.socket(simCncSocket.AF_INET, simCncSocket.SOCK_STREAM)
		self.socket.connect((self.appAddr))
		self.clearData()
		self.sendConnectionRequest()
		self.logOut = simCncLoggerOut()
		self.logOut.addComm(self)
		self.logErr = simCncLoggerErr()
		self.logErr.addComm(self)
		simCncSys.stdout = self.logOut
		simCncSys.stderr = self.logErr

	def __del__(self):
		Comm._comm_instances += 1
		self.logOut.removeComm(self)
		self.logErr.removeComm(self)
		if self.isRunFromSimCnc:
			self.debugger.off() 
		self.sendScriptFinished()

	def sendScriptFinished(self):
		self.send("scriptFinished")

	def clearData(self):
		self.len = 0
		self.lenStr = ""
		self.lenReady = False
		self.crc = 0
		self.crcStr = ""
		self.crcReady = False
		self.datagram = ""

	def calcCRC32(self,txt):
		return "%08X" % (simCncBinascii.crc32(txt) & 0xFFFFFFFF)

	def addLen(self,txt):
		return str(len(txt)) + ":" + txt

	def addCRC(self,txt):
		return self.calcCRC32(txt.encode('utf-8')) + txt

	def prepareMsg(self,msg):
		return self.addCRC( self.addLen( msg ) )
		
	def send(self,msg):
		msgToSend = self.prepareMsg(msg)
		if self.isRunFromSimCnc:
			self.debugger.dbg("send: " + msgToSend)
		self.socket.sendall(msgToSend.encode('utf-8'))
		
	def sendConnectionRequest( self ):
		request = "connectionRequest:" + str(self.instance_number) + ":" + str(self.appNr) + ":" + str(self.startActSrc) + ":" + base64.b64encode(self.password.encode()).decode('utf-8')
		self.send(request)

	def console(self,txt):
		self.send("console:" + txt)

	def checkCRC(self,txt):
		return simCncBinascii.crc32((str(len(txt.decode('utf-8'))) + ":" + txt.decode("utf-8")).encode()) == ( self.crc & 0xffffffff )

	def fillData(self,msg):
		
		if not self.crcReady:
			crcRemain = 8 - len(self.crcStr)
			self.crcStr = self.crcStr + msg[:crcRemain]
			msg = msg[crcRemain:]
			if len(self.crcStr) == 8:
				self.crcReady = True
				try:
					self.crc = int(self.crcStr, 16)
				except:
					simCncSys.exit( "Incorrect datagram (crc is not int)" )
			else:
				return False

		if len(msg) == 0:
			return False

		ready = False

		if not self.lenReady:
			colonPos = msg.find(":")
			if colonPos < 0:
				self.lenStr = self.lenStr + msg
				msg = ""
			else:
				self.lenStr = self.lenStr + msg[:colonPos]
				msg = msg[colonPos+1:]
				self.lenReady = True

			try:
				length = int(self.lenStr)
			except:
				simCncSys.exit( "Incorrect datagram (len is not int)" )

			if not self.lenReady:
				return False

			self.len = length

			if len(msg) == 0:
				return False

		if self.lenReady:

			datagramRemain = self.len - len(self.datagram)
			self.datagram = self.datagram + msg[:datagramRemain]
			msg = msg[datagramRemain:]

			if len(self.datagram) == self.len:
				ready = True

		return ready

	def getReceivedData(self):
		while True:
			msg, addr = self.socket.recvfrom(1024)
			msg = msg.decode("utf-8") 
			if self.isRunFromSimCnc:
				self.debugger.dbg("received part: " + msg)
			if self.fillData(msg) :
				break

	def sendAndWait(self,msg):
		self.send(msg)
		self.clearData()
		self.getReceivedData()
		if self.isRunFromSimCnc:
			self.debugger.dbg("received message: " + self.datagram)
		data = self.datagram.encode()
		if self.checkCRC( data ) == False:
			simCncSys.exit( "CRC error 1" )
		res = data.decode('UTF-8').split(":")
		if len(res) >= 2 and res[0] == "commandExecuted" and res[1] == "ok":
			return ":".join(res[2:])
		else:
			raise SimCncException(":".join(res[1:]))

	def getAppAddr(self):
		return self.appAddr

def createComm():
	return Comm( 'localhost', 48323, '' )