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

c.execute('''CREATE TABLE IF NOT EXISTS examReading
             (idExamReading text primary key, lecture integer, isReading integer, isExam integer)''')
			 
c.execute('''CREATE TABLE IF NOT EXISTS marks
             (username text , lecture integer, idExamReading text, isReading integer, isExam integer, mark real, primary key (username,idExamReading))''')

c.execute('''CREATE TABLE IF NOT EXISTS watchVideo
             (username text , idVideo text, seenTimeSc integer, percentageSeen real, primary key (username,idVideo))''')
			 

c.execute('''CREATE TABLE IF NOT EXISTS video
             (idVideo text primary key, lecture integer, length integer)''') 

			 
c.execute('''CREATE TABLE IF NOT EXISTS comments
             (username text , idElement text, amount integer, primary key (username,idElement))''')				 


conn.commit() 

conn.close()



