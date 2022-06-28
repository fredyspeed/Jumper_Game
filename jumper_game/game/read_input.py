
class Read_Input:
    """This class is for read input, the letter that the user 
    type trying to guess the word 
   
    Attributes:
        letter : Contains the letter input for the user
    """
    __letter = None

    def __init__(self):
        self.__letter = "" 

    def get_letter(self):
        return self.__letter

        

    def read_letter(self):
        """This method obtains from the input standard the letter entered by the user,
        and assigns the private attribute _ letter
        
        Args:
            self (Read_Input): An instance of Read_Input.

        """
        self.__letter = input("Guess a letter [a-z]: ")
        if(self.valid_letter()):
            self.letter = self.__letter.lower()
        else:
            self.read_letter()

    
    def valid_letter(self):
        """ It validates if the input made by the user is a letter of the alphabet, 
        and returns true or false as the case may be.
        Args:
            self (Read_Input): An instance of Read_Input.

        Returns:
            True if the attribute private __letter is a 
            letter of the alphabet and has one character or False in another case
        """
        if(self.__letter.isalpha()):
            if(len(self.__letter)==1):
                return True
            else:
                print("not is a value valid try again")
        else:
            print("not is a letter")
        return False
        
