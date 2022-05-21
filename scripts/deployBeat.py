from brownie import getBeat, accounts


def main():
    acct = accounts.load('deployment_account')
    getBeat.deploy({'from': acct})