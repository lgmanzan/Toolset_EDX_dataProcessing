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
print dirAllFiles

conn = sqlite3.connect('moocDB.db')

c = conn.cursor()

csv.field_size_limit(sys.maxsize)

c.execute("DELETE from watchVideo")
conn.commit()

dirAllFiles = sys.argv[1]
for f in os.listdir(dirAllFiles):
	dir = dirAllFiles +"\\"+ f

	file = open(dir)
	reader = csv.DictReader(file)
		
	for row in reader:
		endName = dir.rindex('.csv')
		startName = dir.rindex('\\')		
		nameFile = dir[startName+1:endName]
		
		dir2 =  sys.argv[2]
		file2 = open(dir2)
		reader2 = csv.DictReader(file2)
		for row2 in reader2:
			
			if row2['idedX'] in nameFile:
				idVideo= row2['\xef\xbb\xbfidVideo']
				duration=int(row2['duration'])
		seenTimeAux = row['state']
		if '"0' in seenTimeAux:
			startTimeIdex = seenTimeAux.index('"0')
			min = seenTimeAux[startTimeIdex+4:startTimeIdex+6]
			ss = seenTimeAux[startTimeIdex+7:startTimeIdex+9]
			seenTimeAux2 = int(min)*60 + int(ss)
			seenTime = duration - (duration - seenTimeAux2)
			percentageSeen = (100*seenTime)/duration
		else:
			seenTime = 0
			percentageSeen = 0
		c.execute("INSERT INTO watchVideo VALUES ('"+row['username']+"','"+ idVideo+"',"+str(seenTime)+","+str(percentageSeen)+")")
		conn.commit()


conn.commit() 

conn.close()
