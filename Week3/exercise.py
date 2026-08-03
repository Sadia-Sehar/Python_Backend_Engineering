# #1-Rectangle class
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     @property
#     def area(self):
#         return self.width*self.height
#     @property
#     def perimeter(self):
#         return 2*(self.width+self.height)
# rec=[Rectangle(2,3),Rectangle(3,4)]
# for r in rec:
#     print(f"Rectangle[Width:{r.width} | Height:{r.height} | Area:{r.area} | Perimeter:{r.perimeter}]")

# #2-Add a str
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     @property
#     def area(self):
#         return self.width*self.height
#     @property
#     def perimeter(self):
#         return 2*(self.width+self.height)
#     def __str__(self):
#         return f"Rectangle {self.width}x{self.height} (area {self.area})"
# rec=[Rectangle(2,3),Rectangle(3,4)]
# for r in rec:
#     print(r)

# #3-Student grades
# class Student:
#     def __init__(self,name,scores):
#         self.name=name
#         self.scores=scores
#     def add_scores(self,scores):
#         total_score=0
#         for score in scores:
#             total_score=total_score+score
#         return total_score
#     def average(self):
#         count=len(self.scores)
#         total=self.add_scores(self.scores)
#         return total/count
#     def __str__(self):
#         return f"Student:{self.name} | Average score: {self.average()}"
# std=Student("Ali",[5,10,5,15,10])
# print(f"Total score: {std.add_scores([5,10,5,15,10])}")
# print(std)

# #4-Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return "..."
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# animals=[Animal("Lucy"),Cat("Bella"),Dog("Duke"),Animal("Max")]
# for animal in animals:
#     print(animal.speak())        

# #5-Encapsulated counter
# class Counter:
#     def __init__(self,value):
#         self.value=value
#     @property
#     def value(self):
#         return self._value
#     @value.setter
#     def value(self,value):
#         if value<0:
#             self._value=0
#         else:
#             self._value=value
#     def increment(self):
#         self.value+=1
# c=Counter(3)
# c.increment()
# c.increment()
# c.increment()
# print(c.value)

# #6-Library system
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"Book Title: {self.title} | Author: {self.author}"
# class Library:
#     def __init__(self,books):
#         self.books=books
#     def add_book(self,new_book):
#         self.books.append(new_book)
#         print (f"{new_book} added to the library!")
#     def list_books(self):
#         for book in self.books:
#             print(book)
#     def find_by_author(self,author_name):
#         for book in self.books:
#             if(book.author==author_name):
#                 return book
#         return "No book found from this author!"
# books=[Book("123","ABC"),Book("456","DEF"),Book("789","GHI")]
# lib=Library(books)
# new_book=Book("012","JKL")
# lib.list_books()
# lib.add_book(new_book)
# lib.list_books()
# print(lib.find_by_author("GHI"))
# print(lib.find_by_author("XYZ"))

# #7-Rebuild Week2s to-do app with OOP
# class Task:
#     def __init__(self,name,status):
#         self.name=name
#         self.status=status
#     def __str__(self):
#         return f"Task: {self.name} | Status: {self.status}"
# class TodoList:
#     def __init__(self,tasks):
#         self.tasks=tasks
#     def add_task(self,new_task):
#         self.tasks.append(new_task)
#         print(f"[{new_task}] added to the list!")
#     def complete_task(self,complete):
#         completed=complete
#         self.tasks.remove(complete)
#         print(f"[{completed}] task completed!")
#     def display_tasks(self):
#         for index,task in enumerate(self.tasks,start=1):
#             print(f"{index}. {task}")
# tasks=[Task("coffee","not done"),Task("Workout","done"),Task("Study","not done")]
# my_list=TodoList(tasks)
# my_list.display_tasks()
# my_list.add_task(Task("Clean room","not done"))
# my_list.display_tasks()
# my_list.complete_task(tasks[2])
# my_list.display_tasks()
