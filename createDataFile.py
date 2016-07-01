#!/usr/bin/env python
from subprocess import check_output
import datetime
from time import strftime,gmtime
import sqlite3
import os

dbConnection = None
dbCursor = None
DELIMITER = ";"
rollingAverage = None

def main():
	openDb()
	
	generateDataForAll()
	generateDataForMonth()
	generateDataForWeek()
	generateDataForLast24Hours()
	
	closeDb()

def generateDataForAll():
	dbResult = readAllFromDb()
	writeDateFile("datefile.txt", dbResult)

def generateDataForMonth():
	dbResult = readMonthDataFromDb()
	writeDateFile("datefileMonth.txt",dbResult)

def generateDataForWeek():
	dbResult = readWeekDataFromDb()
	writeDateFile("datefileWeek.txt", dbResult)

def generateDataForLast24Hours():
	dbResult = readLast24HoursDataFromDb()
	writeDateFile("datefileDay.txt", dbResult)

def writeDateFile(dateFileName, dbResult):
	with open(dateFileName,"w") as outputFile:
		for row in dbResult:
			writeDataSet(row, outputFile)

def readAllFromDb():
	return dbCursor.execute("select t.datum,t.temp from temperatur t")

def readMonthDataFromDb():
	return dbCursor.execute("SELECT t.datum,t.temp FROM `temperatur` t \
	where t.datum >= date('now', '-1 months') \
	ORDER BY t.datum ASC")

def readWeekDataFromDb():
	return dbCursor.execute("SELECT t.datum,t.temp FROM `temperatur` t \
	where t.datum >= date('now', '-7 days') \
	ORDER BY t.datum ASC")

def readLast24HoursDataFromDb():
	return dbCursor.execute("SELECT t.datum,t.temp FROM `temperatur` t \
	where t.datum >= date('now', '-1 days') \
	ORDER BY t.datum ASC")

def writeDataSet(row, outputFile):
		outputFile.write('"' + row[0] +'"')
		outputFile.write(DELIMITER)
		outputFile.write(str(row[1]))
		outputFile.write("\n")

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
