# #1-Rectangle class
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
#     def perimeter(self):
#         return 2*(self.width+self.height)
# rec=[Rectangle(2,3),Rectangle(3,4)]
# for r in rec:
#     print(f"Rectangle[Width:{r.width} | Height:{r.height} | Area:{r.area()} | Perimeter:{r.perimeter()}]")

# #2-Add a str
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
#     def perimeter(self):
#         return 2*(self.width+self.height)
#     def __str__(self):
#         return f"Rectangle {self.width}x{self.height} (area {self.area()})"
# rec=[Rectangle(2,3),Rectangle(3,4)]
# for r in rec:
#     print(r)

# #3-Student grades
# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.scores=[]
#     def add_score(self,score):
#         self.scores.append(score)
#     def average(self):
#         count=len(self.scores)
#         total=sum(self.scores)
#         return total/count
#     def __str__(self):
#         return f"Student:{self.name} | Average score: {self.average()}"
# std=Student("Ali")
# std.add_score(5)
# std.add_score(10)
# std.add_score(15)
# std.add_score(5)
# std.add_score(10)
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
#     print(f"{animal.name}: {animal.speak()}")        

# #5-Encapsulated counter
# class Counter:
#     def __init__(self):
#         self._count=0
#     def increment(self):
#         self._count+=1
#     @property
#     def value(self):
#         return self._count
# c=Counter()
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
#     def __init__(self, name):
#         self.name = name
#         self.done = False   # default status

#     def mark_done(self):
#         self.done = True

#     def __str__(self):
#         status = "Done" if self.done else "Not Done"
#         return f"{self.name} [{status}]"
# class TodoList:
#     def __init__(self):
#         self.tasks = []
#     def add_task(self, name, priority="n"):
#         task = Task(name)
#         if priority == "y":
#             self.tasks.insert(0, task)
#         else:
#             self.tasks.append(task)
#         print("Task added!")
#     def complete_task(self, task_number):
#         if 1 <= task_number <= len(self.tasks):
#             self.tasks[task_number - 1].mark_done()
#             print("Task marked as done!")
#         else:
#             print("Invalid task number!")
#     def display_tasks(self):
#         if not self.tasks:
#             print("No tasks yet.")
#             return
#         for index, task in enumerate(self.tasks, start=1):
#             print(f"{index}. {task}")
# def start():
#     todo = TodoList()
#     while True:
#         print("\nMenu:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Done")
#         print("4. Quit")
#         choice = input("Enter choice: ")
#         if choice == "1":
#             name = input("Enter task name: ").strip()
#             if not name:
#                 print("Task cannot be empty!")
#                 continue
#             priority = input("High priority? (y/n): ").lower()
#             todo.add_task(name, priority)
#         elif choice == "2":
#             todo.display_tasks()
#         elif choice == "3":
#             number = input("Enter task number to mark as done: ").strip()
#             if number.isdigit():
#                 todo.complete_task(int(number))
#             else:
#                 print("Please enter a valid number!")
#         elif choice == "4":
#             print("Goodbye! Stay productive.")
#             break
#         else:
#             print("Invalid choice!")
# start()
