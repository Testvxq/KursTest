if(d.getSelectedToolNumber( )==d.getSpindleToolNumber( )):
	print ("aktualne narzedzie = wybrane narzedzie ")
else:
	print ("za³aduj narzedzie: ",d.getSelectedToolNumber( ))
	msg.info("zaladuj narzedzie: {:.0f}".format(d.getSelectedToolNumber()),('zmiana narzedzia'))
	d.stopTrajectory()
	d.setGCodeNextLine()
	d.setSpindleToolNumber( d.getSelectedToolNumber( ) )
	