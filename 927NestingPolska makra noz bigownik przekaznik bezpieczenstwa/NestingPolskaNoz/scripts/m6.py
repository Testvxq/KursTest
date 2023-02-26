#############################################
# POLSKA GRUPA CNC
#AUTO Tool Change noz bigownik
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
InGateOpen="14" 
OutSpindle1=4				#Wyjscie noza
OutSpindle2=5					#Wyjscie bigownika



DelayTime=1						#czas oczekiwania po zmianie narzedzia
ZSafeUpPos=-1					#podjazd do wyskokosci zmiany wrzeciona
###########DelayTime#######   END CONFIG BLOCK    ##########################


#######   FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!    ###############
 
mod_IP = d.getModule( ModuleType.IP, 0 )
def IsGateOpen():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InGateOpen) == DIOPinVal.PinReset :
		IsGateOpen=1
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InGateOpen) == DIOPinVal.PinSet :
		IsGateOpen=0
	return IsGateOpen
if(IsGateOpen()):
	msg.wrn("Przerwany sygnal bramek bezpieczenstwa'", "Warning!")
	sys.exit("Przerwany sygnal bramek bezpieczenstwa!")

e=0

mod_IP = d.getModule( ModuleType.IP, 0 )

def Spindle1Down():
	mod_IP.setDigitalIO(OutSpindle1,DIOPinVal.PinSet)       
def Spindle1Up():
	mod_IP.setDigitalIO(OutSpindle1,DIOPinVal.PinReset)
def Spindle2Down():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinSet)       
def Spindle2Up():
	mod_IP.setDigitalIO(OutSpindle2,DIOPinVal.PinReset)

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

ActTool=d.getSpindleToolNumber( )
NewTool=d.getSelectedToolNumber( )

########    END FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!   ###########


#######################   MACRO MAIN    #########################
#sprawdzenie czy wyjscie ktores aktywne jesli tak to czy ten sam offset jesli nie to blad!


#sprawdzenie czy narzedzie znajduje sie w zakresie magazynu
if (NewTool>2 or NewTool<0):
	msg.wrn("Nie ma takiego narzedzia!")
	sys.exit("Wybrano narzedzie ktorego nie ma w zakresie, Blad wymiany narzedzia!")

#sprawdzenie czy aktualne narzedzie = nowe narzedzie 
if (NewTool==ActTool):
	if (NewTool==1 and IsOutSpindle1Active()):
			print ("narzedzie 1 aktualnie zaladowane")
	elif (NewTool==2 and IsOutSpindle2Active() and IsOutSpindle1Active()):
			print ("narzedzie 2 aktualnie zaladowane")
	elif (NewTool==0):
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
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(0)	
		d.setToolOffsetNumber(0)
	if(NewTool==1):
		Spindle2Up()
		time.sleep(DelayTime)	
		Spindle1Down()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(1)	
		d.setToolOffsetNumber(1)
	if(NewTool==2):
		Spindle1Down()
		Spindle2Down()
		time.sleep(DelayTime)	
		d.setSpindleToolNumber(2)	
		d.setToolOffsetNumber(2)

print("poprawnie zaladowano narzedzie: "+str(d.getSpindleToolNumber( )))

######################   END MACRO MAIN    #######################



