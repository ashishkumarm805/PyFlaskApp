from deposite import deposite
from withdraw import withdraw
class coustomerDetails:
    def __init__(self,id,account,account_type,balance,address,age):
        self.id=id
        self.account=account
        self.account_type=account_type
        self.balance=balance=balance
        self.address=address
        self.age=age
class coustomer:
    def __init__(self,coustomer_db):
        self.coustomer_db=(coustomer_db)
if __name__ =='__main__':
    n=int(input())
    coustomer_db=[]
    for i in range(n):
        id=input()
        account=input()
        account_type=input()
        balance=int(input())
        address=input()
        age=int(input())
        c=coustomerDetails(id, account, account_type, balance, address, age)
        coustomer_db.append(c)
    print ("enter the deposite item")
    ammount=int(input())
    newBalance=deposite(coustomer_db,ammount)
    print (newBalance)
    print ("enter ammount to withdraw")
    value=int(input())
    newBalance=withdraw(coustomer_db,value)
    print (newBalance)