import random

print("-----NUMBER GUESSING GAME------")

print("select difficulty:")
print("1. Easy(1-50)")
print("2. medium (1-100)")
print("3.hard (1-200)")

choice = input("enter the choice (1/2/3):")

if choice =="1":
    number = random.randint(1, 50)

elif choice =="2":
    number = random.randint(1, 100)
    
elif choice =="3":
    number = random.randint(1, 200)

else:
    print(" invalid choice, defaulting to medium")
    number = random. randint(1, 100)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input("guess a number :"))
    attempts +=1

    if guess > number:
        print("Too high")

    elif guess < number:
        print("Too low")

    else:
        print("correct! you guessed it")
        print("you guessed in ",attempts,"attempts")
        break

    difference = abs(guess - number)

    if difference <= 5:
        print("hot (very close to 0-5)")
    
    elif difference <= 15:
        print("warm (close to 6-15)")
    else:
        print("cold (far:- more than 15  away)")

if attempts == max_attempts and guess != number:
    print("Game Over! The number was", number)

