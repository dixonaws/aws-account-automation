#!/usr/bin/python

def main():
	accountList=open("accountList.csv", "r")
	
	for account in accountList:
		print accountList.readline()


main()


