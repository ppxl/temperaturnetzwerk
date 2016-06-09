#!/usr/bin/env python
from subprocess import check_output
import datetime
from time import strftime,gmtime
import sqlite3
import os

dbConnection = None
dbCursor = None
DELIMITER = ";"


def main():
	openDb()
	dbResult = readFromDb()
	
	with open("datefile.txt","w") as outputFile:
		for row in dbResult:
			writeDataSet(row, outputFile)
	
	closeDb()

def readFromDb():
	#dbCursor.execute("delete from temperatur")
	result = dbCursor.execute("select * from temperatur")
	#dbConnection.commit()
	return result

def writeDataSet(row, outputFile):
		outputFile.write(row[0])
		outputFile.write(DELIMITER)
		outputFile.write(str(row[1]) + "\n")

def openDb():
	global dbConnection
	global dbCursor
	dbConnection= sqlite3.connect('temperatur.db')
	dbCursor = dbConnection.cursor()
	
def closeDb():
	global dbConnection
	dbConnection.close()

if __name__ == '__main__':
	main()
