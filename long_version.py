import random

number = random.randint(0,100)
print("Welcome to Guess The Number.")
# print(number)
mode = input("Choose a difficulty mode, 'easy' or 'hard'?: ")

if mode == 'easy':
  easy = 10
  stop = False
  while easy > 0 and not stop:
    print(f"You have {easy} guesses left. ")
    guess = int(input("Take a guess: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    elif guess == number:
      print(f"You guessed right, {number} is correct")
      stop = True
    easy -= 1
    if easy == 0:
      print("Awn, you've run out of guesses, better luck next time.")
elif mode == 'hard':
  print("You have 5 guesses to correctly guess the correct number:")
  hard = 5
  stop = False
  while hard > 0 and not stop:
    print(f"You have {hard} guesses left. ")
    guess = int(input("Take a guess: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    elif guess == number:
      print(f"You guessed right, {number} is correct")
      stop = True
    hard -= 1
    if hard == 0:
      print("Oops, you've run out of guesses!!")