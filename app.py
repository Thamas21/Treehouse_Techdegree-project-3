# Import your Game class
import random

from phrasehunter import game
from phrasehunter import phrase


# Create your Dunder Main statement.

# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop
if __name__ == "__main__":
    game = game.Game()
    phrase_one = phrase.Phrase("Special cases aren't special enough to break the rules")
    phrase_two = phrase.Phrase("Beautiful is better than ugly")
    phrase_three = phrase.Phrase("Explicit is better than implicit")
    phrase_four = phrase.Phrase("Simple is better than complex")
    game.create_phrase(phrase_one)
    game.create_phrase(phrase_two)
    game.create_phrase(phrase_three)
    for word in game:
        print(word)
