import random

num_guesses = 0

#compares the two number, lowers the number of lives if needed
#Returns coorrect guess or not bool
def compare(player_guess, secret_num):
    global num_guesses
    if player_guess > secret_num:
        print("Too high.")
        return False
    elif player_guess < secret_num:
        print("Too low.")
        return False
    else:
        print(f"Yes! The secret number is {secret_num}! You win!")
        return True

#returns a bool
def one_more_time():
    one_more = input("Do you want to play again? Type y or n: ")
    if one_more == "y":
        return True
    else:
        return False

print("Welcome to the Number Guessing game.")

#setup
still_playing = True
while still_playing == True:
    print("I'm thinking of a number between 1 and 100")

    secret_number = random.randint(1,100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        num_guesses = 10
    else:
        num_guesses = 5
    
    #guess loop
    while num_guesses >0:
        new_guess = int(input(f"You have {num_guesses} left. Make a guess: "))
        verdict = compare(new_guess, secret_number)
        if verdict == True:
            break
        else:
            num_guesses -= 1
            if num_guesses <= 0:
                print("You Lose")
                break
            else:
                print("Guess again")
    still_playing = one_more_time()
    
        






