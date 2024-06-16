import random

number = random.randint(1, 100)

attempt = 1
guess = int(input("Enter a number between 1 and 100: "))

while True:
    if guess < number:
        guess = int(input("Enter another number! Your guess is less than the number 📈: "))
        attempt += 1
    elif guess > number:
        guess = int(input("Enter another number! Your guess is greater than the number 📉: "))
        attempt += 1
    else:
        print("Congratulations✨")
        print("You won the match..! 😊")
        print(f"Yeah, this is the number! You guessed the number in {attempt} attempts.")
        break
