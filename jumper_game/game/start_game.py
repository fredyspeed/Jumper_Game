from game.jumper import Jumper
from game.read_input import Read_Input
from game.list_of_words import ListOfWords
from game.game_logic import GameLogic

class StartGame:
    """This class is for call the methods of each class for execut the game
   
    Attributes:
        finish:is a boolean value that is initialized with False and when the word is guessed or
        the number of attempts is completed,
        the execution of the program ends.
        
    """
    __finish = None

    def __init__(self):
        """Initializes the private finish attribute to False .
   
            Args:
            self (StartGame): An instance of StartGame.
        """
        self.__finish = False
        
    def start_now(self):
        """This method controls the execution of the game, 
        and finalizes when the user guesses the word or the 
        number of attempts is completed
   
            Args:
            self (StartGame): An instance of StartGame.
        """
        jumper = Jumper()
        list_of_words = ListOfWords()
        read_input = Read_Input()
        game_logic = GameLogic()
        word = list_of_words.value_ramdom()
        jumper.draw_jumper()
        while self.__finish == False:
            
            read_input.read_letter()
            letter = read_input.get_letter()
            result = game_logic.compare_letter_input(word,letter)
            #word_letters_guess = game_logic.get_letters_guess()
            jumper.rest_oportunities(result)
            game_logic.letters_found()
            jumper.draw_jumper()
            self.__finish = game_logic.verific_finish_game(word)
            







    
