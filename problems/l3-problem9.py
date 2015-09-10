low, high = 0, 100
guess = 50
answer = ""

print('Please think of a number between 0 and 100!')

while answer != "c":
  print("Is your secret number " + str(guess) + "?")
  answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

  if answer == "c":
    break
  elif answer == "h":
    high = guess
    guess = (low + high) / 2
  elif answer == "l":
    low = guess
    guess = (low + high) / 2
  else:
    print("Didn't get this answer")

print("Game over. Your secret number was: " + str(guess))
