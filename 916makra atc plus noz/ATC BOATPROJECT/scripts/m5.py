import time
print("Stopping spindle")
d.setSpindleState(SpindleState.OFF)
time.sleep(3)
print("Spindle stopped")
