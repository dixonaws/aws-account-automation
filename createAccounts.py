#!/usr/bin/python

import csv


def main():
    accounts = {}
    with open('accountList.csv') as accountList:
        reader = csv.DictReader(accountList)
        for row in reader:
            print row

    accountList.close()

main()
