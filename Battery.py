# Import module
print("Importing module...")
import psutil
import time
from win10toast import ToastNotifier
print("Finished importing module.")

# New line
print("")

# Console output
print("@#####################################################@")
print("@                                                     @")
print("@ Battery percentage, battery left and power plugged. @")
print("@                                                     @")
print("@#####################################################@")

# New line
print("")

# Current version
print("Current version 1")

# New line
print("")

# Notice
print("The battery left and battery percentage may bugged sometimes. Try reopen it.")
print("Battery left will be named as 'BatteryTime.POWER_TIME_UNLIMITED' if charging.")
print("Battery left will be in seconds and updated after the battery percentage changes")

# New line
dprint("")

# Variable
rmax = 74
rmin = 41
sleeplevel = 10
battery = psutil.sensors_battery()
Check = True
toast = ToastNotifier()
sleep = False
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

# Script settings
print("Max battery percentage :", rmax)
print("Min battery percentage :", rmin)

# New line
print("")

# Checks
while Check == True:
    battery = psutil.sensors_battery()
    print("Battery percentage :", battery.percent, "%")
    battery = psutil.sensors_battery()
    print("Power plugged in :", battery.power_plugged)
    battery = psutil.sensors_battery()
    if battery.power_plugged == False:
        print("Battery left :", convertTime(battery.secsleft))
        battery = psutil.sensors_battery()
    if battery.power_plugged == True:
        print("Battery left :", battery.secsleft)
        battery = psutil.sensors_battery()    
    if battery.percent == rmax:
        battery = psutil.sensors_battery()
        if battery.power_plugged == True:
            battery = psutil.sensors_battery()
            print("Please unplug your charger")
            toast.show_toast("Battery v1", "Please unplug your charger.")
    if battery.percent > rmax:
        battery = psutil.sensors_battery()
        if battery.power_plugged == True:
            battery = psutil.sensors_battery()
            print("Please unplug your charger")
            toast.show_toast("Battery v1", "Please unplug your charger.")
    if battery.percent < rmin:
        battery = psutil.sensors_battery()
        if battery.power_plugged == False:
            battery = psutil.sensors_battery()
            print("Please plug in your charger")
            toast.show_toast("Battery v1", "Please charge.")
    if battery.percent == rmin:
        battery = psutil.sensors_battery()
        if battery.power_plugged == False:
            battery = psutil.sensors_battery()
            print("Please plug in your charger")
            toast.show_toast("Battery v1", "Please charge.", duration = 1)
    print("")
    time.sleep(1)
