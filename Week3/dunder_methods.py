# # str()-called with print(object),str(object)
# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"Dog({self.name})"
# rex=Dog("Rex")
# print(rex)

# # repr()-called with repr(object), print a list containing objects
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     # def __str__(self):
#     #     return f"Student('{self.name} scored {self.marks}')"
#     def __repr__(self):
#         return f"Student('{self.name}', {self.marks})"
# std=Student("Ali",95)
# # print(std)
# print(str(std))
# # print(repr(std))
# # students=[Student("Ali",90),Student("Sara",90),Student("Ahmer",90)]
# # print(students)

# # len()
# class Book:
#     def __init__(self,name,pages):
#         self.name=name
#         self.pages=pages
#     def __len__(self):
#         return self.pages
# book=Book("ABS",255)
# print(len(book))

# # eq()
# class Book:
#     def __init__(self,name,pages):
#         self.name=name
#         self.pages=pages
#     def __eq__(self,other):
#         return self.name==other.name
# b1=Book("abc",230)
# b2=Book("abc",230)   
# print(b1==b2)

# # Class variable vs. Instance variable
# class Dog:
#     species="Canis"
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"{self.name} is {self.species}"
# rex=Dog("Rex")
# bella=Dog("Bella")
# # print(rex)
# # print(bella)
# Dog.species="Wolf"
# rex.species="hiii"
# print(rex.species)
# print(bella.species)


