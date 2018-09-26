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
	print "Who has watched more videos Lecture", lectureIndex, " and the average percentage watchVideos--- country"
	cursor0=c.execute("select distinct country from  moocUsers")
	result0 = cursor0.fetchall()

	cursor1=c.execute("select idVideo from video where lecture="+str(lectureIndex))
	result1 = cursor1.fetchall()

	for element in result0:
		#element[0] is the only possibility because no more positions exist because the previous 
		#query as just for an element per row (a column)
		cursor1=c.execute("select username from  moocUsers where country='"+element[0]+"'")

		result = cursor1.fetchall()
		amountTotal = 0
		percentageSeen = 0
		for ele in result:
			for ele1 in result1:
				cursor2=c.execute("select percentageSeen from watchVideo where username='"+ele[0]+"' and idVideo='"+ele1[0]+"'")
				result2 = cursor2.fetchall()
				for ele2 in result2:
					if ele2[0] is not None:
						amountTotal = amountTotal + 1
						percentageSeen = percentageSeen + int(ele2[0])
		if amountTotal >0:
			print element[0], str(percentageSeen/amountTotal)
			
			
print 'gender'
for lectureIndex in range(1,7):
	print "Who has watched more videos Lecture", lectureIndex, " and the average percentage watchVideos--- gender"
	cursor0=c.execute("select distinct gender from  moocUsers")
	result0 = cursor0.fetchall()

	cursor1=c.execute("select idVideo from video where lecture="+str(lectureIndex))
	result1 = cursor1.fetchall()

	for element in result0:
		#element[0] is the only possibility because no more positions exist because the previous 
		#query as just for an element per row (a column)
		cursor1=c.execute("select username from  moocUsers where gender='"+element[0]+"'")

		result = cursor1.fetchall()
		amountTotal = 0
		percentageSeen = 0
		for ele in result:
			for ele1 in result1:
				cursor2=c.execute("select percentageSeen from watchVideo where username='"+ele[0]+"' and idVideo='"+ele1[0]+"'")
				result2 = cursor2.fetchall()
				for ele2 in result2:
					if ele2[0] is not None:
						amountTotal = amountTotal + 1
						percentageSeen = percentageSeen + int(ele2[0])
		if amountTotal >0:
			print element[0], str(percentageSeen/amountTotal)
					
print 'level_of_education'
for lectureIndex in range(1,7):
	print "Who has watched more videos Lecture", lectureIndex, " and the average percentage watchVideos--- level_of_education"
	cursor0=c.execute("select distinct level_of_education from  moocUsers")
	result0 = cursor0.fetchall()

	cursor1=c.execute("select idVideo from video where lecture="+str(lectureIndex))
	result1 = cursor1.fetchall()

	for element in result0:
		#element[0] is the only possibility because no more positions exist because the previous 
		#query as just for an element per row (a column)
		cursor1=c.execute("select username from  moocUsers where level_of_education='"+element[0]+"'")

		result = cursor1.fetchall()
		amountTotal = 0
		percentageSeen = 0
		for ele in result:
			for ele1 in result1:
				cursor2=c.execute("select percentageSeen from watchVideo where username='"+ele[0]+"' and idVideo='"+ele1[0]+"'")
				result2 = cursor2.fetchall()
				for ele2 in result2:
					if ele2[0] is not None:
						amountTotal = amountTotal + 1
						percentageSeen = percentageSeen + int(ele2[0])
		if amountTotal >0:
			print element[0], str(percentageSeen/amountTotal)

print 'year_of_birth'
for lectureIndex in range(1,7):
	print "Who has watched more videos Lecture", lectureIndex, " and the average percentage watchVideos--- year_of_birth"
	cursor0=c.execute("select distinct year_of_birth from  moocUsers")
	result0 = cursor0.fetchall()

	cursor1=c.execute("select idVideo from video where lecture="+str(lectureIndex))
	result1 = cursor1.fetchall()

	for element in result0:
		#element[0] is the only possibility because no more positions exist because the previous 
		#query as just for an element per row (a column)
		cursor1=c.execute("select username from  moocUsers where year_of_birth='"+element[0]+"'")

		result = cursor1.fetchall()
		amountTotal = 0
		percentageSeen = 0
		for ele in result:
			for ele1 in result1:
				cursor2=c.execute("select percentageSeen from watchVideo where username='"+ele[0]+"' and idVideo='"+ele1[0]+"'")
				result2 = cursor2.fetchall()
				for ele2 in result2:
					if ele2[0] is not None:
						amountTotal = amountTotal + 1
						percentageSeen = percentageSeen + int(ele2[0])
		if amountTotal >0:
			print element[0], str(percentageSeen/amountTotal)
			
conn.commit() 
conn.close()



