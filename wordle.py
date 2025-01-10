import random

def check_guess(your_guess, secret_word):
    result = ["⬜"] * 5
    letters_left = {}

    for letter in secret_word:
        letters_left[letter] = letters_left.get(letter, 0) + 1

    for i in range(5):
        if your_guess[i] == secret_word[i]:
            result[i] = "🟩"
            letters_left[your_guess[i]] -= 1

    for i in range(5):
        if result[i] == "🟩":
            continue
        if your_guess[i] in letters_left and letters_left[your_guess[i]] > 0:
            result[i] = "🟨"
            letters_left[your_guess[i]] -= 1

    return result

def start_game():
    fruits = [
        "apple", "grape", "peach", "mango", "berry", "melon", "lemon", "guava", 
        "cherry", "papaya", "plums", "kiwis", "dates", "figs", "prune", "olive",
        "pear", "lychee", "apric", "banan", "orange"
    ]

    secret_word = random.choice(fruits)
    max_tries = 6
    attempts = 0

    print("Welcome to the Super-Noob Friendly Wordle Game!")
    print("The secret word is a common fruit. Try to guess it in 6 attempts.")
    print("🟩: Correct letter and position")
    print("🟨: Correct letter but wrong position")
    print("⬜: Letter not in the word")

    while attempts < max_tries:
        your_guess = input(f"\nTry {attempts + 1}/{max_tries}: Enter a 5-letter fruit: ").strip().lower()

        if len(your_guess) != 5:
            print("Oops! Make sure it's a 5-letter fruit. Try again.")
            continue

        feedback = check_guess(your_guess, secret_word)
        print("Feedback:", " ".join(feedback))

        if your_guess == secret_word:
            print("🎉 Yay! You guessed the fruit! You're a word wizard!")
            break

        attempts += 1

    if attempts == max_tries:
        print(f"Game Over! The correct fruit was: {secret_word}.")

def main():
    while True:
        start_game()
        restart = input("\nWant to play again? Type 'yes' to restart or anything else to quit: ").strip().lower()
        if restart != 'yes':
            print("Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()
