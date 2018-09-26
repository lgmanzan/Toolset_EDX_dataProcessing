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
print 'country'
for lectureIndex in range(1,7):
	for questionTypeIndex in range(1,3):
		if questionTypeIndex == 1:
			type= "isExam"
		else:
			type = "isReading"
		print "Who has answered better in Lecture", lectureIndex, " and type", type, " --- country"
		print 'Country', 'Avg. of those who have done it'
		cursor0=c.execute("select distinct country from  moocUsers")
		result0 = cursor0.fetchall()
		
		cursor01=c.execute("select idExamReading from examReading where lecture="+str(lectureIndex)+" and "+type+"=1")
		result01 = cursor01.fetchall()

		for element in result0:
			cursor1=c.execute("select username from  moocUsers where country='"+element[0]+"'")

			result = cursor1.fetchall()
			mark= 0
			amountTotal = 0
			for ele in result:
				for ele1 in result01:				
					cursor2=c.execute("select mark from marks where username='"+ele[0]+"' and idExamReading='"+ele1[0]+"'")
					result2 = cursor2.fetchall()
					for ele2 in result2:
						if ele2[0] != 0: 
							mark = mark + float(ele2[0])
							amountTotal = amountTotal +1
			if amountTotal==0:
				amountTotal=1
			if mark > 0:
				print element[0], str(mark/amountTotal)
				
				
				
print 'country but avg all lectures'

for questionTypeIndex in range(1,3):
	if questionTypeIndex == 1:
		type= "isExam"
	else:
		type = "isReading"
	print "Who has answered better avg all Lectures and type", type, " --- country"
	print 'Country', 'Avg. of those who have done it'
	cursor0=c.execute("select distinct country from  moocUsers")
	result0 = cursor0.fetchall()
	
		
	for element in result0:
		cursor1=c.execute("select username from  moocUsers where country='"+element[0]+"'")

		result = cursor1.fetchall()
		mark= 0
		amountTotal = 0
		for lectureIndex in range(1,7):
			cursor01=c.execute("select idExamReading from examReading where lecture="+str(lectureIndex)+" and "+type+"=1")
			result01 = cursor01.fetchall()
			for ele in result:
				for ele1 in result01:				
					cursor2=c.execute("select mark from marks where username='"+ele[0]+"' and idExamReading='"+ele1[0]+"'")
					result2 = cursor2.fetchall()
					for ele2 in result2:
						if ele2[0] != 0: 
							mark = mark + float(ele2[0])
							amountTotal = amountTotal +1
			if amountTotal==0:
				amountTotal=1
		if mark > 0:
			print element[0], str(mark/amountTotal)
				
			
print 'gender'
for lectureIndex in range(1,7):
	for questionTypeIndex in range(1,3):
		if questionTypeIndex == 1:
			type= "isExam"
		else:
			type = "isReading"
		print "Who has answered better in Lecture", lectureIndex, " and type", type, " --- gender"
		print 'gender', 'Avg. of those who have done it'
		cursor0=c.execute("select distinct gender from  moocUsers")
		result0 = cursor0.fetchall()
		
		cursor01=c.execute("select idExamReading from examReading where lecture="+str(lectureIndex)+" and "+type+"=1")
		result01 = cursor01.fetchall()

		for element in result0:
			cursor1=c.execute("select username from  moocUsers where gender='"+element[0]+"'")

			result = cursor1.fetchall()
			mark= 0
			amountTotal = 0
			for ele in result:
				for ele1 in result01:				
					cursor2=c.execute("select mark from marks where username='"+ele[0]+"' and idExamReading='"+ele1[0]+"'")
					result2 = cursor2.fetchall()
					for ele2 in result2:
						if ele2[0] != 0: 
							mark = mark + float(ele2[0])
							amountTotal = amountTotal +1
			if amountTotal==0:
				amountTotal=1
			if mark > 0:
				print element[0], str(mark/amountTotal)

print 'year_of_birth'
for lectureIndex in range(1,7):
	for questionTypeIndex in range(1,3):
		if questionTypeIndex == 1:
			type= "isExam"
		else:
			type = "isReading"
		print "Who has answered better in Lecture", lectureIndex, " and type", type, " --- year_of_birth"
		print 'year_of_birth', 'Avg. of those who have done it'
		cursor0=c.execute("select distinct year_of_birth from  moocUsers")
		result0 = cursor0.fetchall()
		
		cursor01=c.execute("select idExamReading from examReading where lecture="+str(lectureIndex)+" and "+type+"=1")
		result01 = cursor01.fetchall()

		for element in result0:
			cursor1=c.execute("select username from  moocUsers where year_of_birth='"+element[0]+"'")

			result = cursor1.fetchall()
			mark= 0
			amountTotal = 0
			for ele in result:
				for ele1 in result01:				
					cursor2=c.execute("select mark from marks where username='"+ele[0]+"' and idExamReading='"+ele1[0]+"'")
					result2 = cursor2.fetchall()
					for ele2 in result2:
						if ele2[0] != 0: 
							mark = mark + float(ele2[0])
							amountTotal = amountTotal +1
			if amountTotal==0:
				amountTotal=1
			if mark > 0:
				print element[0], str(mark/amountTotal)
		
print 'level_of_education'
for lectureIndex in range(1,7):
	for questionTypeIndex in range(1,3):
		if questionTypeIndex == 1:
			type= "isExam"
		else:
			type = "isReading"
		print "Who has answered better in Lecture", lectureIndex, " and type", type, " --- level_of_education"
		print 'level_of_education', 'Avg. of those who have done it'
		cursor0=c.execute("select distinct level_of_education from  moocUsers")
		result0 = cursor0.fetchall()
		
		cursor01=c.execute("select idExamReading from examReading where lecture="+str(lectureIndex)+" and "+type+"=1")
		result01 = cursor01.fetchall()

		for element in result0:
			cursor1=c.execute("select username from  moocUsers where level_of_education='"+element[0]+"'")

			result = cursor1.fetchall()
			mark= 0
			amountTotal = 0
			for ele in result:
				for ele1 in result01:				
					cursor2=c.execute("select mark from marks where username='"+ele[0]+"' and idExamReading='"+ele1[0]+"'")
					result2 = cursor2.fetchall()
					for ele2 in result2:
						if ele2[0] != 0: 
							mark = mark + float(ele2[0])
							amountTotal = amountTotal +1
			if amountTotal==0:
				amountTotal=1
			if mark > 0:
				print element[0], str(mark/amountTotal)
		



conn.commit() 
conn.close()



