from datetime import datetime
from models import Account, Transaction

def main():
    account = Account(active=True, available_limit=1000)
    print(account)
    
    transaction = Transaction(merchant="Merchant A", amount=100, time=datetime.now())
    account.add_transaction(transaction)
    print(account)

if __name__ == "__main__":
    main()
