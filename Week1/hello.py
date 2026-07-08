print("Hello. Future programmer.")



age = 15
her_name1="sara"
print(age)
print(her_name1)

x=10
print(type(x))
x="abc"
print(type(x))
x=3.14
print(type(x))
x=True
print(type(x))


print(10/2)
print(10//2)
print(10%2)
print(2**3)


age=16
has_permission=True
print(age>=13 and has_permission)
print(age<13 or has_permission)
print(not has_permission)
boolean=True
print(boolean+boolean)
print(int(True))
print(int(False))
print(isinstance(3,int))
print(isinstance(True,int))
print(isinstance(True,bool))
text="hi"
results=[True, False, True, False, True, False, text]
print(text in results)
print("h" in text)


#-----String-----
name="Sara"
score=92
print(f"Well done {name}! You scored {score+1}%")
price=3.4567
print(f"Price: {price:.10f}")
print(f"Hello, {name}")
x=5
y=3
print(f"{x}+{y}={x+y}")
print(f"{price:.2f}")
#-----Text alignment-----
print(f"|{name:^10}  {score:>6}%|  ")
print(f"|{name:^10}  {score:>6}%|  ")
print(f"|{name:^10}  {score:>6}%|  ")
population=1234.345
print(f"{population:,}")
print(f"{population:%}")
print(f"{population:.2%}")
population=1
print(f"{population:.0%}")


word="Python"
print(word[0])
print(word[2])
print(word[-1])
print(word[0:3])
print(word[2:])
print(word[:3])
num=2000
num=1_000
print(num)
x = 12345
print(type(x))
y = str(x)
print(type(y))
print(y[0])
print(y[4])
num=123
print(num)

#-----Methods-----
print("hi".upper())
print('HI'.lower())
print(" Hi ".strip())
print("cat".replace("c","b"))
print("a b c".split())
print(len("Hello"))
word="sadia"
print(word.capitalize())
print(word)
print(word.upper())
print(word)
print(word.lower())
word=word.upper()
print(word)
print(word[1])
print(len({"a":1, "b":2})) #Dictionaries (week2)


#-----Input and Decisions-----
name=input("What is your name? ")
print(f"Hello, {name}!")
age=int(input("Age:   "))
age=input("Age: ")
age=int(age)
age=age+5
print(f"Age is: {age}")
#IF ELSE
age=int(input("Age:   "))
if age>=18:
    print("You are an adult.") 
elif age>=13:
    print("You may enter with a guardian.")
else:
    print("Too young today.")