import unittest
from datetime import datetime
from autorizador.models import Account, Transaction

class TestAccount(unittest.TestCase):

    def test_add_transaction(self):
        account = Account(active=True, available_limit=1000)
        transaction = Transaction(merchant="Test Merchant", amount=200, time=datetime.now())
        account.add_transaction(transaction)
        self.assertEqual(account.available_limit, 800)
        self.assertEqual(len(account.history), 1)
        self.assertEqual(account.history[0], transaction)

if __name__ == "__main__":
    unittest.main()
