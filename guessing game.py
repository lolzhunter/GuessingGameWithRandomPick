import random
counter = 0
lastnumber = int(input('''the range for the guessing game,
for example: 1 to x '''))
stop = "test"
while stop != "stop":
  counter = 0
  n = random.randint(1, lastnumber)
  guess = random.randint(1, lastnumber)
  optimize = 1
  optimize2 = lastnumber
  print("parameters are {0} and {1}\n".format(optimize, optimize2))
  print("the chances of guessing the number are 1 out of", optimize2)
  print(guess, "is the first guess")
  while True:
    if guess < n:
        optimize = guess+1
        guess = random.randint(optimize, optimize2)
        print("guess is low\n"+"parameters are now {0} and {1}\n".format(optimize, optimize2))
        chance = optimize2 - optimize
        chance+=1
        print("the chances of guessing the number are 1 out of", chance)
        print(guess)
        counter+=1
    elif guess > n:
        optimize2 = guess-1
        guess = random.randint(optimize, optimize2)
        print("guess is high\n"+"parameters are now {0} and {1}\n".format(optimize, optimize2))
        chance = optimize2 - optimize
        chance+=1
        print("the chances of guessing the number are 1 out of", chance)
        print(guess)
        counter+=1
    else:
        print("you guessed it after {0} tries!\n".format(counter))
        print('''final parameters were:
         {0} and {1}\n'''.format(optimize, optimize2))
        print("the number was", n)
        stop = input()
        break
    print
