import random
import string

# Words with hints
WORDS = {
    "python": "A popular programming language 🐍",
    "variable": "Used to store data in a program",
    "function": "Block of reusable code",
    "loop": "Repeats a block of code",
    "algorithm": "Step-by-step procedure to solve a problem"
}

MAX_WRONG = 6  # number of lives

def choose_word():
    word = random.choice(list(WORDS.keys()))
    hint = WORDS[word]
    return word, hint

def display_state(word, guessed, wrong_letters, hint):
    masked = "".join([c if c in guessed else "_" for c in word])
    lives_left = MAX_WRONG - len(wrong_letters)
    print(f"\nHint: {hint}")
    print(f"Word: {masked}")
    print(f"Guessed letters: {' '.join(sorted(guessed.union(wrong_letters))) if guessed or wrong_letters else '(none)'}")
    print(f"Lives left: {'❤️' * lives_left}{'💔' * len(wrong_letters)}\n")

def get_guess(guessed, wrong_letters):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed or guess in wrong_letters:
            print("You already tried that letter. Try another.")
            continue
        return guess

def play():
    word, hint = choose_word()
    guessed = set()
    wrong_letters = set()

    while True:
        display_state(word, guessed, wrong_letters, hint)
        guess = get_guess(guessed, wrong_letters)

        if guess in word:
            guessed.add(guess)
            print("Correct guess!\n")
            if all(c in guessed for c in word):
                print(f"🎉 You win! The word was: {word}")
                break
        else:
            wrong_letters.add(guess)
            print(" Wrong guess!\n")
            if len(wrong_letters) >= MAX_WRONG:
                display_state(word, guessed, wrong_letters, hint)
                print(f"☠️ You lose! The word was: {word}")
                break

if __name__ == "__main__":
    print("=== Hangman Game ===")
    play()
