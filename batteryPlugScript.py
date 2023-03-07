# Radded's quick little battery checker / thing to make sure I don't explode my Surface battery more than it already is

import psutil
from time import sleep
from KasaSwitch import KasaSwitch

# CONSTANTS
max_percent = 80
min_percent = 20
plug = None
def whenBatteryMax():
	global plug
	plug.set_state(False)
def whenBatteryMin():
	global plug
	plug.set_state(True)

def getState():
	batt = psutil.sensors_battery()
	return (batt.percent, batt.power_plugged)

def discover_plug():
	global plug
	plug = KasaSwitch("10.0.0.127")

def main():
	discover_plug()
	print("Radded's battery thing")
	global max_percent
	global min_percent

	while True:
		print("Getting battery state...")
		state = getState()
		print("The battery is at {percent}% and {charging}".format(percent=state[0], charging=("charging" if state[1] else "not charging")))
		if (state[0] >= max_percent and state[1]):
			print("Stop charging!")
			whenBatteryMax()
		elif (state[0] <= min_percent and not state[1]):
			print("Start charging!")
			whenBatteryMin()
		print("Going to sleep...")
		sleep(30)

if __name__ == "__main__":
	main()