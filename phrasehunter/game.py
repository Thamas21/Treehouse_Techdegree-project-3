# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random
class Game:
    
    def __init__(self):
        
        self.missed = 0
        self.phrases = [
        Phrase("Beautiful is better than ugly"),
        Phrase("Explicit is better than implicit"),
        Phrase("Simple is better than complex"),
        Phrase("Complex is better than complicated"),
        Phrase("Flat is better than nested")
            
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
    

    def get_random_phrase(self):
        phrase = random.choice(self.phrases)
        return phrase


    def welcome(self):
        welcome = 'Welcome to Phrase Hunter'
        boarder = '=' * len(welcome)
        print('\n' * 3)
        print(' ' * 20, boarder)
        print(' ' * 20, welcome)
        print(' ' * 20, boarder)
        print('\n' * 2)

    def start(self):
        #self.welcome()
        while not self.active_phrase.check_complete(self.guesses):
            self.active_phrase.display(self.guesses)
            print('\n')
            print(f'Number missed:  {self.missed}')
            print('\n')
            user_guess = self.get_guess()
            if self.missed > 4:
                return False
                break
        if self.active_phrase.check_complete(self.guesses):
            print(f"Congratz! You won!! And only missed {self.missed}!")
            
        else:
            print('Better luck next time!')
        
    def get_guess(self):
        user_guess = input('Guess a letter: ').lower()
        if not user_guess.isalpha():
            print('Letters only please!')
            print('\n')
            self.missed += 1
        elif len(user_guess) >= 2:
            print('Easy there tiger! One letter at a time.')
            print('\n')
            self.missed += 1
        elif user_guess in self.guesses:
            print("You've already guessed that")
            self.missed += 1
        elif user_guess not in self.active_phrase.phrase:
            print("The phrase doesn't contain that letter.")
            self.missed += 1
        else:
            self.guesses.append(user_guess)
        return user_guess

    
    def play_phrasehunter(self):
        play_again = ' '
        while True:
            self.start()
            play_again = input('Do you want to play again? yes/no: ').upper()
            if play_again == 'Y' or play_again == 'YES':
                self.missed = 0
                self.guesses = [" "]
                self.active_phrase = self.get_random_phrase()
                self.start()
            else:
                return False

    
    