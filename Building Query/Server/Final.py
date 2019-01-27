import sqlite3
conFinal = sqlite3.connect("final.db")
conDB1 = sqlite3.connect("test1.db")
conDB2 = sqlite3.connect("test2.db")
conDBL = sqlite3.connect("Location0.db")
conFinal.text_factory = str
conDB1.text_factory = str
conDB2.text_factory = str
conDBL.text_factory = str
cf = conFinal.cursor()
c1 = conDB1.cursor()
c2 = conDB2.cursor()
cL = conDBL.cursor()

#if final is deleted make a new one if not just use final
cf.execute('''CREATE TABLE IF NOT EXISTS devices (device_name text, mac_address text UNIQUE, owner_name text, present integer, location integer);''')
conFinal.commit()

cf.execute('''UPDATE devices SET present=0 WHERE present=1;''')

c1.execute('''SELECT * FROM devices''') 
for row in c1:
	if row[3] == 1:
		cf.execute('''INSERT OR REPLACE INTO devices (device_name,mac_address,owner_name,present,location) VALUES (?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4]))		

c2.execute('''SELECT * FROM devices''') 
for row in c2:
	if row[3] == 1:
		cf.execute('''INSERT OR REPLACE INTO devices (device_name,mac_address,owner_name,present,location) VALUES (?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4]))	
conFinal.commit()

cL.execute('''SELECT * FROM devices''') 
for row in cL:
	if row[3] == 1:
		cf.execute('''INSERT OR REPLACE INTO devices (device_name,mac_address,owner_name,present,location) VALUES (?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4]))	
conFinal.commit()

conFinal.close()
conDB1.close()
conDB2.close()
conDBL.close()
