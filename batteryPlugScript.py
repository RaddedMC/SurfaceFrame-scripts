# Radded's quick little battery checker / thing to make sure I don't explode my Surface battery more than it already is

import psutil
from time import sleep

# CONSTANTS
max_percent = 80
min_percent = 20
def whenBatteryMax():
	pass
def whenBatteryMin():
	pass

def getState():
	batt = psutil.sensors_battery()
	return (batt.percent, batt.power_plugged)

def main():
	# Do this first to align with program state
	print("Radded's battery thing")
	whenBatteryMin()
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