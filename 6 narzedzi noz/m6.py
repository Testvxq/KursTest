#############################################
# POLSKA GRUPA CNC
#AUTO Tool Change v1.00
#############################################

import sys
import time

#############################################
# CONFIG BLOCK
#inputs
InDustCover="11"						#wejscie podniesienia szczotki 
InColletOpen="13"						#wejscie otwarcia szczek
InColletClose="14"						#wejscie zamkniecia szczek ze stozkiem
InSpindleRotation="12"			#wejscie obrot�w wrzeciona

#outputs
OutDustCover="4"					#wyjscie szczotki
OutCleanCone="5"					#wyjscie przedmuchu stozka(nie uzywane)
OutOpenCollet="2"				  	#wyjscie otwarcia szcz�k
OutFwd="1"									#wyjscie forward przepisac z konfiguracji wrzeciona (sprawdzenie czy nie jest w stanie aktywnym przed wymiana narzedzia)
OutCutter="3"							# wyjscie opuszenia noza
#tool change config
Capacity=7									#ilosc narzedzi w magazynie
SafeZ=-1								#wysokosc przejazdu nad stozkami(kordynaty maszynowe)
CleanConeHeight=10				#wysokosc przedmuchu stozka
ForslideY=2880	#pozycja wjazdy w magazyn po Y(PRETCPOSITION)
FastSpeed="F45000"				#predkosc dojazdu do pozycji forslide
EnterSpeed="F12000"				#predkosc wjazdu w magazyn (wjazd w uchwyt)
ZUpSpeed="F8000"					#predkosc podnoszenia po oddaniu narzedzia
ZDownSpeed="F8000"			#predkosc najazdu Z na stozek 
EscapeSpeed="F25000"		#predkosc wyjazdu z magazynu

T1=[500.6,2972.8,-78.32]						#pzycje narz�dzi kolejno po przecinkach x,y,z			
T2=[652.6,2971.654,-78.32]
T3=[801.6,2972.654,-78.32]
T4=[951.6,2972.053,-78.32]
T5=[1102.4,2971.854,-78.32]
T6=[1252.4,2971.454,-78.32]
#END CONFIG BLOCK
#############################################

#############################################
#FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!
mod_IP = d.getModule( ModuleType.IP, 0 )
def IsColletOpen():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InColletOpen) == DIOPinVal.PinReset :
		IsColletOpen=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InColletOpen) == DIOPinVal.PinSet :
		IsColletOpen=1
	return IsColletOpen
def IsColletClose():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InColletClose) == DIOPinVal.PinReset :
		IsColletClose=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InColletClose) == DIOPinVal.PinSet :
		IsColletClose=1
	return IsColletClose
def IsDustCoverUp():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InDustCover) == DIOPinVal.PinReset :
		IsDustCoverUp=0
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InDustCover) == DIOPinVal.PinSet :
		IsDustCoverUp=1
	return IsDustCoverUp
def IsSpindleRotate():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindleRotation) == DIOPinVal.PinReset :
		IsSpindleRotate=1
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InSpindleRotation) == DIOPinVal.PinSet :
		IsSpindleRotate=0
	return IsSpindleRotate
def IsFwdActive():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutFwd) == DIOPinVal.PinReset :
		IsFwdActive=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutFwd) == DIOPinVal.PinSet :
		IsFwdActive=1
	return IsFwdActive
def IsCutterDown():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutCutter) == DIOPinVal.PinReset :
		IsCutterDown=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutCutter) == DIOPinVal.PinSet :
		IsCutterDown=1
	return IsCutterDown
def ColletOpen():
	mod_IP.setDigitalIO(OutOpenCollet,DIOPinVal.PinSet)       
def ColletClose():
	mod_IP.setDigitalIO(OutOpenCollet,DIOPinVal.PinReset)
def DustCoverUp():
	mod_IP.setDigitalIO(OutDustCover,DIOPinVal.PinSet)                              
def DustCoverDown():
	mod_IP.setDigitalIO(OutDustCover,DIOPinVal.PinReset)                           
def CleanConeOn():
	mod_IP.setDigitalIO(OutCleanCone,DIOPinVal.PinSet)                             
def CleanConeOff():
	mod_IP.setDigitalIO(OutCleanCone,DIOPinVal.PinReset)                         
def CutterDown():
	mod_IP.setDigitalIO(OutCutter,DIOPinVal.PinSet)       
def CutterUp():
	mod_IP.setDigitalIO(OutCutter,DIOPinVal.PinReset)                
#END FUNKCJON  DEFINITION
#############################################

