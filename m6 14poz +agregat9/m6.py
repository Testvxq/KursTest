#############################################
# POLSKA GRUPA CNC
#AUTO Tool Change v1.00
#############################################

import sys
import time

#############################################
# CONFIG BLOCK
#inputs
InDustCover="10"						#wejscie podniesienia szczotki 
InColletOpen="8"						#wejscie otwarcia szczek
InColletClose="9"						#wejscie zamkniecia szczek ze stozkiem
InSpindleRotation="13"			#wejscie obrotow wrzeciona

#outputs IP
OutDustCover="3"					#wyjscie szczotki
OutOpenCollet="2"				  	#wyjscie otwarcia szczek
OutFwd="1"									#wyjscie forward przepisac z konfiguracji wrzeciona (sprawdzenie czy nie jest w stanie aktywnym przed wymiana narzedzia)

OutT15="11"			#	wyjscie narzedzia t15 agregatu
OutT16="12"			#	wyjscie narzedzia t16 agregatu
OutT17="4"				#wyjscie narzedzia t17 agregatu
OutT18="5"				#wyjscie narzedzia t18 agregatu
OutT19="6"				#wyjscie narzedzia t19 agregatu
OutT20="7"				#wyjscie narzedzia t20 agregatu
OutT21="8"			#	wyjscie narzedzia t21 agregatu
OutT22="9"			#	wyjscie narzedzia t22 agregatu
OutT23="10"			#	wyjscie narzedzia t23 agregatu



OutRygiel="15"		#wyjscie ryglowania agregatu (IO)
OutAgregat="13"	#wyjscie opuszczania agregatu	(IO)


#tool change config
Capacity=23								#ilosc narzedzi w magazynie
SafeZ=-10									#wysokosc przejazdu nad stozkami(kordynaty maszynowe)
CleanConeHeight=10				#wysokosc przedmuchu stozka
ForslideY=3270						#pozycja wjazdy w magazyn po Y(PRETCPOSITION)
FastSpeed="F45000"				#predkosc dojazdu do pozycji forslide
EnterSpeed="F10000"			#predkosc wjazdu w magazyn (wjazd w uchwyt)
ZUpSpeed="F8000"					#predkosc podnoszenia po oddaniu narzedzia
ZDownSpeed="F8000"				#predkosc najazdu Z na stozek 
EscapeSpeed="F25000"			#predkosc wyjazdu z magazynu

#tool position [X,Y,Z]
T1=[339.400,3414.100,-156.200]						#pzycje narz�dzi kolejno po przecinkach x,y,z			
T2=[479.400,3412.800,-156.200]
T3=[619.400,3412.800,-157.200]
T4=[759.300,3411.800,-157.200]
T5=[899.700,3414.000,-157.400]
T6=[1039.800,3412.400,-157.200]
T7=[1179.200,3413.300,-157.200]
T8=[1319.200,3413.700,-157.200]
T9=[1459.200,3413.000,-157.200]
T10=[1599.200,3413.300,-157.300]
T11=[1739.200,3413.075,-157.300]
T12=[1879.200,3412.700,-157.300]
T13=[2019.200,3412.300,-157.300]
T14=[2158.300,3413.100,-157.300]
#END CONFIG BLOCK
#############################################

#############################################
#FUNKCJON  DEFINITION -DO NOT CHANGE ANYTHING!!!
mod_IP = d.getModule( ModuleType.IP, 0 )
#obsluga IP
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
def T15Down():
	mod_IP.setDigitalIO(OutT15,DIOPinVal.PinSet)       
def T15Up():
	mod_IP.setDigitalIO(OutT15,DIOPinVal.PinReset)
def T16Down():
	mod_IP.setDigitalIO(OutT16,DIOPinVal.PinSet)       
def T16Up():
	mod_IP.setDigitalIO(OutT16,DIOPinVal.PinReset)
def T17Down():
	mod_IP.setDigitalIO(OutT17,DIOPinVal.PinSet)       
def T17Up():
	mod_IP.setDigitalIO(OutT17,DIOPinVal.PinReset) 
def T18Down():
	mod_IP.setDigitalIO(OutT18,DIOPinVal.PinSet)       
