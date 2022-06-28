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
        self.shots_fails = 0
        self.SHOT_FAIL_MAX = 5
        self.number_found_letter = 0
        self.guess_word = False
        self.letters_guess = [" "," "," "," "," "]
        
    def increase_shots_fails(self):
        self.shots_fails +=1
    
    def increase_letters_found(self):
        self.number_found_letter +=1

    def verific_finish_game(self,word):
        game_finish = False
        if (self.number_found_letter == 5):
            print(f" Congratulations you find the word!")
            game_finish = True
        elif(self.shots_fails==5):
            print(f"You don't guess the word this was: {word}")
            game_finish = True
        
        return game_finish

    def get_letters_guess(self):
        return self.letters_guess   

    def compare_letter_input(self,word,letter):
        found = False
        for i in range (self.SHOT_FAIL_MAX):
            if(self.letters_guess[i]==" "):
                if(word[i]==letter):
                    self.increase_letters_found()
                    self.letters_guess[i]=letter
                    found = True
        if(found == False):
            self.increase_shots_fails()
        return found

    def letters_found(self):
        for i in range(5):
            if (self.letters_guess[i]==" "):
                print("_ ",end="")
            else:
                print(f"{self.letters_guess[i]} ",end="")
        print()
        