#############################################
# POLSKA GRUPA CNC 2709
#AUTO Tool Change 3 spindles v1.00
#############################################

import sys
import time

################      WARNING BLOCK    #############################
# WARNING BLOCK
# comment this block when you set settings below
#msg.wrn("Setup m6 macro first!\n\nMenu 'Macro->Show Script Editor and choose 'm6'", "Warning!")
#sys.exit("Error! Probing macro not configured!")
# END WARNING BLOCK
#################    END WARNING BLOCK     #########################


#################     CONFIG BLOCK    #############################
InSpindle1Up=7					#Wejscie wrzeciona 1
InSpindle2Up=11					#Wejscie wrzeciona 2
InSpindle3Up=9					#Wejscie wrzeciona 3

OutSpindle1=1					#Wyjscie Wrzeciona 1
OutSpindle2=3					#Wyjscie Wrzeciona 2
OutSpindle3=4					#Wyjscie Wrzeciona 3


DelayTime=2						#czas pomiedzy wysterowaniem wyjsc zmiany a odpytaniem krancowek polozenia wrzecion
ZSafeUpPos=-1					#podjazd do wyskokosci zmiany wrzeciona
###########DelayTime#######   END CONFIG BLOCK    ##########################


#######   FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!    ###############
e=0
mod_IP = d.getModule( ModuleType.IP, 0 )
def IsSpindleOn():
	if ((d.getSpindleState( ))==SpindleState.OFF):
		IsSpindleOn=0
	if ((d.getSpindleState( ))==SpindleState.CW_ON):
		IsSpindleOn=1
	return IsSpindleOn
def IsSpindle1Up():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle1Up) == DIOPinVal.PinReset :
		IsSpindle1Up=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle1Up) == DIOPinVal.PinSet :
		IsSpindle1Up=1
	return IsSpindle1Up
def IsSpindle2Up():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle2Up) == DIOPinVal.PinReset :
		IsSpindle2Up=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle2Up) == DIOPinVal.PinSet :
		IsSpindle2Up=1
	return IsSpindle2Up
def IsSpindle3Up():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle3Up) == DIOPinVal.PinReset :
		IsSpindle3Up=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindle3Up) == DIOPinVal.PinSet :
		IsSpindle3Up=1
	return IsSpindle3Up
def Spindle1Down():
	mod_IP.setDigitalIO(OutSpindle1,DIOPinVal.PinSet)       
def Spindle1Up():
	mod_IP.setDigitalIO(OutSpindle1,DIOPinVal.PinReset)
def Spindle2Down():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinSet)       
def Spindle2Up():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinReset)
def Spindle3Down():
	mod_IP.setDigitalIO(OutSpindle3,DIOPinVal.PinSet)       
def Spindle3Up():
	mod_IP.setDigitalIO(OutSpindle3,DIOPinVal.PinReset)
def IsOutSpindle1Active():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle1) == DIOPinVal.PinReset :
		IsOutSpindle1Active=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle1) == DIOPinVal.PinSet :
		IsOutSpindle1Active=1
	return IsOutSpindle1Active
def IsOutSpindle2Active():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle2) == DIOPinVal.PinReset :
		IsOutSpindle2Active=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle2) == DIOPinVal.PinSet :
		IsOutSpindle2Active=1
	return IsOutSpindle2Active
def IsOutSpindle3Active():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle3) == DIOPinVal.PinReset :
		IsOutSpindle3Active=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutSpindle3) == DIOPinVal.PinSet :
		IsOutSpindle3Active=1
	return IsOutSpindle3Active
ActTool=d.getSpindleToolNumber( )
NewTool=d.getSelectedToolNumber( )

########    END FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!   ###########


#######################   MACRO MAIN    #########################
#sprawdzenie czy wyjscie ktores aktywne jesli tak to czy ten sam offset jesli nie to blad!


#sprawdzenie czy narzedzie znajduje sie w zakresie magazynu
if (NewTool>3 or NewTool<0):
	msg.wrn("Nie ma takiego narzêdzia!")
	sys.exit("Wybrano narzedzie ktorego nie ma w zakresie, B³¹d wymiany narzêdzia!")

#sprawdzenie czy aktualne narzedzie = nowe narzedzie 
if (NewTool==ActTool):
	if (NewTool==1 and IsOutSpindle1Active()):
			print ("narzedzie 1 aktualnie zaladowane")
	elif (NewTool==2 and IsOutSpindle2Active()):
			print ("narzedzie 2 aktualnie zaladowane")
	elif (NewTool==3 and IsOutSpindle3Active()):
			print ("narzedzie 3 aktualnie zaladowane")
	elif (NewTool==0 and IsSpindle1Up() and IsSpindle2Up() and IsSpindle3Up()):
			print ("narzedzie 0 aktualnie zaladowane")
	#jesli nie ma wysterowanego wyjscia dla wybranego narzedzia wpusczenie do zmiany narzedzia
	else:
		e=1

# wyknanie zmiany narzedzia
if(NewTool!=ActTool or e):

	#podjazd osi z do gory
	pos=d.getPosition(CoordMode.Machine)
	pos[2]=ZSafeUpPos
	d.executeGCode("F8000")
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	
#zmiana wyjsc wysterowanie offsetow	
	if(NewTool==0):
		Spindle1Up()
		Spindle2Up()
		Spindle3Up()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(0)	
		d.setToolOffsetNumber(0)
	if(NewTool==1):
		Spindle2Up()
		Spindle3Up()
		Spindle1Down()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(1)	
		d.setToolOffsetNumber(1)
	if(NewTool==2):
		Spindle1Up()
		Spindle3Up()
		Spindle2Down()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(2)	
		d.setToolOffsetNumber(2)
	if(NewTool==3):
		Spindle1Up()
		Spindle2Up()
		Spindle3Down()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(3)	
		d.setToolOffsetNumber(3)
	
	

#sprawdzenie czy pozostale wrzeciona w gorze w razie braku cisnienia
if(d.getSpindleToolNumber( )==0 and  IsSpindle1Up() and IsSpindle2Up() and IsSpindle3Up() ):
	print("poprawnie zaladowano narzedzie: "+str(d.getSpindleToolNumber( )))
if(d.getSpindleToolNumber( )==1 and not IsSpindle1Up() and IsSpindle2Up() and IsSpindle3Up() ):
	print("poprawnie zaladowano narzedzie: "+str(d.getSpindleToolNumber( )))
elif(d.getSpindleToolNumber( )==2 and IsSpindle1Up() and not IsSpindle2Up() and IsSpindle3Up() ):
	print("poprawnie zaladowano narzedzie: "+str(d.getSpindleToolNumber( )))
elif(d.getSpindleToolNumber( )==3 and IsSpindle1Up() and  IsSpindle2Up() and not IsSpindle3Up() ):
	print("poprawnie zaladowano narzedzie: "+str(d.getSpindleToolNumber( )))
else:
		msg.wrn("Niepoprawne zaladowanie narzedzia- sprawdz cisnienie powietrza")
		sys.exit("Niepoprawnie zaladowanie narzedzia, B³¹d wymiany narzêdzia!")
######################   END MACRO MAIN    #######################