def T18Up():
	mod_IP.setDigitalIO(OutT18,DIOPinVal.PinReset)
def T19Down():
	mod_IP.setDigitalIO(OutT19,DIOPinVal.PinSet)       
def T19Up():
	mod_IP.setDigitalIO(OutT19,DIOPinVal.PinReset)
def T20Down():
	mod_IP.setDigitalIO(OutT20,DIOPinVal.PinSet)       
def T20Up():
	mod_IP.setDigitalIO(OutT20,DIOPinVal.PinReset)
def T21Down():
	mod_IP.setDigitalIO(OutT21,DIOPinVal.PinSet)       
def T21Up():
	mod_IP.setDigitalIO(OutT21,DIOPinVal.PinReset)
def T22Down():
	mod_IP.setDigitalIO(OutT22,DIOPinVal.PinSet)       
def T22Up():
	mod_IP.setDigitalIO(OutT22,DIOPinVal.PinReset)
def T23Down():
	mod_IP.setDigitalIO(OutT23,DIOPinVal.PinSet)       
def T23Up():
	mod_IP.setDigitalIO(OutT23,DIOPinVal.PinReset)

def IsAgregatDown():
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutAgregat) == DIOPinVal.PinReset :
		IsAgregatDown=0
	if mod_IP.getDigitalIO( IOPortDir.OutputPort, OutAgregat) == DIOPinVal.PinSet :
		IsAgregatDown=1
	return IsAgregatDown                        
def RygielOpen():
	mod_IP.setDigitalIO(OutRygiel,DIOPinVal.PinSet)       
def RygielClose():
	mod_IP.setDigitalIO(OutRygiel,DIOPinVal.PinReset)   
def AgregatDown():
	mod_IP.setDigitalIO(OutAgregat,DIOPinVal.PinSet)       
def AgregatUp():
	mod_IP.setDigitalIO(OutAgregat,DIOPinVal.PinReset)
       
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


#END assigning the tool position value
#############################################
#############################################
#Macro main
#d.setNextGCodeLine()
if(ActTool>Capacity or ActTool<0):  															#sprawdzene czy akualne narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("zaladowane narzedzie poza zakresem!")
if(NewTool>Capacity or NewTool<0):																	#sprawdzene czy wybrane narzedzie miesci sie w zakresie pojemnoaci magazyny
	sys.exit("Nie ma takiego narzedzia!")
if(ActTool==NewTool):																								# sprawdzenie czy aktualne i nowe narzedzie to nie to samo + sprawdzenie obecnosci stozka
	if(ActTool==0):
		if(not IsColletClose()and not IsAgregatDown()) :																				#sprawdzenie czy stozek we wrzecionie przy aktualnym narzedziu 0 lub niewypuszczony agregat
			sys.exit("Narzedzie 0 aktualnie zaladowane")
		else:
			sys.exit("Narzedzie znajduje sie w uchwycie lub agregat opuszczony dla aktualnego 0, blad wymiany narzedzia!")
	else:																							# stozek w szczekach przy narzedziach 
		if (IsColletClose()and ActTool<15 and (not IsAgregatDown())):																			#jesli jest stozek dla aktualnego 1-14 i podniesiony agregat to ok
			print ("narzedzie stozkowe aktualnie zaladowane")
			e=1
		elif (( not IsColletClose())and ActTool>14 and IsAgregatDown()):																			#jesli jest stozek dla aktualnego 1-14 to ok
			print ("narzedzie agregat aktualnie zaladowane")
			e=1
		else:																						#jesli nie ma stozka lub agregat nieopuszczony dla narzedzia aktualnie zaladowanego toblad!
			sys.exit("brak stozka w szczekach wrzeciona lub nieopuszczony agregat,lub nieopuszczony noz blad wymiany narzedzia!")
