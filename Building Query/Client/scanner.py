#importing
from bluetool import Bluetooth
import sqlite3
import time

#Create Table if none exists
conn = sqlite3.connect('devices.db')
conn.text_factory = str
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS devices (device_name text, mac_address text UNIQUE, owner_name text, present integer, location text);''')
conn.commit()

#variables
bluetooth=Bluetooth()
devices = {}
mac_address=[]		
actualName = "Unknown"
seconds = 10
present = 1
location = 0
#redefines %devices% and redefines macaddress_list
def scan():
	print "scanning"
	bluetooth.scan()
	devices = bluetooth.get_available_devices()	
	mac_addresses = []
	for x in devices:
		print x		
	print "scan complete"
	return devices

#removes all presence
def presence():
	c.execute('''UPDATE devices SET present=0 WHERE present=1;''')

#populate changes
def add_unique(devices):
	print "enter add unique"
	print devices
	for x in devices:
		name = x['name']
		mac_address = x['mac_address']	
		c.execute('''REPLACE INTO devices (device_name,mac_address,owner_name,present,location) VALUES (?, ?, ?, ?, ?)''', (name, mac_address, actualName, present, location))	
	conn.commit()	




#main
presence()
add_unique(scan())
print "Closing"
conn.close()

