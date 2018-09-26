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

dir = sys.argv[1] 

conn = sqlite3.connect('moocDB.db')

c = conn.cursor()



csv.field_size_limit(sys.maxsize)



file = open(dir)
reader = csv.DictReader(file)

for row in reader:
	c.execute("INSERT INTO examReading VALUES ('"+row['\xef\xbb\xbfidExamReading']+"',"+ row['lecture']+","+row['isReading']+","+row['isExam']+")")
	conn.commit()



conn.commit() 

conn.close()
