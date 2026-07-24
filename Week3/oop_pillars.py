# # 1-Encapsulation
# # 2-Inheritance
# # Name mangling, MRO, composition
# # type(obj) tells the actual class that created the object
# # isinstance(obj, ParentClass) tells whether the object belongs to that class or any of its parent classes (preferred)

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
    
# class SavingsAccount(BankAccount):
#     def __init__(self,owner,balance=0,rate=0.05):
#         super().__init__(owner,balance)
#         self.rate=rate
#     def add_interest(self):
#         self.balance+=self.balance*self.rate
#         return self.balance
# s=SavingsAccount("Ali",1000)
# print(s.deposit(500))
# print(s.add_interest())

# # polymorphism
# class Animal:
#     def speak(self):
#         print("Some sound")
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
# d=Dog()
# print(dir(d))
# animals=[Dog(),Cat(),Animal(),Dog()]
# animals[0].speak()
# animals[1].speak()
# animals[2].speak()
# animals[3].speak()
# for animal in animals:
#     animal.speak()
# print(Dog.mro())

# # Polymorphism doesn't require inheritance in Python
# class Cat:
#     def speak(self):
#         print("Meow")
# class Dog:
#     def speak(self):
#         print("Woof")
# animals=[Cat(),Dog()]
# # method 1
# for animal in animals:
#     animal.speak()
# # method 2
# def make_sound(animal):
#     animal.speak()
# make_sound(animals[0])
# make_sound(animals[1])
# # method 3
# make_sound(Cat())
# make_sound(Dog())

# class Circle:
#     def __init__(self,r):self.r=r
#     def area(self): return 3.14159*self.r**2
# class Square:
#     def __init__(self,side):self.side=side
#     def area(self): return self.side**2
# shapes=[Circle(5),Square(4),Circle(2)]
# for shape in shapes:
#     print(shape.area())
# shapes.append(Square(4))
# for shape in shapes:
#     print(shape.area())

# #sort(key,reverse) vs. sorted(obj,key,reverse)
# numbers=[5,2,8,1]
# print(numbers.sort())
# print(numbers)
# new_list=sorted(numbers)
# print(new_list)