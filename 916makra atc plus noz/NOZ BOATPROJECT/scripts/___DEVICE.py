import sys
import socket
import numbers
from ___COMM import Comm
from ___COMM import SimCncException
from enum import Enum

class Axis(Enum):
  X = 0
  Y = 1
  Z = 2
  A = 3
  B = 4
  C = 5

class State(Enum):
  EStop = 0
  Idle = 1
  Homing = 2
  Trajectory = 3
  JOG = 4
  MDI = 5
  MPG = 6

class SpindleState(Enum):
  OFF = 0
  CW_ON = 1
  CCW_ON = 2

class FloodState(Enum):
  OFF = 0
  ON = 1

class MistState(Enum):
  OFF = 0
  ON = 1

class ModuleType(Enum):
  IP = 0
  IO = 1
  MPG = 2
  ENC = 3
  TST = 4
  DRV = 5

class IOPortDir(Enum):
  InputPort = 0
  OutputPort = 1

class DIOPinVal(Enum):
  PinReset = 0
  PinSet = 1

class CoordMode(Enum):
  Machine = 0
  Program = 1

class IOFunctionId(Enum):
  iofnEStop = 0
  iofnHome = 1
  iofnIndex = 2
  iofnLimitP = 3
  iofnLimitN = 4
  iofnDriveFault = 5
  iofnTrajTrig = 6
  iofnProbe = 7
  iofnThcUp = 8
  iofnThcDown = 9
  iofnThcTorchOnDig = 10
  iofnThcTorchOnAnalog = 11
  iofnThcAnalog = 12
  iofnDriveEnable = 13
  iofnDriveReset = 14
  iofnTrajSyncOut = 15
  iofnSpindleCw = 16
  iofnSpindleCcw = 17
  iofnSpindleAO = 18
  iofnFlood = 19
  iofnMist = 20
  iofnHvEnable = 21
  iofnPyFunctionRun = 22
  iofnMPGEncPosition = 23
  iofnMPGEncSpeed = 24
  iofnMPGStatus = 25
  iofnSpindleSpeed = 26
  iofnExtRateOverrideEnable = 27
  iofnExtRateOverrideRegulator = 28
  iofnMPGAxisXSelect = 29
  iofnMPGAxisYSelect = 30
  iofnMPGAxisZSelect = 31
  iofnMPGAxisASelect = 32
  iofnMPGAxisBSelect = 33
  iofnMPGAxisCSelect = 34
  iofnMPGIncrementSelect_x1 = 35
  iofnMPGIncrementSelect_x10 = 36
  iofnMPGIncrementSelect_x100 = 37
  iofnLimitsOverride = 38
  iofnSpindleFault = 39
  iofnPSupplyFault = 40
  iofnMPGInhibit = 41
  iofnLaserAOut = 42

class DSignalVal(Enum):
  signalActive = 0
  signalInactive = 1

class LaserMode(Enum):
  Off = 0
  Image = 1
  Manual = 2
  Cut = 3

class RasterOrientation(Enum):
  Horizontal = 0
  Vertical = 1

class ImgColorMode(Enum):
  Grayscale = 0
  Threshold = 1
  Dithering = 2

class Direction(Enum):
  Negative = 0
  Positive = 1

class ThcState(Enum):
  Off = 0
  On = 1

class JogMode(Enum):
  Continous = 0
  Step = 1


