#############################################
# POLSKA GRUPA CNC
#4 wrzeciona -Timoleon
#############################################

import sys
import time

#############################################


#############################################
# CONFIG BLOCK

#outputs

OutSpindle2="2"				#wyjscie wrzeciona 2
OutFwd="1"							#wyjscie forward przepisac z konfiguracji wrzeciona (sprawdzenie czy nie jest w stanie aktywnym przed wymiana narzedzia)
#tool change config
SafeZ=-1									#wysokosc podjazdu do wymiany
#END CONFIG BLOCK
#############################################

#############################################
#FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!
mod_IP = d.getModule( ModuleType.IP, 0 )

def IsFwdActive():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutFwd) == DIOPinVal.PinReset :
		IsFwdActive=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutFwd) == DIOPinVal.PinSet :
		IsFwdActive=1
	return IsFwdActive

def Spindle2Down():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinSet)                             
def Spindle2Up():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinReset)  

#END FUNKCJON  DEFINITION
#############################################

#############################################
#VARIABLES  DECLARATION -DO NOT CHANGE ANYTHING!!!
ActToolPos=1
NewToolPos=1
pos=d.getPosition(CoordMode.Machine)
ActTool=d.getSpindleToolNumber()
NewTool=d.getSelectedToolNumber()
e=0
#END WARIABLES  DECLARATION
#############################################
#############################################
#Macro main

if(ActTool==NewTool):
	print("narzedzie aktualnie zaladowane")
	e=1 
if(e<1):
	e=0
	pos[2]=SafeZ
	d.setSpindleState(SpindleState.OFF)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f} F3000 ".format(pos[0],pos[1],pos[2]))
	if  (NewTool==1):
		e=1
		Spindle2Up()
		time.sleep(2)
	if  (NewTool==2):
		e=1
		Spindle2Down()
		time.sleep(2)
	if(e<1):
			msg.wrn("Nie ma tekiego narzedzia!")
			sys.exit("nie ma takiego, B31d wymiany narzedzia!")
d.setSpindleToolNumber(NewTool)
d.setToolOffsetNumber(NewTool)

#END Macro main
#############################################

