import random


# GET GUESS
def get_guess():
    return list(input("What is your guess? "))


# Generate computer code 123
def generate_code():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]


# Generate clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return f"Code Cracked!\nNumber of guesses: {g_num}"

    clues = []
    for idx, num in enumerate(user_guess):
        if num == code[idx]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')

    if not clues:
        return ['Nope']
    else:
        return clues


# Run game logic
print('Welcome Code Breaker!')
secret_code = generate_code()

clue_report = []
g_num = 1

while clue_report != 'CODE CRACKED!':

    guess = get_guess()
    g_num += 1

    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
