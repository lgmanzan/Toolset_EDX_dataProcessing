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


print 'all users from COUNTRY'

cursor0=c.execute("select distinct country from  moocUsers")
result0 = cursor0.fetchall()

for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select count(*) from  moocUsers where country='"+element[0]+"'")

	result = cursor1.fetchall()
	for ele in result:
		print element[0], ele[0]
		
print 'all users from GENDER'	


cursor0=c.execute("select distinct gender from  moocUsers")
result0 = cursor0.fetchall()

for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select count(*) from  moocUsers where gender='"+element[0]+"'")
	result = cursor1.fetchall()
	for ele in result:
		print element[0], ele[0]
		
		
print 'all users from level_of_education'	
cursor0=c.execute("select distinct level_of_education from  moocUsers")
result0 = cursor0.fetchall()

for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select count(*) from  moocUsers where level_of_education='"+element[0]+"'")
	result = cursor1.fetchall()
	for ele in result:
		print element[0], ele[0]		
		
print 'all users from year_of_birth'	
cursor0=c.execute("select distinct year_of_birth from  moocUsers")
result0 = cursor0.fetchall()

for element in result0:
	#element[0] is the only possibility because no more positions exist because the previous 
	#query as just for an element per row (a column)
	cursor1=c.execute("select count(*) from  moocUsers where year_of_birth='"+element[0]+"'")

	result = cursor1.fetchall()
	for ele in result:
		print element[0], ele[0]				



conn.commit() 
conn.close()



