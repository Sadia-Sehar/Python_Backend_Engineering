# 1-Countdown
for n in range(10):
    print(f"Count: {10-n}")
print("Lift off!")

# 2-Sum a list
prices=[4,9,2,7]
total=0
for price in prices:
    total+=price
print(f"Total price(using for loop): {total}")
print(f"Total price(using built-in function): {sum(prices)}")

# 3-Word lengths
def longest(words):
    if not words: #check empty list
        return "None! List is empty."
    result=words[0]
    for word in words:
        if len(word)>len(result):
            result=word
    return result
words=["Apple","Banana","Orange","Mango"]
print(words)
print(f"Longest word: {longest(words)}")

# 4-Vowel counter
def count_vowels(text):
    vowel_count=0
    for char in text.lower():
        if char in "aeiou":
            vowel_count+=1
    return vowel_count
text=input("Enter a word: ")
print(f"Vowel count: {count_vowels(text)}")

# 5-Phone book
def print_record(record):
    for key,value in record.items():
        print(f"{key}: {value}")
record={
    "Alex":123,
    "Bella":456,
    "Charles":789
}
print_record(record)
print("Adding a new contact... David: 123\n")
record["David"]=95
print_record(record)

# 6-Unique words
def unique_words_count(text):
    words=text.split()
    unique=set(words)
    count=len(unique)
    return count
text="I am a student and a photographer."
print(text)
print(f"Unique words count: {unique_words_count(text)}")

# 7-FizzBuzz
for n in range(1,31,1):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)

# 8-Grade book function
def average(scores):
    avg_score=sum(scores)/len(scores)
    return avg_score

def letter_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
user_input=input("Enter marks separated by spaces: ")
record=[int(x) for x in user_input.split()]
print(f"Grade: {letter_grade(average(record))}")

    