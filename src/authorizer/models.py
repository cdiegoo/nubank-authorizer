from datetime import datetime

class Transaction:
    def __init__(self, merchant: str, amount: int, time: datetime):
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def __str__(self):
        return f"Transaction(merchant={self.merchant}, amount={self.amount}, time={self.time})"

class Account:
    def __init__(self, active: bool, available_limit: int):
        self.active = active
        self.available_limit = available_limit
        self.history = []

    def add_transaction(self, transaction: Transaction):
        self.history.append(transaction)
        self.available_limit -= transaction.amount

    def __str__(self):
        history_str = ', '.join(str(tx) for tx in self.history)
        return f"Account(active={self.active}, available_limit={self.available_limit}, history=[{history_str}])"
