#okno funkcji auto
from tkinter import *

def T1_Change():
	d.executeGCode("M6 T1")
	window.destroy()
	sys.exit()
def T2_Change():
	d.executeGCode("M6 T2")
	window.destroy()
	sys.exit()
def T3_Change():
	d.executeGCode("M6 T3")
	window.destroy()
	sys.exit()
def T4_Change():
	d.executeGCode("M6 T4")
	window.destroy()
	sys.exit()
def T5_Change():
	d.executeGCode("M6 T5")
	window.destroy()
	sys.exit()
def T6_Change():
	d.executeGCode("M6 T6")
	window.destroy()
	sys.exit()
def T7_Change():
	d.executeGCode("M6 T7")
	window.destroy()
	sys.exit()
def T8_Change():
	d.executeGCode("M6 T8")
	window.destroy()
	sys.exit()
def T9_Change():
	d.executeGCode("M6 T9")
	window.destroy()
	sys.exit()
def T10_Change():
	d.executeGCode("M6 T10")
	window.destroy()
	sys.exit()
def T11_Change():
	d.executeGCode("M6 T11")
	window.destroy()
	sys.exit()
def T12_Change():
	d.executeGCode("M6 T12")
	window.destroy()
	sys.exit()
def T13_Change():
	d.executeGCode("M6 T13")
	window.destroy()
	sys.exit()
def T14_Change():
	d.executeGCode("M6 T14")
	window.destroy()
	sys.exit()
def T15_Change():
	d.executeGCode("M6 T15")
	window.destroy()
	sys.exit()
def T16_Change():
	d.executeGCode("M6 T16")
	window.destroy()
	sys.exit()


def EXIT():
	window.destroy()
	sys.exit()



# - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  Main Window - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

f=d.getSpindleToolNumber( )
window = Tk()																																			
window.geometry("350x600+800+100")																												
window.title( "Zmiana Narzedzia" )																													



# Buttons GoTo_Zero ------------------------------------------------------------------------------------------

T1 = Button(window, text='Narzedzie T1', font= ("Times New Roman",14), command = T1_Change, bg = "green" )		
T1.place(x=40, y=30, height=40, width=115)		

T2 = Button(window, text='Narzedzie T2 ', font= ("Times New Roman",14), command =T2_Change, bg = "green" )		
T2.place(x=40, y=80, height=40, width=115)	

T3 = Button(window, text='Narzedzie T3', font= ("Times New Roman",14), command = T3_Change, bg = "green" )		
T3.place(x=40, y=130, height=40, width=115)		

T4 = Button(window, text='Narzedzie T4', font= ("Times New Roman",14), command = T4_Change, bg = "green" )		
T4.place(x=40, y=180, height=40, width=115)	

T5 = Button(window, text='Narzedzie T5', font= ("Times New Roman",14), command = T5_Change, bg = "green" )		
T5.place(x=40, y=230, height=40, width=115)		

T6 = Button(window, text='Narzedzie T6 ', font= ("Times New Roman",14), command = T6_Change, bg = "green" )		
T6.place(x=40, y=280, height=40, width=115)	

T7 = Button(window, text='Narzedzie T7', font= ("Times New Roman",14), command = T7_Change, bg = "green" )		
T7.place(x=40, y=330, height=40, width=115)	

T8 = Button(window, text='Narzedzie T8', font= ("Times New Roman",14), command = T8_Change, bg = "green" )		
T8.place(x=40, y=380, height=40, width=115)	

T9 = Button(window, text='Narzedzie T9', font= ("Times New Roman",14), command = T9_Change, bg = "green" )		
T9.place(x=40, y=430, height=40, width=115)	

T10 = Button(window, text='Narzedzie T10', font= ("Times New Roman",14), command = T10_Change, bg = "green" )		
T10.place(x=40, y=480, height=40, width=115)	

T11 = Button(window, text='Narzedzie T11', font= ("Times New Roman",14), command = T11_Change, bg = "green" )		
T11.place(x=160, y=30, height=40, width=115)		

T12 = Button(window, text='Narzedzie T12 ', font= ("Times New Roman",14), command =T12_Change, bg = "green" )		
T12.place(x=160, y=80, height=40, width=115)	

T13 = Button(window, text='Narzedzie T13', font= ("Times New Roman",14), command = T13_Change, bg = "green" )		
T13.place(x=160, y=130, height=40, width=115)		

T14 = Button(window, text='Narzedzie T14', font= ("Times New Roman",14), command = T14_Change, bg = "green" )		
T14.place(x=160, y=180, height=40, width=115)	

T15 = Button(window, text='Narzedzie T15', font= ("Times New Roman",14), command = T15_Change, bg = "green" )		
T15.place(x=160, y=230, height=40, width=115)		

T16 = Button(window, text='NOZ', font= ("Times New Roman",14), command = T16_Change, bg = "orange" )		
T16.place(x=160, y=280, height=40, width=115)	




EXIT = Button(window, text='WYJSCIE ', font= ("Times New Roman",14), command = EXIT, bg = "grey" )		
EXIT.place(x=40, y=550, height=40, width=270)	

t=d.getSpindleToolNumber( )
if(f==1):
	T1.configure(bg="red")
if(f==2):
	T2.configure(bg="red")
if(f==3):
	T3.configure(bg="red")
if(f==4):
	T4.configure(bg="red")
if(f==5):
	T5.configure(bg="red")
if(f==6):
	T6.configure(bg="red")
if(f==7):
	T7.configure(bg="red")
if(f==8):
	T8.configure(bg="red")
if(f==9):
	T9.configure(bg="red")
if(f==10):
	T10.configure(bg="red")
if(f==11):
	T11.configure(bg="red")
if(f==12):
	T12.configure(bg="red")
if(f==13):
	T13.configure(bg="red")
if(f==14):
	T14.configure(bg="red")
if(f==15):
	T15.configure(bg="red")
if(f==16):
	T16.configure(bg="red")
if(f==17):
	T17.configure(bg="red")

window.mainloop( )
#window.destroy()
sys.exit()

