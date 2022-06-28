from game.list_of_words import ListOfWords

class GameLogic:
    """This class is which controling the logic of the game
   
    Attributes:
        shots_fails: is the number the input where the letter is not in the word
        SHOT_FAIL_MAX: Maximum number of attempts
        number_found_letter: Is the number of letters found
        guess_letter: Inicial have false and only change is the word is guess
    """
    
    def __init__(self):
        """Constructs a new instance of GameLogic.

        Args:
            self (GameLogic): An instance of GameLogic.
        """
        self.__shots_fails = 0
        self.__SHOT_FAIL_MAX = 5
        self.__number_found_letter = 0
        self.__guess_word = False
        self.__letters_guess = [" "," "," "," "," "]
        
    def increase_shots_fails(self):
        """This method increases the number or value of the private attribute __shots_fails
   
            Args:
            self (GameLogic): An instance of GameLogic.
        """
        self.__shots_fails +=1
    
    def increase_letters_found(self):
        """This method increases the number or value of the private attribute __number_found_letter
   
            Args:
            self (GameLogic): An instance of GameLogic.
        """
        self.__number_found_letter +=1

    def verific_finish_game(self,word):
        """ This method checks if the game is over, i.e. if the word was guessed or
            the number of tries is over, prints Congratulations in case the word is 
            found or prints You did not guess the word
   
            Args:
                self (GameLogic): An instance of GameLogic.

            Returns:
                True or false 

        """
        game_finish = False
        if (self.__number_found_letter == 5):
            print(f" Congratulations you find the word!")
            game_finish = True
        elif(self.__shots_fails == 5):
            print(f"You did not guess the word, this was: {word}")
            game_finish = True
        
        return game_finish

    def get_letters_guess(self):
        """This method returns the state of the attribute __letter_guess list
            Args:
                self (GameLogic): An instance of GameLogic.
            Returns:
                List: __letters_guess
        """
        return self.__letters_guess   

    def compare_letter_input(self,word,letter):
        found = False
        for i in range (self.__SHOT_FAIL_MAX):
            if(self.__letters_guess[i]==" "):
                if(word[i]==letter):
                    self.increase_letters_found()
                    self.__letters_guess[i]=letter
                    found = True
        if(found == False):
            self.increase_shots_fails()
        return found

    def letters_found(self):
        for i in range(5):
            if (self.__letters_guess[i]==" "):
                print("_ ",end="")
            else:
                print(f"{self.__letters_guess[i]} ",end="")
        print()
        