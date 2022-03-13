
class Phrase:

    def __init__(self, phrase):

        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter == ' ':
                print(' ', end=' ')
            elif letter in guesses:
                print(f'{letter}', end="")
            else:
                print("_", end=" ")

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        game_over = all(letter in guesses for letter in self.phrase)
        if game_over:
            return True
