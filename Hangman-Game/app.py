import random

def select_random_word(word_list):
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print('Current word:', displayed_word)

def get_user_guess(guessed_letters):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif not guess.isalpha():
            print('Please enter a valid letter.')
        elif guess in guessed_letters:
            print('You have already guessed that letter. Try again.')
        else:
            return guess

def hangman():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']
    max_incorrect_guesses = 6
    
    while True:
        word = select_random_word(word_list)
        guessed_letters = set()
        incorrect_guesses = 0
        guessed_word = False
        
        print('\nWelcome to Hangman!')
        
        while incorrect_guesses < max_incorrect_guesses and not guessed_word:
            display_current_state(word, guessed_letters)
            print(f'Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}')
            
            guess = get_user_guess(guessed_letters)
            guessed_letters.add(guess)
            
            if guess in word:
                print(f'Good guess! {guess} is in the word.')
            else:
                print(f'Sorry, {guess} is not in the word.')
                incorrect_guesses += 1
            
            guessed_word = all(letter in guessed_letters for letter in word)
        
        if guessed_word:
            print(f'Congratulations! You guessed the word: {word}')
        else:
            print(f'Sorry, you ran out of guesses. The word was: {word}')
        
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            break

if __name__ == '__main__':
    hangman()
