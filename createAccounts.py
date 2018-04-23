#!/usr/bin/python

import csv


def main():
    accounts = []

    # read the CSV file into a list called accounts
    with open('accountList.csv') as accountList:
        reader = csv.DictReader(accountList)
        for row in reader:
            accounts.append(row)

    accountList.close()

    # print all the accounts
    for account in accounts:
        print account

    numberOfAccounts = len(accounts)
    print "Read " + str(numberOfAccounts) + " accounts from the input file"

    # pop an account from the accounts list and print the email address of it
    randomAccount = accounts.pop();
    print "Email address from account 0: " + randomAccount['emailAddress']

main()
