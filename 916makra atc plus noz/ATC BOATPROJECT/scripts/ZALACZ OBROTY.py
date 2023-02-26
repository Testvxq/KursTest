if(d.getSpindleState( )==SpindleState.CW_ON):
	d.executeGCode( "M05" )
else:
	d.executeGCode( "M03" )
