from datetime import datetime
from models import Account, Transaction

def authorizer():
    account = Account(active=True, available_limit=1000)
    if account.active == True:
        print("A conta está ativa!")
        transaction = Transaction(merchant="Merchant1", amount=1000, time=datetime.now())
        if account.history
        if transaction.amount <= account.available_limit*0.9:
            print("Essa transacao não excede 90 porcento do limite.")
            if transaction.amount <= account.available_limit:
                print("Essa transacao não excede o valor total do limite.")
            
            account.add_transaction(transaction)
        else:
            print("Deu errado") 
    else:
        print(account)

# def main():
#     account = Account(active=True, available_limit=1000)
#     print(account)
    
#     transaction = Transaction(merchant="Merchant A", amount=100, time=datetime.now())
#     account.add_transaction(transaction)
#     print(account)

if __name__ == "__main__":
    authorizer()
