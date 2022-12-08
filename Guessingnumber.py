import random
guess_done= 0
print("Hi! What is your name?")
myname = input("Your name: ")
number = random.randint(0,100)
print(f'Well,{myname},I am thinking of a number between 0 to 100😊.')
print("\n\tYou have 7 Chances to Guess ")
while guess_done<8:

    guess =int(input("Enter Your Number:- "))
    guess_done = guess_done+1
    if guess < number:
        print("Your guess is too low!🙄")
    if guess > number:
        print("Your guess is too high!🥱")
    if guess==number:
        break
if guess==number:
    print(f"\n\tCongratulations✌, {myname} You guessed my number in {guess_done} guesses!")
if guess !=number:
    print(f"Nope😁.The number I was thinking is {number}.")
    print("Better luck next time")
