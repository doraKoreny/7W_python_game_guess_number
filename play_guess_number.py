from guess_number import guess_number


def give_exercise(name, lowest, highest):
    print("Well %s, I am thinking of a number between %d and %d." % (name, lowest, highest))


def check_guess(guess, number, name, guessing_round):
    if guess != number:
        if guess > number:
            print(input("Your guess is too high.\nTake a guess.\n"))
        elif guess < number:
            print(input("Your guess is too low.\nTake a guess.\n"))
    elif guess == number:
        print("Good job, %s! You guessed my number in %d guesses!" % (name, guessing_round))
        

def main():
    random_number = guess_number(1,20)
    print(random_number)
    player_name = input("Hello! What's your name?")
    give_exercise(player_name, 1, 20)
    count_guesses = 0
    user_guess = int(input("Take a guess\n"))
    while user_guess != random_number:
        check_guess(user_guess, random_number, player_name, count_guesses)
        count_guesses += 1


if __name__ == '__main__':
    main()
