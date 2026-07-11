# For LOOP
# ===range()==== produces numbers, doesn't store them
# range() with a number range(stop), start at 0
for number in range(5):
    print(f"Count: {number}")
# range() with a range(start,end)
for number in range(3,5):
    print(number)
# range() with a step range(start,end,step(gap))
for number in range(2,11,2):
    print(number)
numbers=range(5)
print(numbers) #prints range(0,5) - a sequence not a list
for i in numbers: #prints numbers one by one
    print(i) 
numbers=range(2,6)
print(numbers)
for i in range(2,6):
    print(i)
numbers=range(2,11,2)
print(numbers)
for i in numbers:
    print(i)
# list() converts the sequence into a list
numbers=list(range(0,5))
print(numbers) #prints [0,1,2,3,4]
# Check membership
print(3 in range(5))
print(3 in range(0,5))
print(3 in range(2,6,2))
# Find length
print(len(range(5)))
print(len(range(0,5)))
print(len(range(2,11,2)))
# Indexing and slicing
numbers=range(4,15)
print(numbers[2])
print(numbers[2:6]) #prints range(6,10) bcz it's not a list but a range
print(list(numbers[2:6])) #prints [6,7,8,9]-a list

# while loop
password=""
while password!="swordfish":
    password=input("Enter password: ")
print("Access granted")
# using break
while True:
    password=input("Enter password: ")
    if password=="secret":
        break
print("Access Granted!")
# using continue
count=0
while count<=5:
    count+=1
    if count==3:
        continue
    print(count)
# for games
# while player_alive:

# Lists-ordered,editable,happy to repeat
fruits=["Apple","Banana","Orange"]
print(fruits[0])
fruits.append("Date")
fruits[1]="Cherry"
print(fruits)
print(len(fruits))
for fruit in fruits:
    print(f"I like {fruit}.")
results=[True,False,True,False]
for result in results:
    print(result)
data=["Ali",2,True, 3.5] #lists can have any type, even multiple types
# print(sum(data)) #won't work
print(data[1:5])
# data[4]=False #not allowed, index out of range
data.remove(data[2])
data.remove("Ali")
print(data)
# membership
print("Ali" in data)
# Common methods apart from append() and remove()
last=data.pop()
print(f"Last item: {last}")
data.insert(2,False) #creates space amd moves the rest of the items one index forward
data=[2,3,6,7,1,4,8,5]
data.sort()
print(data)
data.reverse()
print(data)
print(data.count(1)) #counts occurences
print(data.index(2)) #Positiob by value

# Tuples-ordered, immutable, repeatable
point=(3,5,5)
print(point[0])
print(point[0:])
print(point)
point[0]=6 
# Methods: index() and count()
print(point.count(5))
# single-element tuple
x=(2)
print(type(x))
x=(2,)
print(type(x))
x=(2,3,4,)
print(x)
# packing and unpacking
person="Sadia", 20, "Python" #same as person=("Sadia",20,"Python")
print(person)
name,age,course=person
print(name)
print(age)
print(course)

# Dictionaries-(key:value)
student={
    "name":"Sadia",
    "age":"20",
    "major":"SE"
}
print(f"{student["name"]} is {student["age"]} years old and studying {student["major"]}.")
# changing values
student["age"]=21
print(student)
# adding new key
student["city"]="Fsd"
print(student)
# removing a key
del student["city"]
print(student)
print(len(student))
# membership-checks keys not values
print("name" in student)
print("Sadia" in student)
print("Sadia" in student.values())
# looping through dictionary
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)
# Common methods
print(student.keys())
print(student.values())
print(student.items()) #each item is a tuple
# keys-non repeatable, values-repeatable
# when you aren't sure about what the dictionary has
print(student.get("city", "City not provided"))

# sets- unordered,non-repeatable,mutable
colors={"red","blue","green","green"}
print(colors)
# Membership checks-extremely fast
print("red" in colors)
# adding items
colors.add("orange")
print(colors)    
# removing item
colors.remove("orange")
colors.discard("blue")
print(colors)
colors.clear() #clears data
print(colors)
colors.add("pink")
print(colors)
print(len(colors))
# empty dict
empty={}
print(type(empty))
# empty set
empty=set()
print(type(empty))
for color in colors:
    print(color)
# Set operations
science={"Ali","Sara","Ahmed"}
sports={"Sara","Ahmed","Fatima"}
print(science | sports) #union
print(science.union(sports))
result=science.union(sports)
print(result)
print(science & sports) #intersection
print(science - sports) #difference
print(science ^ sports) #symmetric difference-exactly one 

