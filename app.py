# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase




if __name__ == "__main__":
    game = Game()
    #print('\n')
    #print(game.active_phrase.phrase) 
    #print('\n')
    #game.active_phrase.display(game.guesses)
    #print('\n')
    print(game.active_phrase.phrase)
    game.start()
  

   
   

   
# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop

    
    
