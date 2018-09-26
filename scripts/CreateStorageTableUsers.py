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

c.execute('''CREATE TABLE IF NOT EXISTS moocUsers
             (id integer primary key, username text, name text, email text, language text, location text, year_of_birth text, gender text, level_of_education text, enrollment_mode text, verification_status text, city text, country text)''')



c.execute("delete from moocUsers")
conn.commit()

csv.field_size_limit(sys.maxsize)

dir = sys.argv[1]

file = open(dir)
reader = csv.DictReader(file)
for row in reader:
	
	if row['location'] == '':
		location = "None" #not specified
	else:
		location = row['location']
	if row['city'] == '':
		city = "None" #not specified
	else:
		city = row['city']		
	if row['country'] == '':
		country = "None" #not specified
	else:
		country = row['country']	
	if row['country'] == '':
		country = "None" #not specified
	else:
		country = row['country']		
	if row['verification_status'] == '':
		verification_status = "None" #not specified
	else:
		verification_status = row['verification_status']
	if row['enrollment_mode'] == '':
		enrollment_mode = "None" #not specified
	else:
		enrollment_mode = row['enrollment_mode']
	if row['level_of_education'] == '':
		level_of_education = "None" #not specified
	else:
		level_of_education = row['level_of_education']		
	if row['gender'] == '':
		gender = "None" #not specified
	else:
		gender = row['gender']		
	if row['year_of_birth'] == '':
		year_of_birth = "None" #not specified
	else:
		year_of_birth = row['year_of_birth']			
	if row['language'] == '':
		language = "None" #not specified
	else:
		language = row['language']	
	if row['name'] == '':
		name = "None" #not specified
	else:
		name = row['name']	
	if row['email'] == '':
		email = "None" #not specified
	else:
		email = row['email']			

	c.execute("INSERT INTO moocUsers VALUES ("+row['\xef\xbb\xbfid']+",'"+row['username']+"','"+ name+"','"+email+"','"+language+"','"+location+"','"+year_of_birth+"','"+gender+"','"+level_of_education+"','"+enrollment_mode+"','"+verification_status+"','"+city+"','"+country+"')")
	conn.commit()

conn.commit() 
conn.close()



