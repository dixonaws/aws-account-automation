#!/usr/bin/python

import csv

def create_account(
        account_name,
        account_email,
        account_role,
        access_to_billing,
        organization_unit_id,
        scp):
        print "create_account(): I got account " + account_email


def main():
    lstAccounts = []

    # read the CSV file into a list called accounts
    with open('accountList.csv') as filAccountList:
        reader = csv.DictReader(filAccountList)
        for row in reader:
         lstAccounts.append(row)

    filAccountList.close()

    intNumberOfAccounts = len(lstAccounts)
    print "Read " + str(intNumberOfAccounts) + " accounts from the input file"


    # print all the accounts
    for account in lstAccounts:
        # pop an account from the accounts list and print the email address of it
        create_account("testaccount", account['emailAddress'],"","","","")

main()