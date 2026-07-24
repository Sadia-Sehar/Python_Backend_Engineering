# # Class and objects
# class Dog:
#     def bark(self):
#         print("Woof")
# rex=Dog()
# bella=Dog()        
# rex.bark()
# bella.bark()

# Attributes- appears the moment you assign it & init()
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print(f"{self.name} says Woof! he is {self.age} years old")
rex=Dog("Rex","Golden Retriever")
# rex.age=4
rex.bark()
# print(rex.age) #works-directly accessing the attributes
# bella=Dog("Bella","Golden Retriever")
# bella.bark() #shows error
# reinitialization is allowed
# rex.__init__("Max","Poodle")
# rex.age=5
# rex.bark()
# self is a convention-not a keyword. Any other word is legal

# class Dog:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed

#     def bark(self):
#         return f"{self.name} says woof!"
# rex=Dog("Rex","Labrador")
# bella=Dog("bella","Poodle")
# print(rex.bark())
# print(bella.breed)

# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return self.balance
    
#     def withdraw(self,amount):
#         if amount>self.balance:
#             return "Insufficient funds."
#         self.balance=self.balance-amount
#         return self.balance
# acct=BankAccount("Sara",100)
# acct.deposit(50)
# print(acct.deposit(50))
# print(acct.withdraw(200))
# print(acct.balance)

