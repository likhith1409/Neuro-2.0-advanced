import psutil
import os
from Speak import Say


def systeminfo():
	import wmi
	c = wmi.WMI()  
	my_system_1 = c.Win32_LogicalDisk()[0]
	my_system_2 = c.Win32_ComputerSystem()[0]
	info = ["Total Disk Space: " + str(round(int(my_system_1.Size)/(1024**3),2)) + " GB",
			"Free Disk Space: " + str(round(int(my_system_1.Freespace)/(1024**3),2)) + " GB",
			"Manufacturer: " + my_system_2.Manufacturer,
			"Model: " + my_system_2. Model,
			"Owner: " + my_system_2.PrimaryOwnerName,
			"Number of Processors: " + str(my_system_2.NumberOfProcessors),
			"System Type: " + my_system_2.SystemType]
	print(info)

def batteryinfo():
	# usage = str(psutil.cpu_percent(interval=0.1))
	battery = psutil.sensors_battery()
	pr = str(battery.percent)
	if battery.power_plugged:
		return "Your System is currently on Charging Mode and it's " + pr + "% done."
	Say("Your System is currently on " + pr + "% battery life.")


print(batteryinfo())
