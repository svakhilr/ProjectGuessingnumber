import random

def game(attempt,num):
    game_on=True
    while game_on:
        print(f'you have {attempt} remaining to guess the number')
        guess=int(input('Make your guess'))
        if guess> num:
            print('guess is high try again')

        elif guess <num:
            print('guess is less try again')

        else:
            print('your guess is right')
            game_on=False
        attempt -=1

        if attempt == 0:
            game_on=False
            print(f'The number was {num}')

print('WELCOME TO TH GUESSING GAME')
random_num=random.randint(1,100)
print(f'number is {random_num}')

level=input("Choose your dificulty 'easy' or 'hard ").lower()
if level == "hard":
    attempts=5
else:
    attempts=10

game(attempt=attempts,num=random_num)
