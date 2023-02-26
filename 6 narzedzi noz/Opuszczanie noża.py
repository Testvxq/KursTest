mod_IP = d.getModule( ModuleType.IP, 0 )
cutter = 3
if mod_IP.getDigitalIO( IOPortDir.OutputPort, cutter ) == DIOPinVal.PinReset:
	mod_IP.setDigitalIO( cutter, DIOPinVal.PinSet )
else:
	mod_IP.setDigitalIO( cutter, DIOPinVal.PinReset )