def deposite(db,amount):
    for i in db:
        i.balance+=amount
        return (i.balance)
    
        