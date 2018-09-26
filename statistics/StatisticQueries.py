#Authors: Lorena Gonzalez and J. Maria de Fuentes
#Organization: Universidad Carlos III de Madrid
#Code of the paper Design recommendations for online cybersecurity courses
#accepted in Computers and Security in 2018

import sqlite3
import csv
import os
import csv
import sys

conn = sqlite3.connect('moocDB.db')

c = conn.cursor()
	
cursor0=c.execute("select amount from  comments")
result0 = cursor0.fetchall()
conn.commit()
num=0
for ele in result0:
	num = num + ele[0]
	
print 'num total comments', num


cursor0=c.execute("select count(*) from  video")
result0 = cursor0.fetchall()
conn.commit()
for ele in result0:
	print 'num total videos', ele[0]
	
cursor0=c.execute("select username from  moocUsers")
result0 = cursor0.fetchall()
conn.commit()
sum=0
for ele in result0:
	sum = sum +1
print 'num total users', sum
	
print 'Avg. num users who have watched videos per lecture'
for lectureIndex in range(1,7):
	cursor0=c.execute("select idVideo from video where lecture="+str(lectureIndex))
	result0 = cursor0.fetchall()
	amountTotal = 0
	totalVideosLecture=0
	for element in result0:
		cursor2=c.execute("select percentageSeen from watchVideo where idVideo='"+element[0]+"'")
		result2 = cursor2.fetchall()
		totalVideosLecture=totalVideosLecture+1
		for ele2 in result2:
			if ele2[0] is not None:
				amountTotal = amountTotal + 1
	print 'lecture',str(lectureIndex), amountTotal/totalVideosLecture,totalVideosLecture

	
print 'Num users who have done EXAMS per lecture'	
for lectureIndex in range(1,7):
	cursor0=c.execute("select mark from marks where lecture="+str(lectureIndex)+" and isExam=1")
	result0 = cursor0.fetchall()
	amountTotal = 0
	for element in result0:
		if element[0] >0:
			amountTotal = amountTotal +1
	print 'lecture',str(lectureIndex), amountTotal	

		
cursor0=c.execute("select mark from marks where lecture='10'")
result0 = cursor0.fetchall()
amountTotal = 0
for element in result0:
	if element[0] >0:
		amountTotal = amountTotal +1
print 'num users who have done FINALEXAM',amountTotal			

