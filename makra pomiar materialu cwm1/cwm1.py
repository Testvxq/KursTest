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
ToolSensorHeigh=64.76
# probe index
probeIndex = 0
# probing start position [X, Y, Z]
probeStartAbsPos = [103,100,-1]   #pozycja czujnika wskazana wrzecionem1!
# Axis Z probing end position (absolute)
zEndPosition = -280
# the absolute position of the Z axis of the probe contact for the reference tool
refToolProbePos = 0
# approach velocity (units/min)
vel = 25000
# probing velocity (units/min)
fastProbeVel = 300	
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

# go to XY start probe position
if(moveX == True):
  pos[Axis.X.value] = probeStartAbsPos[Axis.X.value]
if(moveY == True):
  pos[Axis.Y.value] = probeStartAbsPos[Axis.Y.value]
d.moveToPosition(CoordMode.Machine, pos, vel)
# go to Z start probe position

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
# lift-up Z
d.moveAxisIncremental(Axis.Z, goUpDist, vel)
ToolLength=d.getToolLength(d.getSpindleToolNumber( ))

Woffset=d.getCurrentWorkOffset( )
# calculate and set tool length
MaterialOffset = probeFinishPos[Axis.Z.value] - ToolSensorHeigh-ToolLength
Woffset[2]=MaterialOffset
d.setCurrentWorkOffset( Woffset)

# finish
print("pomiar wysokosci materialu zakonczony sukcesem!")
