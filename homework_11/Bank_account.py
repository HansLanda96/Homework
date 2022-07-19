"""
Awesome Class Bank Account
"""
from uuid import uuid4, uuid1           # Using built-in module to create id of acc and transaction
from decimal import Decimal             # Using built-in module for easiest bank calculation
from datetime import datetime as dt     # Using built-in module for date now


class Transaction:

    """
        A class that represent Transactions

    __init__ Attributes
    __________
    amount: Decimal
        Means Money amount  (Always rounded with 2 numbers after dot)

    commission: Decimal
        Represent commission for operation (Always equal 1%)

    operation:
        Represent the type of transaction (Deposit or Withdrawal)

    date: datetime
        Represent date the transaction took place

    status='Confirmed'
        Represent status of operation. If operation approved - status "Confirmed". "Fail" otherwise

    uid=uuid()
        Represent unique number for operation
    __________

    Methods
    __________
    __str__(self)
        Print beautiful output in console :D
    """

    def __init__(self, amount: Decimal, operation: str, status="Confirmed"):
        self.amount = round(amount, 2)
        self.commission = round(amount * Decimal(0.01), 2)
        self.operation = operation
        self.date = dt.now().strftime("%d.%m.%Y %H:%M:%S")
        self.status = status
        self.uid = uuid4()

    def __str__(self):
        if self.operation == "Deposit":
            self.commission = 0
        return f'''
                        Date: {self.date}
                        Transaction ID: {self.uid}
                        Status: {self.status}
                        Operation: {self.operation}
                        Amount of Money for transaction: {self.amount} UAH
                        Bank commission for operation: {self.commission} UAH
        '''

    def __repr__(self):
        return self.__str__()


class BankAccount:
    """
    A class that represent a bank account.

    __init__ Attributes
    __________
    name :  str
        Name of account holder

    surname : str
        Surname of account holder

    uid :   UUID
        Unique number of account

    balance :   Decimal
        Represent balance of account

    transactions : list
        This attribute will represent [type of operation, amount, and date of operation]
    __________

    Methods
    __________
    __str__(self)
        Print beautiful output in console :D

    _valid_name(self, name)
        Method check name and surname for acceptable writing

    _format_transactions(self)
        Method formatting instance self._transactions for normal output

    deposit(amount: float | int)
        Method will add amount to account of user

    withdrawal(amount: float | int)
        Method will subtract amount from user account

    balance_changes(self, transactions)
        Create dict of types operations and counting balance change proceeding from type operation
    __________
    """

    def __init__(self, name: str, surname: str):
        self._name = self._valid_name(name.capitalize())
        self._surname = self._valid_name(surname.capitalize())
        self._uid = uuid1()
        self._balance = (Decimal(0))
        self._transactions = []

    def __str__(self):
        return f'''
        
        Bank Account:
            Account Owner: {self._name} {self._surname}
            Account ID: {self._uid}
            Current Balance: {self._balance} UAH
            
            Transactions: {self._format_transactions()}
        '''

    def __repr__(self):
        return self.__str__()

    def _valid_name(self, name):
        if len(name) > 17:
            raise ValueError(f'Your {name} cannot be more than 17 characters')
        if not name.isalpha():
            raise ValueError(f'{name} must be only with letters')
        return name

    def _format_transactions(self):
        return "\n".join([str(transaction) for transaction in self._transactions])

    def deposit(self, amount: float | int):
        self._transactions.append(Transaction(Decimal(amount), "Deposit"))
        self.balance_changes(self._transactions[-1])

    def withdrawal(self, amount: float | int):
        if self._balance - Decimal(amount) < 0:
            self._transactions.append(
                Transaction(Decimal(amount), 'Withdrawal', 'Failed. Insufficient funds to complete the operation'))
        else:
            self._transactions.append(Transaction(Decimal(amount), 'Withdrawal'))
            self.balance_changes(self._transactions[-1])

    def balance_changes(self, transactions):
        types = {
            'Deposit': self._balance + transactions.amount,
            'Withdrawal': self._balance - transactions.amount - transactions.commission
        }
        self._balance = types[transactions.operation]


def main():
    account = BankAccount("Egor", "Marchenko")
    account.withdrawal(100)
    account.deposit(3000)
    account.withdrawal(2300)
    account.withdrawal(100)
    account_1 = BankAccount("Oleksiy", "Fedoriv")
    account_1.deposit(5000)
    account_1.withdrawal(10000)
    account_1.withdrawal(3000)
    print(account, account_1)


if __name__ == '__main__':
    main()
