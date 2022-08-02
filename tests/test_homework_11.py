from unittest import TestCase, main
from homework_11.Bank_account import Transaction, BankAccount, Decimal


class TestBankAccount(TestCase):
    def setUp(self):
        self.account = BankAccount("Egor", "Marchenko")

    def test_BankAccount_class(self):
        self.assertEqual(self.account._name, "Egor")
        self.assertEqual(self.account._surname, "Marchenko")
        self.assertEqual(self.account._balance, Decimal(0))
        self.assertEqual(self.account._transactions, [])

    def test_valid_name1(self):
        with self.assertRaises(ValueError) as e:
            self.account._valid_name("sdflk;gjdf;klgdfkjgl")
        self.assertEqual("Your name cannot be more than 17 characters", e.exception.args[0])

    def test_valid_name2(self):
        with self.assertRaises(ValueError) as e:
            self.account._valid_name("1231254125")
        self.assertEqual("Name or surname must be only with letters", e.exception.args[0])

    def test_balance_changes(self):
        self.account.deposit("100.73")
        self.account.withdrawal("2300.15")
        self.assertEqual(self.account._balance, Decimal('100.73'))

    def test_deposit(self):
        self.account.deposit("100.73")
        self.assertEqual(self.account._balance, Decimal("100.73"))
        self.assertEqual(self.account._transactions[-1].amount, Decimal("100.73"))
        self.assertEqual(self.account._transactions[-1].operation, "Deposit")
        self.assertEqual(self.account._transactions[-1].status, "Confirmed")

    def test_withdrawal(self):
        self.account.deposit("100.73")
        self.account.withdrawal("2300.15")
        self.assertEqual(self.account._balance, Decimal('100.73'))
        self.assertEqual(self.account._transactions[-1].amount, Decimal('2300.15'))
        self.assertEqual(self.account._transactions[-1].operation, "Withdrawal")
        self.assertEqual(self.account._transactions[-1].status, "Failed. Insufficient funds to complete the operation")
        self.account.withdrawal("50")
        self.assertEqual(self.account._balance, Decimal('50.23'))

    def test_Transaction_class(self):
        transaction = Transaction(Decimal("100.73"), "Deposit")
        self.assertEqual(transaction.amount, Decimal("100.73"))
        self.assertEqual(transaction.operation, "Deposit")
        self.assertEqual(transaction.commission, 0)
        self.assertEqual(transaction.status, "Confirmed")


if __name__ == '__main__':
    main()
