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

def EXIT():
	window.destroy()
	sys.exit()



# - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  Main Window - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

f=d.getSpindleToolNumber( )
window = Tk()																																			
window.geometry("190x300+800+100")																												
window.title( "Funkcje Auto" )																													



# Buttons GoTo_Zero ------------------------------------------------------------------------------------------

T1 = Button(window, text='Nóż', font= ("Times New Roman",14), command = T1_Change, bg = "green" )		
T1.place(x=40, y=30, height=40, width=110)		

T2 = Button(window, text='Bigownik ', font= ("Times New Roman",14), command =T2_Change, bg = "green" )		
T2.place(x=40, y=80, height=40, width=110)	


EXIT = Button(window, text='WYJSCIE ', font= ("Times New Roman",14), command = EXIT, bg = "grey" )		
EXIT.place(x=40, y=180, height=40, width=110)	

t=d.getSpindleToolNumber( )
if(f==1):
	T1.configure(bg="red")
if(f==2):
	T2.configure(bg="red")

window.mainloop( )
#window.destroy()
sys.exit()

