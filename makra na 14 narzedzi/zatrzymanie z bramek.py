if(d.getState( )==State.Trajectory):
	d.finishTrajectory( )
	d.setSpindleState(SpindleState.OFF)
	msg.wrn("Przekroczono bramki bezpieczenstwa!'", "Warning!")
	sys.exit("Przekroczono bramki bezpieczenstwa!")