#############################################
#VARIABLES  DECLARATION -DO NOT CHANGE ANYTHING!!!
ActToolPos=d.getPosition(CoordMode.Machine)
NewToolPos=d.getPosition(CoordMode.Machine)
pos=d.getPosition(CoordMode.Machine)
ActTool=d.getSpindleToolNumber( )
NewTool=d.getSelectedToolNumber( )
e=0
#END WARIABLES  DECLARATION
#############################################
#############################################
#assigning the tool position value
if  (ActTool==1):
	ActToolPos[0]=T1[0]
	ActToolPos[1]=T1[1]
	ActToolPos[2]=T1[2]
if  (ActTool==2):
	ActToolPos[0]=T2[0]
	ActToolPos[1]=T2[1]
	ActToolPos[2]=T2[2]
if  (ActTool==3):
	ActToolPos[0]=T3[0]
	ActToolPos[1]=T3[1]
	ActToolPos[2]=T3[2]
if  (ActTool==4):
	ActToolPos[0]=T4[0]
	ActToolPos[1]=T4[1]
	ActToolPos[2]=T4[2]
if  (ActTool==5):
	ActToolPos[0]=T5[0]
	ActToolPos[1]=T5[1]
	ActToolPos[2]=T5[2]
if  (ActTool==6):
	ActToolPos[0]=T6[0]
	ActToolPos[1]=T6[1]
	ActToolPos[2]=T6[2]


if  (NewTool==1):
	NewToolPos[0]=T1[0]
	NewToolPos[1]=T1[1]
	NewToolPos[2]=T1[2]
if  (NewTool==2):
	NewToolPos[0]=T2[0]
	NewToolPos[1]=T2[1]
	NewToolPos[2]=T2[2]
if  (NewTool==3):
	NewToolPos[0]=T3[0]
	NewToolPos[1]=T3[1]
	NewToolPos[2]=T3[2]
if  (NewTool==4):
	NewToolPos[0]=T4[0]
	NewToolPos[1]=T4[1]
	NewToolPos[2]=T4[2]
if  (NewTool==5):
	NewToolPos[0]=T5[0]
	NewToolPos[1]=T5[1]
	NewToolPos[2]=T5[2]
if  (NewTool==6):
	NewToolPos[0]=T6[0]
	NewToolPos[1]=T6[1]
	NewToolPos[2]=T6[2]

#END assigning the tool position value
#############################################
#############################################
#Macro main
#d.setNextGCodeLine()
if(ActTool>Capacity or ActTool<0):  																#sprawdzene czy akualne narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("zaladowane narzedzie poza zakresem!")
if(NewTool>Capacity or NewTool<0):																	#sprawdzene czy wybrane narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("Nie ma takiego narzedzia!")
if(ActTool==NewTool):																				# sprawdzenie czy aktualne i nowe narzedzie to nie to samo + sprawdzenie obecnosci stozka
	if(ActTool==0):
		if not  IsColletClose():																	#sprawdzenie czy stozek we wrzecionie przy aktualnym narzedziu 0
			sys.exit("Narzedzie 0 aktualnie zaladowane")
		else:
			sys.exit("Narzedzie znajduje sie w uchwycie, blad wymiany narzedzia!")
	else:																							# stozek w szczekach przy narzedziach 
		if (IsColletClose()and ActTool<7):																			#jesli jest stozek to ok
			print ("narzedzie aktualnie zaladowane")
			#d.setNextGCodeLine()
			e=1
		if(ActTool==7 and IsCutterDown()):
			print("noz aktualnie zaladowany")
			e=1
		else:																						#jesli nie ma stozka dla narzedzia aktualnie zaladowanego toblad!
				if (IsColletClose()and ActTool>6):																			#jesli jest stozek to ok
					print ("podaj poprawne narzedzie we wrzecionie")
					sys.exit("brak stozka w szczekach wrzeciona,lub nieopuszczony noz blad wymiany narzedzia!")

############           Od�o�enie narz�dzia        ################
if(e<1):
	d.setTangentialAxisEnable(False)
	d.setSpindleState( SpindleState.OFF)
	d.executeGCode(FastSpeed)
	#time.sleep(3)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	DustCoverUp()
	pos[3]=0
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f} A{:f}".format(pos[0],pos[1],pos[2],pos[3]))
	i=0
	while  i<50:
		if  (IsDustCoverUp()):
			i=51
		else:
			i=i+1
			time.sleep(.1)
	if(i<=50):
		DustCoverDown()
		msg.wrn("Nie mozna podniesc szczotki Blad wymiany narzedzia", "Warning!")
		sys.exit("Nie mozna podniesc szczotki, Blad wymiany narzedzia!")

