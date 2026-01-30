import random

a = random.randint(1, 100)

i = 0

while True:
    
    z = int(input("Guess a number between 1 and 100: "))

    if (z < 1 or z > 100):
        print("Please enter a number between 1 and 100")
        continue

    i += 1
    
    if (z == a):
        print("Correct!")
        print("You guessed it in", z, "attempts")
        break
    elif (z <= a):
        print("Too Low, try Again")
        i += 1

    else:
        print("Too High, try Again")
        i += 1