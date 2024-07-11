import unittest
from datetime import datetime
from autorizador.models import Transaction

class TestTransaction(unittest.TestCase):

    def test_transaction_creation(self):
        transaction = Transaction(merchant="Test Merchant", amount=100, time=datetime.now())
        self.assertEqual(transaction.merchant, "Test Merchant")
        self.assertEqual(transaction.amount, 100)

if __name__ == "__main__":
    unittest.main()
