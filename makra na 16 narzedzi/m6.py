#############################################
# POLSKA GRUPA CNC
#AUTO Tool Change v1.00
#############################################

import sys
import time

#############################################
# CONFIG BLOCK
#inputs
InDustCover="7"						#wejscie podniesienia szczotki 
InColletOpen="5"						#wejscie otwarcia szczek
InColletClose="6"						#wejscie zamkniecia szczek ze stozkiem
InSpindleRotation="12"			#wejscie obrot�w wrzeciona
#outputs
OutDustCover="3"					#wyjscie szczotki
OutCleanCone="15"					#wyjscie przedmuchu stozka(nie uzywane)
OutOpenCollet="2"				  	#wyjscie otwarcia szcz�k
OutFwd="1"									#wyjscie forward przepisac z konfiguracji wrzeciona (sprawdzenie czy nie jest w stanie aktywnym przed wymiana narzedzia)
#tool change config
Capacity=16									#ilosc narzedzi w magazynie
SafeZ=0									#wysokosc przejazdu nad stozkami(kordynaty maszynowe)
CleanConeHeight=10				#wysokosc przedmuchu stozka
ForslideY=3250			#pozycja wjazdy w magazyn po Y(PRETCPOSITION)
FastSpeed="F40000"				#predkosc dojazdu do pozycji forslide
EnterSpeed="F6000"				#predkosc wjazdu w magazyn (wjazd w uchwyt)
ZUpSpeed="F6000"					#predkosc podnoszenia po oddaniu narzedzia
ZDownSpeed="F6000"			#predkosc najazdu Z na stozek 
EscapeSpeed="F15000"		#predkosc wyjazdu z magazynu

#tool position [X,Y,Z]
T1=[100.219,3381.331,-129.500]						#pzycje narz�dzi kolejno po przecinkach x,y,z			
T2=[251.019,3380.631,-129.800]
T3=[400.523,3380.031,-129.500]
T4=[550.861,3379.930,-129.800]
T5=[700.809,3379.211,-129.700]
T6=[851.608,3378.911,-129.800]
T7=[1001.003,3378.611,-129.900]
T8=[1151.303,3378.533,-130.000]
T9=[1300.900,3377.430,-130.000]
T10=[1451.000,3377.330,-129.900]
T11=[1600.600,3376.730,-129.900]
T12=[1751.200,3376.230,-129.700]
T13=[1900.895,3375.900,-129.931]
T14=[2050.494,3376.000,-129.730]
T15=[1900.895,3375.900,-129.931]
T16=[2050.494,3376.000,-129.730]
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
if  (ActTool==7):
	ActToolPos[0]=T7[0]
	ActToolPos[1]=T7[1]
	ActToolPos[2]=T7[2]
if  (ActTool==8):
	ActToolPos[0]=T8[0]
	ActToolPos[1]=T8[1]
	ActToolPos[2]=T8[2]
if  (ActTool==9):
	ActToolPos[0]=T9[0]
	ActToolPos[1]=T9[1]
	ActToolPos[2]=T9[2]
if  (ActTool==10):
	ActToolPos[0]=T10[0]
	ActToolPos[1]=T10[1]
	ActToolPos[2]=T10[2]
if  (ActTool==11):
	ActToolPos[0]=T11[0]
	ActToolPos[1]=T11[1]
	ActToolPos[2]=T11[2]
if  (ActTool==12):
	ActToolPos[0]=T12[0]
	ActToolPos[1]=T12[1]
	ActToolPos[2]=T12[2]
if  (ActTool==13):
	ActToolPos[0]=T13[0]
	ActToolPos[1]=T13[1]
	ActToolPos[2]=T13[2]
if  (ActTool==14):
	ActToolPos[0]=T14[0]
	ActToolPos[1]=T14[1]
	ActToolPos[2]=T14[2]
if  (ActTool==15):
	ActToolPos[0]=T15[0]
	ActToolPos[1]=T15[1]
	ActToolPos[2]=T15[2]
if  (ActTool==16):
	ActToolPos[0]=T16[0]
	ActToolPos[1]=T16[1]
	ActToolPos[2]=T16[2]

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
if  (NewTool==7):
	NewToolPos[0]=T7[0]
	NewToolPos[1]=T7[1]
	NewToolPos[2]=T7[2]
if  (NewTool==8):
	NewToolPos[0]=T8[0]
	NewToolPos[1]=T8[1]
	NewToolPos[2]=T8[2]
if  (NewTool==9):
	NewToolPos[0]=T9[0]
	NewToolPos[1]=T9[1]
	NewToolPos[2]=T9[2]
