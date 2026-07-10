# numbers=[1,2,3,4,5]
# squares= []
# for number in numbers:
#     squares.append(number*number)
# print(numbers)
# print(squares)

# squares=[number**2 for number in numbers]
# print(numbers)
# print(squares)

# names=["ali","sara","ahmed"]
# upper_names=[name.upper() for name in names if name=="sara"]
# print(upper_names)

# numbers=[1,2,3,4,5,6]
# evens=[num for num in numbers if num%2==0]
# print(evens)

# # dictionary comprehension
# numbers=[1,2,3,4,5]
# squares={number:number**2 for number in numbers}
# print(squares)

# # set comprehension
# numbers=[1,2,3,4,5,3,4,5]
# unique={number for number in numbers}
# print(unique)

# # tuple comprehension
# numbers=[1,2,3,4,5]
# new=tuple(number for number in numbers)
# print(new)

# if...else in comprehension
numbers=[1,2,3,4,5,6]
result=[n if n%2==0 else 0 for n in numbers]
print(result)