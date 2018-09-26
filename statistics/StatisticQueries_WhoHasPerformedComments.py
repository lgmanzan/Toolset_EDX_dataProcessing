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
print "Who has performed more comments  -  country"
cursor0=c.execute("select distinct country from  moocUsers")
result0 = cursor0.fetchall()
amountProf=0
for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select username from  moocUsers where country='"+element[0]+"'")

	result = cursor1.fetchall()
	amountTotal = 0
	for ele in result:
		cursor2=c.execute("select amount from  comments where username='"+ele[0]+"'")
		result2 = cursor2.fetchall()
		for ele2 in result2:	
				amountTotal = amountTotal + ele2[0]
	if amountTotal >0:
		print element[0], amountTotal
print amountProf
print ' '
print "Who has performed more comments  -  gender"
cursor0=c.execute("select distinct gender from  moocUsers")
result0 = cursor0.fetchall()
amountProf=0
for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select username from  moocUsers where gender='"+element[0]+"'")

	result = cursor1.fetchall()
	amountTotal = 0
	for ele in result:
		cursor2=c.execute("select amount from  comments where username='"+ele[0]+"'")
		result2 = cursor2.fetchall()
		for ele2 in result2:
				amountTotal = amountTotal + ele2[0]
	if amountTotal >0:
		print element[0], amountTotal
print amountProf
print ' '

print "Who has performed more comments  -  year_of_birth"
cursor0=c.execute("select distinct year_of_birth from  moocUsers")
result0 = cursor0.fetchall()
amountProf=0
for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select username from  moocUsers where year_of_birth='"+element[0]+"'")

	result = cursor1.fetchall()
	amountTotal = 0
	for ele in result:
		cursor2=c.execute("select amount from  comments where username='"+ele[0]+"'")
		result2 = cursor2.fetchall()
		for ele2 in result2:	
				amountTotal = amountTotal + ele2[0]
	if amountTotal >0:
		print element[0], amountTotal
print amountProf
print ' '
	
print "Who has performed more comments  -  level_of_education"
cursor0=c.execute("select distinct level_of_education from  moocUsers")
result0 = cursor0.fetchall()
amountProf=0
for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select username from  moocUsers where level_of_education='"+element[0]+"'")

	result = cursor1.fetchall()
	amountTotal = 0
	for ele in result:
		cursor2=c.execute("select amount from  comments where username='"+ele[0]+"'")
		result2 = cursor2.fetchall()
		for ele2 in result2:	
				amountTotal = amountTotal + ele2[0]
	if amountTotal >0:
		print element[0], amountTotal
print amountProf
print ' '

conn.commit() 
conn.close()



