import random
print('welcome to number guessing game')
secret_number=random.randint(1.50)
guesses_remaining=5
while guesses_remaining>0:
  first_guess=int(input("enter a number:"))
  if first_guess is secret_number+20 or secret_number-20:
    print("your guess is ice cold")
   
