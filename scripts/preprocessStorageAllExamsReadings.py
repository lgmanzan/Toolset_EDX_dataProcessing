#Authors: Lorena Gonzalez and J. Maria de Fuentes
#Organization: Universidad Carlos III de Madrid
#Code of the paper Design recommendations for online cybersecurity courses
#accepted in Computers and Security in 2018

import csv
import os
import csv
import sys


import sqlite3

conn = sqlite3.connect('moocDB.db')

c = conn.cursor()

csv.field_size_limit(sys.maxsize)

dir = sys.argv[1]
numLectures_exams = int(sys.argv[2]) 
numLectures_readings = int(sys.argv[3]) 

file = open(dir)
reader = csv.DictReader(file)	

c.execute("delete from marks")
conn.commit()
for row in reader:
	mark=0
	for index in range(1,numLectures_exams):
		idElement = "ExamL"+str(index)
		cursor0=c.execute("select lecture from examReading where idExamReading='"+idElement+"'")
		result0 = cursor0.fetchall()
		conn.commit()
		for element in result0:
			lectureInd = element[0]	

		if row[idElement]== "Not Attempted":
			mark=0
		else:
			mark = row[idElement]
			
		c.execute("INSERT INTO marks VALUES ('"+row['username']+"',"+str(lectureInd)+",'"+str(idElement)+"',0,1,"+str(mark)+")")

		conn.commit()
	
	if row['FinalExam']== "Not Attempted":
		mark=0
	else:
		mark = row['FinalExam']	
	c.execute("INSERT INTO marks VALUES ('"+row['username']+"',"+str(10)+",'FinalExam',0,1,"+str(mark)+")")
	conn.commit()		
	for index2 in range(1,numLectures_readings):
		idElement = "Reading"+str(index2)
		
		cursor0=c.execute("select lecture from examReading where idExamReading='"+idElement+"'")
		result0 = cursor0.fetchall()
		conn.commit()
		for element in result0:
			lectureIndex = element[0]	

		if row[idElement]== "Not Attempted":
			mark=0
		else:
			mark = row[idElement]			
		
		c.execute("INSERT INTO marks VALUES ('"+row['username']+"',"+str(lectureIndex)+",'"+str(idElement)+"',1,0,"+str(mark)+")")
		conn.commit()		


conn.close()

