import random
import json
import datetime
from operator import itemgetter

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []


player = input("Please enter your name: ")

with open("guess_game.json", "r") as score_file:
    score_list = json.loads(score_file.read())

best_score = sorted(score_list, key=itemgetter("attempts"))
top_three = 0

for score_dict in best_score:
    if top_three == 3:
        break
    else:
        print(f"player: {score_dict['player']},"
              f" secret number: {score_dict['secret']},"
              f" {score_dict['attempts']} attempts,"
              f" date: {score_dict['date']},"
              f" wrong guesses: {score_dict['wrong_guesses']}")
    top_three +=1

while True:
    guess = int(input(f"\nGuess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:

        score_list.append({"player": player,
                           "secret": secret,
                           "attempts": attempts,
                           "date": str(datetime.datetime.now()),
                           "wrong_guesses": wrong_guesses})

        with open("guess_game.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
