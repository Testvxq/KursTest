#############################################
# CS-Lab s.c.
#
# simCNC sample automatic tool lenght probing macro
#############################################
import sys
import time

#############################################
# BEGIN WARNING BLOCK
# comment this block when you set/check settings below
#############################################
#msg.wrn("Setup probing macro configuration first.\n\nMenu 'Macro->Show Script Editor' and choose 'probing'", "Warning!")
#sys.exit("Error! Probing macro not configured!")
#############################################
# END WARNING BLOCK
#############################################


#############################################
###### BEGIN SETTINGS
#############################################
# probe index
probeIndex = 0
# probing start position [X, Y, Z]
probeStartAbsPos = [418.339,3297,-20]   #pozycja czujnika wskazana wrzecionem!
Spindle2Offset=[-174.800,21.300]									#ofset noza [X,Y]
Spindle3Offset=[-279.800,21.300]									#ofset bigownika [X,Y]


# Axis Z probing end position (absolute)
zEndPosition = -211
# the absolute position of the Z axis of the probe contact for the reference tool
refToolProbePos = 0
# approach velocity (units/min)
vel = 15000
# probing velocity (units/min)
fastProbeVel = 600	
slowProbeVel = 150
# lift up dist before fine probing
goUpDist = 5
# delay (seconds) before fine probing
fineProbingDelay = 0.2
# other options
moveX = True
moveY = True
checkFineProbingDiff = False
fineProbeMaxAllowedDiff = 0.1
CutterOffset=-16.8
#############################################
###### END SETTINGS
#############################################



#############################################
# Macro START
#############################################
d.setSpindleState(SpindleState.OFF)
toolNr = d.getSpindleToolNumber()
if(toolNr == 0):
  sys.exit("Tool(0) has no tool lenght offset. Probing failed!")
# get current absolute position
pos = d.getPosition(CoordMode.Machine)
# lift up Z to absolute 0
pos[Axis.Z.value] = -1;
d.moveToPosition(CoordMode.Machine, pos, vel)

if(toolNr==2):
	probeStartAbsPos[0]=probeStartAbsPos[0]+Spindle2Offset[0]
	probeStartAbsPos[1]=probeStartAbsPos[1]+Spindle2Offset[1]
if(toolNr==3):
	probeStartAbsPos[0]=probeStartAbsPos[0]+Spindle3Offset[0]
	probeStartAbsPos[1]=probeStartAbsPos[1]+Spindle3Offset[1]



# go to XY start probe position
d.setTangentialAxisEnable(False)
if(moveX == True):
  pos[Axis.X.value] = probeStartAbsPos[Axis.X.value]
if(moveY == True):
  d.setSoftLimitsState( Axis.Y, False)
  pos[Axis.Y.value] = probeStartAbsPos[Axis.Y.value]
d.moveToPosition(CoordMode.Machine, pos, vel)
# go to Z start probe position
pos[Axis.Z.value] = probeStartAbsPos[Axis.Z.value]
d.moveToPosition(CoordMode.Machine, pos, vel)

# start fast probing
pos[Axis.Z.value] = zEndPosition;
probeResult = d.executeProbing(CoordMode.Machine, pos, probeIndex, fastProbeVel)
if(probeResult == False):
  sys.exit("fast probing failed!")
# get fast probe contact position
fastProbeFinishPos = d.getProbingPosition(CoordMode.Machine)

# lift-up Z
d.moveAxisIncremental(Axis.Z, goUpDist, vel)
# delay
time.sleep(fineProbingDelay)
# start fine probing
probeResult = d.executeProbing(CoordMode.Machine, pos, probeIndex, slowProbeVel)
if(probeResult == False):
  sys.exit("slow probing failed!")
# get fine probe contact position
probeFinishPos = d.getProbingPosition(CoordMode.Machine)

# check diff between fast and fine probing
probeDiff = abs(fastProbeFinishPos[Axis.Z.value] - probeFinishPos[Axis.Z.value])
if(probeDiff > fineProbeMaxAllowedDiff and checkFineProbingDiff == True):
  errMsg = "ERROR: fine probing difference limit exceeded! (diff: {:.3f})".format(probeDiff)
  sys.exit( errMsg)

# calculate and set tool length
if(toolNr == 2):
	toolOffset = probeFinishPos[Axis.Z.value] - refToolProbePos-CutterOffset
	d.setToolLength(toolNr, toolOffset)
else:
	toolOffset = probeFinishPos[Axis.Z.value] - refToolProbePos
	d.setToolLength(toolNr, toolOffset)
# lift Z to abs 0
pos[Axis.Z.value] = 0
d.moveToPosition(CoordMode.Machine, pos, vel)

if(moveY == True):
	pos[Axis.Y.value] = probeStartAbsPos[Axis.Y.value]-400
	d.moveToPosition(CoordMode.Machine, pos, vel)
	d.setSoftLimitsState( Axis.Y, True)
# finish
print("Tool({:d}) offset set to: {:.4f}".format(toolNr, toolOffset))
