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
        print('\n\n\n')
        print(' ' * 20, boarder)
        print(' ' * 20, welcome)
        print(' ' * 20, boarder)
        print('\n\n\n\n')

    def start(self):
        self.welcome()
        while not self.active_phrase.check_complete(self.guesses):
            self.active_phrase.display(self.guesses)
            print('\n')
            print(f'Number missed:  {self.missed}')
            print('\n')
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        if self.active_phrase.check_complete(self.guesses):
            print(f"Congratz! You won!! And only missed {self.missed}!")
        else:
            print('Better luck next time!')

    def get_guess(self):
        user_guess = input('Guess a letter: ')
        return user_guess

    
    
    