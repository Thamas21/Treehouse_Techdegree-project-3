# Create your Game class logic in here.
import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = [" "]

    def create_phrase(self, phrase):
        self.phrases.append(phrase)

    def __iter__(self, phrase):
        self.phrases

    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        print(random_phrase)

    def __str__(self):
        return f'{self.phrases}'.format()


if __name__ == "__main__":
    phrase_one = Phrase("Beautiful is better than ugly")
    phrase_two = Phrase("Explicit is better than implicit")
    phrase_three = Phrase("Simple is better than complex")
    game = Game()
    game.create_phrase(phrase_one)
    game.create_phrase(phrase_two)
    game.create_phrase(phrase_three)
    game.get_random_phrase()
