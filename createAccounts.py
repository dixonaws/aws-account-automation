#!/usr/bin/python

import csv

def create_account(
        account_name,
        account_email,
        account_role,
        access_to_billing,
        organization_unit_id,
        scp):
        print "create_account(): I got account " + account_name
# create_account()

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

    # print lstAccounts

    account_name=""
    account_email=""
    account_role=""
    access_to_billing=""
    organization_unit_id=""
    scp=""

    # print all the accounts
    for account in lstAccounts:
        try:
            account_name=account['account_name']
            account_email=account['account_email']
            account_role=account['account_role']
            access_to_billing=account['access_to_billing']
            organization_unit_id=account['organization_unit_id']

        except KeyError:
            pass

        create_account(account_name, account_email, account_role,
                       access_to_billing, organization_unit_id, scp)
    # for account in lstAccounts
# main()

main()