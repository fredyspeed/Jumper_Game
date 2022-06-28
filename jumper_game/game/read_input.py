
class Read_Input:
    """This class is for read input, the letter that the user 
    type trying to guess the word 
   
    Attributes:
        letter : Contains the letter input for the user
    """

    def __init__(self):
        self.letter = "" 

    def get_letter(self):
        return self.letter

        

    def read_letter(self):
        self.letter = input("Guess a letter [a-z]: ")
        if(self.valid_letter()):
            self.letter = self.letter.lower()
        else:
            self.read_letter()

    
    def valid_letter(self):
        if(self.letter.isalpha()):
            if(len(self.letter)==1):
                return True
            else:
                print("not is a value valid try again")
        else:
            print("not is a letter")
        return False
        
