# untested code, just for SRP example

import random


class DepositManager:
    def deposit_money(self, account, amount):
        account.balance += amount
        return account.balance


class WithdrawManager:
    def withdraw_money(self, account, amount):
        account.balance -= amount
        return account.balance


class BalanceManager:
    def check_balance(self, account):
        return account.balance


class AccountNumberManager:
    def generate_account_number(self):
        return random.randint(100000, 999999)


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.balance_manager = BalanceManager()
        self.deposit_manager = DepositManager()
        self.withdraw_manager = WithdrawManager()
        # to get new account number
        self.account_number_manager = AccountNumberManager()

    def deposit(self, account, amount):
        return self.deposit_manager.deposit_money(self, account, amount)

    def withdraw(self, account, amount):
        return self.withdraw_manager.withdraw_money(self, account, amount)

    def check_balance(self, account):
        return self.balance_manager.check_balance(account)

    def generate_account_number(self):
        return self.account_number_manager.generate_account_number()

    def get_account_number(self):
        return self.account_number
