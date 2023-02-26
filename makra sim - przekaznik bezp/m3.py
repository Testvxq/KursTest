InGateOpen="15" #wejscie bramek

mod_IP = d.getModule( ModuleType.IP, 0 )
def IsGateOpen():
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InGateOpen) == DIOPinVal.PinReset :
		IsGateOpen=1
	if mod_IP.getDigitalIO( IOPortDir.InputPort, InGateOpen) == DIOPinVal.PinSet :
		IsGateOpen=0
	return IsGateOpen
if(IsGateOpen()):
	msg.wrn("Przerwany sygnal bramek bezpieczenstwa", "Warning!")
	sys.exit("Przerwany sygnal bramek bezpieczenstwa!")
print("spindle on CW")
d.setSpindleState( SpindleState.CW_ON )
print("spindle ready")

