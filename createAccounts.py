#!/usr/bin/python

import csv

def main():
    lstAccounts = []

    # read the CSV file into a list called accounts
    with open('accountList.csv') as filAccountList:
        reader = csv.DictReader(filAccountList)
        for row in reader:
            lstAccounts.append(row)

    filAccountList.close()

    # print all the accounts
    for account in lstAccounts:
        print account

    intNumberOfAccounts = len(lstAccounts)
    print "Read " + str(intNumberOfAccounts) + " accounts from the input file"

    # pop an account from the accounts list and print the email address of it
    randomAccount = lstAccounts.pop();
    print "Email address from account 0: " + randomAccount['emailAddress']

main()