############           Odlozenie narzedzia        ################
if(e<1):
	if(ActTool>14 and NewTool>14):
		print("zmiana agregat-agregat")
	else:
		d.setSpindleState( SpindleState.OFF)
	d.executeGCode(FastSpeed)
	#time.sleep(3)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2],pos[3]))
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
print (IsColletClose())
print (e)
if(IsColletClose() and e<1):																																					#jesli zamkniete szczeki ze stozkiem
	AgregatUp()
	time.sleep(2)
	RygielClose() 
	if(ActTool==0 or ActTool>14):																																			#jesli aktualne 0 lub agregat i stozek w szczekach to blad
		DustCoverDown()
		msg.wrn("W szczekach wrzeciona znajduje sie stozek, niedopuszczalne dla narzedzia 0, lub>10", "Warning!")
		sys.exit("Dla narzedzia 0 lub agregatu  wykryty sygnal obecnosci stozka, Blad wymiany narzedzia!")
	d.executeGCode(FastSpeed)																																				#wykonanie odlozenia narzedzia 
	d.setSoftLimitsState( Axis.Y, False )
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
	if (NewTool>14 or NewTool==0):
		pos[2]=0
		d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
		pos[1]=ForslideY-350
		d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
		d.setSoftLimitsState( Axis.Y, True)		

if(ActTool>14 and e<1 and NewTool<15):
	pos[2]=0
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	RygielOpen()
	AgregatUp()
	T15Up()
	T16Up()
	T17Up()
	T18Up()
	T19Up()
	T20Up()
	T21Up()
	T22Up()
	T23Up()
	time.sleep(2)
	RygielClose()

############## Pobranie narzedzia###################
if(NewTool>14 and e<1):
	pos[2]=0
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	RygielOpen()
	time.sleep(1)
	AgregatDown()
	if(NewTool==15):
		T15Down()
		T16Up()
		T17Up()
		T18Up()
		T19Up()
		T20Up()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==16):
		T15Up()
		T16Down()
		T17Up()
		T18Up()
		T19Up()
		T20Up()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==17):
		T15Up()
		T16Up()
		T17Down()
		T18Up()
		T19Up()
		T20Up()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==18):
		T15Up()
		T16Up()
		T17Up()
		T18Down()
		T19Up()
		T20Up()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==19):
		T15Up()
		T16Up()
		T17Up()
		T18Up()
		T19Down()
		T20Up()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==20):
		T15Up()
		T16Up()
		T17Up()
		T18Up()
		T19Up()
		T20Down()
		T21Up()
		T22Up()
		T23Up()
	if(NewTool==21):
		T15Up()
		T16Up()
		T17Up()
		T18Up()
		T19Up()
		T20Up()
		T21Down()
		T22Up()
		T23Up()
	if(NewTool==22):
		T15Up()
		T16Up()
		T17Up()
		T18Up()
		T19Up()
		T20Up()
		T21Up()
		T22Down()
		T23Up()
	if(NewTool==23):
		T15Up()
		T16Up()
		T17Up()
		T18Up()
		T19Up()
		T20Up()
		T21Up()
		T22Up()
		T23Down()



	d.setSoftLimitsState( Axis.Y, True)
	print ("zmieniono narzedzie na {:d}".format(NewTool))
	d.setSpindleToolNumber(NewTool)
	d.setToolOffsetNumber(NewTool)
	e=1
if(NewTool==0 and e<1):																								#jezeli 0 aktualizacja i koniec
	d.executeGCode(FastSpeed)
	pos[2]=0
	#d.goToAbsolute(pos)
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	pos[3]=0
	d.executeGCode("G1G53 X{:f} Y{:f} Z{:f}".format(pos[0],pos[1],pos[2]))
	#d.updateSpindleToolNr(NewTool)
	RygielOpen()
	AgregatUp()
	T15Up()
	T16Up()
	T17Up()
	T18Up()
	T19Up()
	T20Up()
	T21Up()
	T22Up()
	T23Up()

	time.sleep(2)
	RygielClose()
	d.executeGCode( "G49")
	DustCoverDown()
	print ("zmieniono narzedzie na {:d}".format(NewTool))
	d.setSpindleToolNumber(NewTool)
	d.setToolOffsetNumber(NewTool)
	d.setSoftLimitsState( Axis.Y, True)
	e=1

if(NewTool>0 and NewTool<15 and e<1):																				#jezeli narzedzia sozkowe pobrac i koniec
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