class Device( object ):
  def __init__( self, ip = 'localhost', password = '' ):
    self.port = 48323
    self.password = password
    self.comm = Comm( ip, self.port, self.password )
    self.ip = ip

  def getComm( self ):
    return self.comm

  class Module:
    def __init__( self, type, id, comm ):
      self.comm = comm
      self.type = type
      self.id = id

    def __repr__(self):
      return self.type + str(self.id)

    def getAnalogIO( self, direction, analogPin ):
      return float(self.comm.sendAndWait( "getAnalogIO:" + direction.name + ':' + str(analogPin) + ':' + self.type + ';' + self.id ))

    def getDigitalIO( self, direction, digitalPin ):
      return DIOPinVal[self.comm.sendAndWait( "getDigitalIO:" + direction.name + ':' + str(digitalPin) + ':' + self.type + ';' + self.id )]

    def getEncoderIOAngle( self, channel = 0 ):
      return float(self.comm.sendAndWait( "getEncoderIOAngle:" + str(channel) + ':' + self.type + ';' + self.id ))

    def getEncoderIOPosition( self, channel = 0 ):
      return int(self.comm.sendAndWait( "getEncoderIOPosition:" + str(channel) + ':' + self.type + ';' + self.id ))

    def getEncoderIORPM( self, channel = 0 ):
      return float(self.comm.sendAndWait( "getEncoderIORPM:" + str(channel) + ':' + self.type + ';' + self.id ))

    def setAnalogIO( self, analogPin, value ):
      self.comm.sendAndWait( "setAnalogIO:" + str(analogPin) + ':' + str(value) + ':' + self.type + ';' + self.id )

    def setDigitalIO( self, digitalPin, value ):
      self.comm.sendAndWait( "setDigitalIO:" + str(digitalPin) + ':' + value.name + ':' + self.type + ';' + self.id )

    def getDigitalIOCount( self, direction ):
      return int(self.comm.sendAndWait( "getDigitalIOCount:" + direction.name + ':' + self.type + ';' + self.id ))

    def getAnalogIOCount( self, direction ):
      return int(self.comm.sendAndWait( "getAnalogIOCount:" + direction.name + ':' + self.type + ';' + self.id ))

    def getEncoderIOPositionCount( self ):
      return int(self.comm.sendAndWait( "getEncoderIOPositionCount:" + self.type + ';' + self.id ))

    def getEncoderIOVelocityCount( self ):
      return int(self.comm.sendAndWait( "getEncoderIOVelocityCount:" + self.type + ';' + self.id ))

    def getEncoderIOAngleCount( self ):
      return int(self.comm.sendAndWait( "getEncoderIOAngleCount:" + self.type + ';' + self.id ))

    def getDigitalIOs( self, direction ):
      return [DIOPinVal[ i ] for i in self.comm.sendAndWait( "getDigitalIOs:" + direction.name + ':' + self.type + ';' + self.id ).split(";")]

    def getAnalogIOs( self, direction ):
      return [float(i) for i in self.comm.sendAndWait( "getAnalogIOs:" + direction.name + ':' + self.type + ';' + self.id ).split(";")]

    def getEncoderIOPositions( self ):
      return [int(i) for i in self.comm.sendAndWait( "getEncoderIOPositions:" + self.type + ';' + self.id ).split(";")]

    def getEncoderIOVelocities( self ):
      return [float(i) for i in self.comm.sendAndWait( "getEncoderIOVelocities:" + self.type + ';' + self.id ).split(";")]

    def getEncoderIOAngles( self ):
      return [float(i) for i in self.comm.sendAndWait( "getEncoderIOAngles:" + self.type + ';' + self.id ).split(";")]

  def isGcodeFileLoaded( self ):
    return self.comm.sendAndWait( "isGcodeFileLoaded:" ) == "True"

  def executeGCode( self, data ):
    self.comm.sendAndWait( "executeGCode:" + data )

  def executeGCodeList( self, data ):
    self.comm.sendAndWait( "executeGCodeList:" + (type(data).__name__)+':'+str(len(data))+':'+';'.join(data) )

  def executeProbing( self, coordMode, position, probeIndex, velocity ):
    return self.comm.sendAndWait( "executeProbing:" + coordMode.name + ':' + str(position[0])+';'+str(position[1])+';'+str(position[2])+';'+str(position[3])+';'+str(position[4])+';'+str(position[5]) + ':' + str(probeIndex) + ':' + str(velocity) ) == "True"

  def getCurrentWorkOffset( self ):
    return [float(i) for i in self.comm.sendAndWait( "getCurrentWorkOffset:" ).split(";")]

  def getGCodeFilePath( self ):
    return self.comm.sendAndWait( "getGCodeFilePath:" )

  def getMachineParam( self, data ):
    return float(self.comm.sendAndWait( "getMachineParam:" + str(data) ))

  def getProbingPosition( self, data ):
    return [float(i) for i in self.comm.sendAndWait( "getProbingPosition:" + data.name ).split(";")]

  def getPosition( self, data ):
    return [float(i) for i in self.comm.sendAndWait( "getPosition:" + data.name ).split(";")]

  def getWorkOffset( self, data ):
    return [float(i) for i in self.comm.sendAndWait( "getWorkOffset:" + str(data) ).split(";")]

  def getWorkOffsetNumber( self ):
    return int(self.comm.sendAndWait( "getWorkOffsetNumber:" ))

  def openGCodeFile( self, data ):
    self.comm.sendAndWait( "openGCodeFile:" + data )

  def closeGCodeFile( self ):
    self.comm.sendAndWait( "closeGCodeFile:" )

  def setGCodeNextLine( self ):
    self.comm.sendAndWait( "setGCodeNextLine:" )

  def getGCodeLinesCount( self ):
    return int(self.comm.sendAndWait( "getGCodeLinesCount:" ))

  def getGCodeLine( self, data ):
    return self.comm.sendAndWait( "getGCodeLine:" + str(data) )

  def getGCodeCurrentLine( self ):
    return self.comm.sendAndWait( "getGCodeCurrentLine:" )

  def getGCodeCurrentLineNumber( self ):
    return int(self.comm.sendAndWait( "getGCodeCurrentLineNumber:" ))

  def setGCodeCurrentLineNumber( self, data ):
    self.comm.sendAndWait( "setGCodeCurrentLineNumber:" + str(data) )

  def setAxisProgPosition( self, axis, value ):
    self.comm.sendAndWait( "setAxisProgPosition:" + axis.name + ':' + str(value) )

  def setMachineParam( self, paramNumber, value ):
    self.comm.sendAndWait( "setMachineParam:" + str(paramNumber) + ':' + str(value) )

  def setWorkOffset( self, workOffsetIndex, workOffsetValues ):
    self.comm.sendAndWait( "setWorkOffset:" + str(workOffsetIndex) + ':' + str(workOffsetValues[0])+';'+str(workOffsetValues[1])+';'+str(workOffsetValues[2])+';'+str(workOffsetValues[3])+';'+str(workOffsetValues[4])+';'+str(workOffsetValues[5]) )

  def setCurrentWorkOffset( self, data ):
    self.comm.sendAndWait( "setCurrentWorkOffset:" + str(data[0])+';'+str(data[1])+';'+str(data[2])+';'+str(data[3])+';'+str(data[4])+';'+str(data[5]) )

  def setWorkOffsetNumber( self, data ):
    self.comm.sendAndWait( "setWorkOffsetNumber:" + str(data) )

  def executeHoming( self ):
    self.comm.sendAndWait( "executeHoming:" )

  def executeAxisHoming( self, data ):
    self.comm.sendAndWait( "executeAxisHoming:" + data.name )

  def isAxisReferenced( self, data ):
    return self.comm.sendAndWait( "isAxisReferenced:" + data.name ) == "True"

  def getState( self ):
    return State[self.comm.sendAndWait( "getState:" )]

  def enableMachine( self, data ):
    self.comm.sendAndWait( "enableMachine:" + str(data) )

  def isConnected( self ):
    return self.comm.sendAndWait( "isConnected:" ) == "True"

  def setSoftLimitsState( self, axis, state ):
    self.comm.sendAndWait( "setSoftLimitsState:" + axis.name + ':' + str(state) )

  def getSoftLimitsState( self, data ):
    return self.comm.sendAndWait( "getSoftLimitsState:" + data.name ) == "True"

  def setSoftLimitValue( self, direction, axis, value ):
    self.comm.sendAndWait( "setSoftLimitValue:" + direction.name + ':' + axis.name + ':' + str(value) )

  def getSoftLimitValue( self, direction, axis ):
    return float(self.comm.sendAndWait( "getSoftLimitValue:" + direction.name + ':' + axis.name ))

  def ignoreAllSoftLimits( self, data ):
    self.comm.sendAndWait( "ignoreAllSoftLimits:" + str(data) )

  def areAllSoftLimitsIgnored( self ):
    return self.comm.sendAndWait( "areAllSoftLimitsIgnored:" ) == "True"

  def getProfileName( self ):
    return self.comm.sendAndWait( "getProfileName:" )

  def getModuleList( self ):
    data = self.comm.sendAndWait( "getModuleList:" ).split(";")
    
    result = []
    for i in range( 0, len( data ), 2 ):
      
      m = Device.Module( data[i], data[i + 1], self.comm )
      result.append( m )
    return result

  def getModule( self, type, ID ):
    data = self.comm.sendAndWait( "getModule:" + type.name + ':' + str(ID) ).split(";")
    result = Device.Module( data[0], data[1], self.comm )
    return result

  def getAnalogIOSignalValue( self, signalFunction, index = 0 ):
    return float(self.comm.sendAndWait( "getAnalogIOSignalValue:" + signalFunction.name + ':' + str(index) ))

  def getDigitalIOSignalValue( self, signalFunction, index = 0 ):
    return DSignalVal[self.comm.sendAndWait( "getDigitalIOSignalValue:" + signalFunction.name + ':' + str(index) )]

  def getAngleIOSignalValue( self, signalFunction, index = 0 ):
    return float(self.comm.sendAndWait( "getAngleIOSignalValue:" + signalFunction.name + ':' + str(index) ))

  def getPositionIOSignalValue( self, signalFunction, index = 0 ):
    return int(self.comm.sendAndWait( "getPositionIOSignalValue:" + signalFunction.name + ':' + str(index) ))

  def getVelocityIOSignalValue( self, signalFunction, index = 0 ):
    return float(self.comm.sendAndWait( "getVelocityIOSignalValue:" + signalFunction.name + ':' + str(index) ))

  def runPyAction( self, data ):
    self.comm.sendAndWait( "runPyAction:" + data )

  def getFeedrate( self ):
    return float(self.comm.sendAndWait( "getFeedrate:" ))

  def getFRO( self ):
    return int(self.comm.sendAndWait( "getFRO:" ))

  def getSRO( self ):
    return int(self.comm.sendAndWait( "getSRO:" ))

  def getTrajectoryPause( self ):
    return self.comm.sendAndWait( "getTrajectoryPause:" ) == "True"

  def rewindTrajectory( self ):
    self.comm.sendAndWait( "rewindTrajectory:" )

  def setFeedrate( self, data ):
    self.comm.sendAndWait( "setFeedrate:" + str(data) )

  def setFRO( self, data ):
    self.comm.sendAndWait( "setFRO:" + str(data) )

  def setSRO( self, data ):
    self.comm.sendAndWait( "setSRO:" + str(data) )

  def setTrajectoryPause( self, data ):
    self.comm.sendAndWait( "setTrajectoryPause:" + str(data) )

  def startTrajectory( self ):
    self.comm.sendAndWait( "startTrajectory:" )

  def stopTrajectory( self ):
    self.comm.sendAndWait( "stopTrajectory:" )

  def finishTrajectory( self ):
    self.comm.sendAndWait( "finishTrajectory:" )

  def simpleStopTrajectory( self ):
    self.comm.sendAndWait( "simpleStopTrajectory:" )

  def stopButton( self ):
    self.comm.sendAndWait( "stopButton:" )

  def waitForTrajectoryFinished( self, data = 0 ):
    return self.comm.sendAndWait( "waitForTrajectoryFinished:" + str(data) ) == "True"

  def setTangentialAxisEnable( self, data ):
    self.comm.sendAndWait( "setTangentialAxisEnable:" + str(data) )

  def getTangentialAxisEnable( self ):
    return self.comm.sendAndWait( "getTangentialAxisEnable:" ) == "True"

  def waitForZeroVelocity( self, data = 0 ):
    return self.comm.sendAndWait( "waitForZeroVelocity:" + str(data) ) == "True"

  def getCurrentXYZVelocity( self ):
    return float(self.comm.sendAndWait( "getCurrentXYZVelocity:" ))

  def moveAxisIncremental( self, axis, distance, velocity ):
    self.comm.sendAndWait( "moveAxisIncremental:" + axis.name + ':' + str(distance) + ':' + str(velocity) )

  def moveToPosition( self, coordMode, position, velocity ):
    self.comm.sendAndWait( "moveToPosition:" + coordMode.name + ':' + str(position[0])+';'+str(position[1])+';'+str(position[2])+';'+str(position[3])+';'+str(position[4])+';'+str(position[5]) + ':' + str(velocity) )

  def parallelMoveToPosition( self, coordMode, axis, position, velocity ):
    self.comm.sendAndWait( "parallelMoveToPosition:" + coordMode.name + ':' + axis.name + ':' + str(position) + ':' + str(velocity) )

  def setThcState( self, data ):
    self.comm.sendAndWait( "setThcState:" + data.name )

  def getThcState( self ):
    return ThcState[self.comm.sendAndWait( "getThcState:" )]

  def setLaserMode( self, data ):
    self.comm.sendAndWait( "setLaserMode:" + data.name )

  def getLaserMode( self ):
    return LaserMode[self.comm.sendAndWait( "getLaserMode:" )]

  def setLaserRasterOrientation( self, data ):
    self.comm.sendAndWait( "setLaserRasterOrientation:" + data.name )

  def getLaserRasterOrientation( self ):
    return RasterOrientation[self.comm.sendAndWait( "getLaserRasterOrientation:" )]

  def setLaserImgColorMode( self, data ):
    self.comm.sendAndWait( "setLaserImgColorMode:" + data.name )

  def getLaserImgColorMode( self ):
    return ImgColorMode[self.comm.sendAndWait( "getLaserImgColorMode:" )]

  def setLaserManualOut( self, data ):
    self.comm.sendAndWait( "setLaserManualOut:" + str(data) )

  def getLaserManualOut( self ):
    return float(self.comm.sendAndWait( "getLaserManualOut:" ))

  def setLaserImgBrightness( self, data ):
    self.comm.sendAndWait( "setLaserImgBrightness:" + str(data) )

  def getLaserImgBrightness( self ):
    return int(self.comm.sendAndWait( "getLaserImgBrightness:" ))

  def setLaserImgContrast( self, data ):
    self.comm.sendAndWait( "setLaserImgContrast:" + str(data) )

  def getLaserImgContrast( self ):
    return int(self.comm.sendAndWait( "getLaserImgContrast:" ))

  def setLaserImgBWThreshold( self, data ):
    self.comm.sendAndWait( "setLaserImgBWThreshold:" + str(data) )

  def getLaserImgBWThreshold( self ):
    return int(self.comm.sendAndWait( "getLaserImgBWThreshold:" ))

  def setLaserImgPixelSize( self, data ):
    self.comm.sendAndWait( "setLaserImgPixelSize:" + str(data) )

  def getLaserImgPixelSize( self ):
    return float(self.comm.sendAndWait( "getLaserImgPixelSize:" ))

  def setLaserImgWidth( self, data ):
    self.comm.sendAndWait( "setLaserImgWidth:" + str(data) )

  def getLaserImgWidth( self ):
    return float(self.comm.sendAndWait( "getLaserImgWidth:" ))

  def setLaserImgHeight( self, data ):
    self.comm.sendAndWait( "setLaserImgHeight:" + str(data) )

  def getLaserImgHeight( self ):
    return float(self.comm.sendAndWait( "getLaserImgHeight:" ))

  def setLaserKeepAspectRatio( self, data ):
    self.comm.sendAndWait( "setLaserKeepAspectRatio:" + str(data) )

  def getLaserKeepAspectRatio( self ):
    return self.comm.sendAndWait( "getLaserKeepAspectRatio:" ) == "True"

  def setLaserPowerCurve( self, grayLevel_1, voltage_1, grayLevel_2, voltage_2 ):
    self.comm.sendAndWait( "setLaserPowerCurve:" + str(grayLevel_1) + ':' + str(voltage_1) + ':' + str(grayLevel_2) + ':' + str(voltage_2) )

  def getLaserPowerCurve( self ):
    return [float(i) for i in self.comm.sendAndWait( "getLaserPowerCurve:" ).split(";")]

  def setLaserDefaultPowerCurve( self ):
    self.comm.sendAndWait( "setLaserDefaultPowerCurve:" )

  def setLaserImgDefaultConfig( self ):
    self.comm.sendAndWait( "setLaserImgDefaultConfig:" )

  def openLaserImage( self, data ):
    self.comm.sendAndWait( "openLaserImage:" + data )

  def getFloodState( self ):
    return FloodState[self.comm.sendAndWait( "getFloodState:" )]

  def getMistState( self ):
    return MistState[self.comm.sendAndWait( "getMistState:" )]

  def getSelectedToolNumber( self ):
    return int(self.comm.sendAndWait( "getSelectedToolNumber:" ))

  def getSpindleSpeed( self ):
    return float(self.comm.sendAndWait( "getSpindleSpeed:" ))

  def getSpindleState( self ):
    return SpindleState[self.comm.sendAndWait( "getSpindleState:" )]

  def getSpindleToolNumber( self ):
    return int(self.comm.sendAndWait( "getSpindleToolNumber:" ))

  def getToolDiameter( self, data ):
    return float(self.comm.sendAndWait( "getToolDiameter:" + str(data) ))

  def getToolLength( self, data ):
    return float(self.comm.sendAndWait( "getToolLength:" + str(data) ))

  def getToolOffset( self, data ):
    return [float(i) for i in self.comm.sendAndWait( "getToolOffset:" + str(data) ).split(";")]

  def getToolWearOffset( self, data ):
    return [float(i) for i in self.comm.sendAndWait( "getToolWearOffset:" + str(data) ).split(";")]

  def getToolDiameterWear( self, data ):
    return float(self.comm.sendAndWait( "getToolDiameterWear:" + str(data) ))

  def getToolOffsetNumber( self ):
    return int(self.comm.sendAndWait( "getToolOffsetNumber:" ))

  def setFloodState( self, data ):
    self.comm.sendAndWait( "setFloodState:" + data.name )

  def setMistState( self, data ):
    self.comm.sendAndWait( "setMistState:" + data.name )

  def setSelectedToolNumber( self, data ):
    self.comm.sendAndWait( "setSelectedToolNumber:" + str(data) )

  def setSpindleSpeed( self, data ):
    self.comm.sendAndWait( "setSpindleSpeed:" + str(data) )

  def setSpindleState( self, data ):
    self.comm.sendAndWait( "setSpindleState:" + data.name )

  def setSpindleToolNumber( self, data ):
    self.comm.sendAndWait( "setSpindleToolNumber:" + str(data) )

  def setToolDiameter( self, toolNumber, toolDiameter ):
    self.comm.sendAndWait( "setToolDiameter:" + str(toolNumber) + ':' + str(toolDiameter) )

  def setToolLength( self, toolNumber, toolLength ):
    self.comm.sendAndWait( "setToolLength:" + str(toolNumber) + ':' + str(toolLength) )

  def setToolOffset( self, toolNumber, toolOffset ):
    self.comm.sendAndWait( "setToolOffset:" + str(toolNumber) + ':' + str(toolOffset[0])+';'+str(toolOffset[1])+';'+str(toolOffset[2])+';'+str(toolOffset[3])+';'+str(toolOffset[4])+';'+str(toolOffset[5]) )

  def setToolWearOffset( self, toolNumber, toolOffsetWear ):
    self.comm.sendAndWait( "setToolWearOffset:" + str(toolNumber) + ':' + str(toolOffsetWear[0])+';'+str(toolOffsetWear[1])+';'+str(toolOffsetWear[2])+';'+str(toolOffsetWear[3])+';'+str(toolOffsetWear[4])+';'+str(toolOffsetWear[5]) )

  def setToolDiameterWear( self, toolNumber, toolDiameterWear ):
    self.comm.sendAndWait( "setToolDiameterWear:" + str(toolNumber) + ':' + str(toolDiameterWear) )

  def setToolOffsetNumber( self, data ):
    self.comm.sendAndWait( "setToolOffsetNumber:" + str(data) )

  def waitForSpindleSetSpeed( self, data ):
    self.comm.sendAndWait( "waitForSpindleSetSpeed:" + str(data) )

  def setJogSpeed( self, data ):
    self.comm.sendAndWait( "setJogSpeed:" + str(data) )

  def getJogSpeed( self ):
    return float(self.comm.sendAndWait( "getJogSpeed:" ))

  def setJogMode( self, data ):
    self.comm.sendAndWait( "setJogMode:" + data.name )

  def getJogMode( self ):
    return JogMode[self.comm.sendAndWait( "getJogMode:" )]

  def setJogStep( self, data ):
    self.comm.sendAndWait( "setJogStep:" + str(data) )

  def getJogStep( self ):
    return float(self.comm.sendAndWait( "getJogStep:" ))

  def stopDbgGraph( self ):
    self.comm.sendAndWait( "stopDbgGraph:" )

  def makeExecSegDbgFile( self ):
    self.comm.sendAndWait( "makeExecSegDbgFile:" )

  def makePointsDbgFile( self, data ):
    self.comm.sendAndWait( "makePointsDbgFile:" + data )

  def resetPointsDbgParams( self ):
    self.comm.sendAndWait( "resetPointsDbgParams:" )

  def getScreenName( self ):
    return self.comm.sendAndWait( "getScreenName:" )

  def closeAllMessageBoxes( self ):
    self.comm.sendAndWait( "closeAllMessageBoxes:" )