if  (NewTool==10):
	NewToolPos[0]=T10[0]
	NewToolPos[1]=T10[1]
	NewToolPos[2]=T10[2]
if  (NewTool==11):
	NewToolPos[0]=T11[0]
	NewToolPos[1]=T11[1]
	NewToolPos[2]=T11[2]
if  (NewTool==12):
	NewToolPos[0]=T12[0]
	NewToolPos[1]=T12[1]
	NewToolPos[2]=T12[2]
if  (NewTool==13):
	NewToolPos[0]=T13[0]
	NewToolPos[1]=T13[1]
	NewToolPos[2]=T13[2]
if  (NewTool==14):
	NewToolPos[0]=T14[0]
	NewToolPos[1]=T14[1]
	NewToolPos[2]=T14[2]
if  (NewTool==15):
	NewToolPos[0]=T15[0]
	NewToolPos[1]=T15[1]
	NewToolPos[2]=T15[2]
if  (NewTool==16):
	NewToolPos[0]=T16[0]
	NewToolPos[1]=T16[1]
	NewToolPos[2]=T16[2]

#END assigning the tool position value
#############################################
#############################################
#Macro main
#d.setNextGCodeLine()
if(ActTool>Capacity or ActTool<0):  																#sprawdzene czy akualne narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("za�adowane narz�dzie poza zakresem!")
if(NewTool>Capacity or NewTool<0):																	#sprawdzene czy wybrane narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("Nie ma takiego narz�dzia!")
if(ActTool==NewTool):																				# sprawdzenie czy aktualne i nowe narzedzie to nie to samo + sprawdzenie obecnosci stozka
	if(ActTool==0):
		if not  IsColletClose():																	#sprawdzenie czy stozek we wrzecionie przy aktualnym narzedziu 0
			sys.exit("Narz�dzie 0 aktualnie za�adowane")
		else:
			sys.exit("Narzedzie znajduje sie w uchwycie, b��d wymiany narz�dzia!")
	else:																							# stozek w szczekach przy narzedziach 
		if IsColletClose():																			#jesli jest stozek to ok
			print ("narzedzie aktualnie zaladowane")
			#d.setNextGCodeLine()
			e=1
		else:																						#jesli nie ma stozka dla narzedzia aktualnie zaladowanego toblad!
			sys.exit("brak sto�ka w szcz�kach wrzeciona,lub nieopuszczony noz b��d wymiany narz�dzia!")
############           Od�o�enie narz�dzia        ################
if(e<1):
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
		msg.wrn("Nie mo�na podnie�� szczotki B��d wymiany narz�dzia", "Warning!")
		sys.exit("Nie mo�na podnie�� szczotki, B��d wymiany narz�dzia!")

if(IsColletClose() and e<1):																																					#jesli zamkniete szczeki ze stozkiem
	if(ActTool==0):																																			#jesli aktualne 0 i stozek w szczekach to blad
		DustCoverDown()
		msg.wrn("W szcz�kach wrzeciona znajduje si� sto�ek, niedopuszczalne dla narzedzia 0", "Warning!")
		sys.exit("Dla narz�dzia 0 wykryty sygna� obecno�ci sto�ka, B��d wymiany narz�dzia!")
	d.executeGCode(FastSpeed)																																				#wykonanie od�o�enia narzedzia 
	d.setSoftLimitsState( Axis.Y, False )
	pos[0]=ActToolPos[0]
	pos[1]=ForslideY
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[2]=ActToolPos[2]
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	if(IsFwdActive()):
		msg.err("Wrzeciono w��czone", "ERROR!")
		sys.exit("Sygna� obrot�w wrzeciona aktywny, B��d wymiany narz�dzia!")
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
		msg.wrn("Nie mo�na otwozyc szczek, B��d wymiany narz�dzia", "Warning!")
		sys.exit("Nie mo�na otworzyc szczeki, B��d wymiany narz�dzia!")
	d.executeGCode(ZUpSpeed)
	pos[2]=SafeZ
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	ColletClose()


############## Pobranie narz�dzia###################

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

if(NewTool>0 and NewTool<17 and e<1):																				#jezeli narzedzia sozkowe pobrac i koniec
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
		msg.wrn("Nie mo�na otwozyc szczek, B��d wymiany narz�dzia", "Warning!")
		sys.exit("Nie mo�na otworzyc szczeki, B��d wymiany narz�dzia!")
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
		msg.wrn("Brak narzedzia w szczekach, B��d wymiany narz�dzia", "Warning!")
		sys.exit("Brak narzedzia w szczekachi, B��d wymiany narz�dzia!")

	d.executeGCode(EscapeSpeed)
	pos[1]=ForslideY
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	d.executeGCode(FastSpeed)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[1]=ForslideY-200
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

