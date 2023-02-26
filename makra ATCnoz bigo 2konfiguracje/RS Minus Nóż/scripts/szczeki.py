mod_IP = d.getModule( ModuleType.IP, 0 )

if mod_IP.getDigitalIO( IOPortDir.OutputPort, 2) == DIOPinVal.PinReset :
	if msg.askYesNo( 'Otworzyc szceki?', 'zapytanie' ):
		mod_IP.setDigitalIO(2, DIOPinVal.PinSet)
else:
	mod_IP.setDigitalIO(2, DIOPinVal.PinReset)
