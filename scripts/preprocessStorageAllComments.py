#Authors: Lorena Gonzalez and J. Maria de Fuentes
#Organization: Universidad Carlos III de Madrid
#Code of the paper Design recommendations for online cybersecurity courses
#accepted in Computers and Security in 2018

import sqlite3
import csv
import os
import csv
import re
import math, string, sys, fileinput

csv.field_size_limit(sys.maxsize)

dirAllFiles = sys.argv[1]

conn = sqlite3.connect('moocDB.db')

c = conn.cursor()

csv.field_size_limit(sys.maxsize)

dir = sys.argv[1]

c.execute("delete from comments")
conn.commit()
		
file = open(dir)
reader = csv.reader(file)
headers = reader.next()

for row in reader:
	for a in range(0, len(headers)-1):
		if row[a+1]== "":
			amount = 0
		else:
			amount = row[a+1]
		c.execute("INSERT INTO comments VALUES ('"+row[0]+"','"+headers[(a+1)]+"',"+ str(amount)+")")
		conn.commit()

conn.commit() 
conn.close()
