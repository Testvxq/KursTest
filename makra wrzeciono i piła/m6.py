#############################################
# POLSKA GRUPA CNC
##############################################

import sys
import time

#############################################
# WARNING BLOCK
# comment this block when you set settings below
#msg.wrn("Setup m6 macro first!\n\nMenu 'Macro->Show Script Editor and choose 'm6'", "Warning!")
#sys.exit("Error! Probing macro not configured!")
# END WARNING BLOCK
#############################################

#############################################
# CONFIG BLOCK
#inputs
InSawHorizontal="15"                #wejscie polożenia pily ronolegle do x/y 
#outputs
OutSawLock="14"                     #blokada pily (bolec)
OutAgregatLock="11"					#blokada opuszczania piły(Rygiel)
OutSawRotation="13"                 #obracanie pily prawo lewo
OutSawUpDown="12"                   #opuszczanie podnoszenie pily

#tool change config
SafeZ=0								#wysokosc wymiany narzedzia
FastSpeed="F18000"					#predkosc dojazdu do pozycji forslide
EnterSpeed="F5000"					#predkosc wjazdu w magazyn (wjazd w uchwyt)
ZUpSpeed="F3000"					#predkosc podnoszenia po oddaniu narzedzia
ZDownSpeed="F3000"			        #predkosc najazdu Z na stozek
EscapeSpeed="F9000"			        #predkosc wyjazdu z magazynu



#END CONFIG BLOCK
#############################################

#############################################
#FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!
mod_IP = d.getModule( ModuleType.IP, 0 )

def IsSawHorizontal():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSawHorizontal) == DIOPinVal.PinReset :
		IsSawHorizontal=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSawHorizontal) == DIOPinVal.PinSet :
		IsSawHorizontal=1
	return IsSawHorizontal    
   
    
    
    
def RygielOpen():
	mod_IP.setDigitalIO(OutAgregatLock,DIOPinVal.PinSet)       
def RygielClose():
	mod_IP.setDigitalIO(OutAgregatLock,DIOPinVal.PinReset)
def SawLockerUp():
	mod_IP.setDigitalIO(OutSawLock,DIOPinVal.PinSet)  
def SawLockerDown():
	mod_IP.setDigitalIO(OutSawLock,DIOPinVal.PinReset)
def SawDown():
	mod_IP.setDigitalIO(OutSawUpDown,DIOPinVal.PinSet)
def SawUp():
	mod_IP.setDigitalIO(OutSawUpDown,DIOPinVal.PinReset)
def SawHorizontal():
	mod_IP.setDigitalIO(OutSawRotation,DIOPinVal.PinSet)
def SawVertical():
	mod_IP.setDigitalIO(OutSawRotation,DIOPinVal.PinReset)    

  
                
#END FUNKCJON  DEFINITION
#############################################

#############################################
#VARIABLES  DECLARATION -DO NOT CHANGE ANYTHING!!!
ActToolPos=1
NewToolPos=1
pos=d.getPosition(CoordMode.Machine)
ActTool=d.getSpindleToolNumber( )
NewTool=d.getSelectedToolNumber( )
e=0
#END WARIABLES  DECLARATION
#############################################
#############################################
#Macro main
#d.setNextGCodeLine()
if(ActTool>3 or ActTool<0):  																#sprawdzene czy akualne narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("załadowane narzędzie poza zakresem!")
if(NewTool>3 or NewTool<1):																	#sprawdzene czy wybrane narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("Nie ma takiego narzędzia!")


############## Pobranie narzędzia###################
pos[2]=SafeZ
d.executeGCode("G1G53 X{:f} Y{:f} Z{:f} B{:f}".format(pos[0],pos[1],pos[2],pos[4]))
if(NewTool==1):
	RygielOpen()
	time.sleep(1)
	SawUp()
	time.sleep(1)
	RygielClose()
if(NewTool==2):
	if(IsSawHorizontal()):
		RygielOpen()
		time.sleep(1)
		SawDown()
		time.sleep(1)
	else:
		print("1")
		SawVertical()
		time.sleep(1)
		print("2")
		SawLockerUp()
		time.sleep(1)
		print("3")
		SawHorizontal()
		i=0
		while  i<50:
			if  (IsSawHorizontal()):
				i=51
			else:
				i=i+1
				time.sleep(.1)
		if(i<=50):
			SawVertical()
			time.sleep(1)
			SawLockerDown()
			d.setSoftLimitsState( Axis.X, True )
			msg.wrn("Nie można przekrecic pily", "Warning!")
			sys.exit("Nie przekrecic pily, Błąd wymiany narzędzia!") 
		SawLockerDown()
		time.sleep(1)
		RygielOpen()
		time.sleep(1)
		SawDown()
		time.sleep(1)
if(NewTool==3):
	if(IsSawHorizontal()==0):
		RygielOpen()
		time.sleep(1)
		SawDown()
		time.sleep(1)
	else:
		SawHorizontal()
		time.sleep(1)
		SawLockerUp()
		time.sleep(1)
		SawVertical()
		i=0
		while  i<50:
			if  (IsSawHorizontal()==0):
				i=51
			else:
				i=i+1
				time.sleep(.1)
		if(i<=50):
			SawHorizontal()
			time.sleep(1)
			SawLockerDown()
			time.sleep(1)
			d.setSoftLimitsState( Axis.X, True )
			msg.wrn("Nie można przekrecic pily xxx", "Warning!")
			sys.exit("Nie przekrecic pily, Błąd wymiany narzędzia!") 
		SawLockerDown()
		time.sleep(1)
		RygielOpen()
		time.sleep(1)
		SawDown()
		time.sleep(1)              
print ("zmieniono narzedzie na {:d}".format(NewTool))
d.setSpindleToolNumber(NewTool)
d.setToolOffsetNumber(NewTool)

#END Macro main
#############################################