if(IsColletClose() and e<1):																																					#jesli zamkniete szczeki ze stozkiem
	if(ActTool==0 or ActTool==7):																																			#jesli aktualne 0 i stozek w szczekach to blad
		DustCoverDown()
		msg.wrn("W szczekach wrzeciona znajduje sie stozek, niedopuszczalne dla narzedzia 0,7", "Warning!")
		sys.exit("Dla narzedzia 0 wykryty sygnal obecnosci stozka, Blad wymiany narzedzia!")
	d.executeGCode(FastSpeed)																																				#wykonanie od�o�enia narzedzia 
	d.setSoftLimitsState( Axis.Y, False )
	CutterUp()
	pos[0]=ActToolPos[0]
	pos[1]=ForslideY
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[2]=ActToolPos[2]
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	if(IsFwdActive()):
		msg.err("Wrzeciono wylczone", "ERROR!")
		sys.exit("Sygnal obrotow wrzeciona aktywny, Blad wymiany narzedzia!")
		d.setSoftLimitsState( Axis.Y, True)
		DustCoverDown()
	d.executeGCode(EnterSpeed)
	pos[1]=ActToolPos[1]
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	time.sleep(.4)
	ColletOpen()
	i=0
	while  i<50:
		if  (IsColletOpen()):
			i=51
		else:
			i=i+1
			time.sleep(.1)
	if(i<=50):
		ColletClose()
		d.executeGCode(EscapeSpeed)
		pos[1]=ForslideY
		#d.goToAbsolute(pos)
		d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
		d.setSoftLimitsState( Axis.Y, True)
		DustCoverDown()
		msg.wrn("Nie mozna otwozyc szczek, Blad wymiany narzedzia", "Warning!")
		sys.exit("Nie mozna otworzyc szczeki, Blad wymiany narzzdzia!")
	d.executeGCode(ZUpSpeed)
	pos[2]=SafeZ
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	ColletClose()
if(ActTool==7 and e<1):
    CutterUp()

############## Pobranie narz�dzia###################
if(NewTool==7 and e<1):
	e=1
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[1]=ForslideY-350
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	d.setTangentialAxisEnable(True)
	CutterDown()
	d.setSpindleToolNumber(NewTool)
	d.setToolOffsetNumber(NewTool)
	d.setSoftLimitsState( Axis.Y, True)
	print("zmieniono narzedzie na {:d}".format(NewTool))
if(NewTool==0 and e<1):																								#jezeli 0 aktualizacja i koniec
	d.executeGCode(FastSpeed)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[3]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f} A{:f}".format(pos[0],pos[1],pos[2],pos[3]))
	#pos[1]=ForslideY
	#d.goToAbsolute(pos) 
	#d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	#d.updateSpindleToolNr(NewTool)
	d.executeGCode( "G49")
	DustCoverDown()
	print ("zmieniono narzedzie na {:d}".format(NewTool))
	d.setSpindleToolNumber(NewTool)
	d.setToolOffsetNumber(NewTool)
	d.setSoftLimitsState( Axis.Y, True)
	e=1

if(NewTool>0 and NewTool<7 and e<1):																				#jezeli narzedzia sozkowe pobrac i koniec
	d.setSoftLimitsState( Axis.Y, False)
	d.executeGCode(FastSpeed)
	pos[0]=NewToolPos[0]
	pos[1]=NewToolPos[1]
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	ColletOpen()
	i=0
	while  i<50:
		if  (IsColletOpen()):
			i=51
		else:
			i=i+1
			time.sleep(.1)
	if(i<=50):
		ColletClose()
		d.executeGCode(EscapeSpeed)
		pos[1]=ForslideY
		#d.goToAbsolute(pos)
		d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
		d.setSoftLimitsState( Axis.Y, True)
		DustCoverDown()
		msg.wrn("Nie mozna otwozyc szczek, Blad wymiany narzedzia", "Warning!")
		sys.exit("Nie mozna otworzyc szczeki, Blad wymiany narzedzia!")
	d.executeGCode(ZDownSpeed)
	pos[2]=NewToolPos[2]
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	ColletClose()
	i=0
	while  i<50:
		if  (IsColletClose()):
			i=51
		else:
			i=i+1
			time.sleep(.1)
	if(i<=50):
		d.executeGCode(EscapeSpeed)
		pos[1]=ForslideY
		#d.goToAbsolute(pos)
		d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
		DustCoverDown()
		d.setSoftLimitsState( Axis.Y, True)
		msg.wrn("Brak narzedzia w szczekach, Blad wymiany narzedzia", "Warning!")
		sys.exit("Brak narzedzia w szczekachi, Blad wymiany narzedzia!")

	d.executeGCode(EscapeSpeed)
	pos[1]=ForslideY
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	d.executeGCode(FastSpeed)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[1]=ForslideY-350
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	d.setSpindleToolNumber(NewTool)
	d.setToolOffsetNumber(NewTool)
	d.setSoftLimitsState( Axis.Y, True)
	#d.updateSpindleToolNr(NewTool)
	#d.executeGCode( "g43 h{:d}".format(NewTool))
	DustCoverDown()
	print("zmieniono narzedzie na {:d}".format(NewTool))

	e=1

#END Macro main
#############################################