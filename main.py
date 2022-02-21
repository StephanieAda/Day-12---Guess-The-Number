import art
import random

print(art.logo)

number = random.randint(0,100)
end = ["Such a shame, and you were so close too", "Opps, you've run out of guess!!", "And that's a cap, no guesses left"]
def difficulty(diff):
  stop = False
  while diff > 0 and not stop:
    print(f"You have {diff} guesses left. ")
    guess = int(input("Take a guess: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    elif guess == number:
      print(f"You guessed right, {number} is correct")
      stop = True
    diff -= 1
    if diff == 0:
      print(random.choice(end))


print("Welcome to Guess The Number.")
# print(number)
mode = input("Choose a difficulty mode, 'easy' or 'hard'?: ")
if mode == 'easy':
  easy = 10
  difficulty(easy)
elif mode == 'hard':
  hard = 5
  difficulty(hard)