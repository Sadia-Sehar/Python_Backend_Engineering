# ===The Personal Greeter & Quiz===
secret_num=65

print("Welcome to The Personal Greeter & Quiz Game!")
name=input(f"Enter your name: ")
print(f"Hi {name.capitalize()}! Nice to meet you.")

age=int(input(f"How old are you? "))
print(f"You will be {age+10} in ten years.")

#first try
guess1=int(input(f"I have a secret number from 1-100. Guess it:  "))
if guess1==secret_num:
    print("Congratulations! You guessed it.")
elif guess1<secret_num:
    if guess1>=(secret_num-5):
        print("Close call! Aim a little higher.")
    else:
        print("Too Low! Better luck next time.")
elif guess1>secret_num:
    if guess1<=(secret_num+5):
        print("Close call! Aim a little lower.")
    else:
        print("Too High! Better luck next time.")

if guess1!=secret_num:        
#second try
    guess2=int(input(f"Try again:  "))
    if guess2==secret_num:
        print("Congratulations! You guessed it.")
    elif guess2<secret_num:
        if guess2>=(secret_num-5):
            print(f"Almost! The secret number was {secret_num}.")
        else:
            print(f"Too Low! The secret number was {secret_num}.")
    elif guess2>secret_num:
        if guess2<=(secret_num+5):
            print(f"Almost! The secret number was {secret_num}.")
        else:
            print(f"Too High! The secret number was {secret_num}.")
   

print(f"Game over! See you next time {name.capitalize()}.")      



