class Jumper:
    """This class is for grafic representation of jumper has a matriz 
    that keep of characteres that are printed in the screen
   
    Attributes:
        characteres_matriz: Have the characters for print the jumper.
        oportunity: It have de number of times the user has try guess the 
                    character and he has failed
    """
    __board = [[None] * 7 for i in range(10)]
    __oportunity = 0
    def __init__(self):
        """Constructs a new instance of Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.__board = [[None] * 7 for i in range(10)]
        self.__oportunity = 0
        self.fill_board()
        
    def fill_board(self):
        """Fill the matrix with the characters that allow forming the parachutist (jumper)
        
        Args:
            self (Jumper): An instance of Jumper.
        """
        self.__board[0][0] = " "
        self.__board[0][1] = " "
        self.__board[0][2] = "_"
        self.__board[0][3] = "_"
        self.__board[0][4] = "_"
        self.__board[0][5] = " "
        self.__board[0][6] = " "
        self.__board[1][0] = " "
        self.__board[1][1] = "/"
        self.__board[1][2] = "_"
        self.__board[1][3] = "_"
        self.__board[1][4] = "_"
        self.__board[1][5] = "\\"
        self.__board[1][6] = " "
        self.__board[2][0] = " "
        self.__board[2][1] = "\\"
        self.__board[2][2] = " "
        self.__board[2][3] = " "
        self.__board[2][4] = " "
        self.__board[2][5] = "/"
        self.__board[2][6] = " "
        self.__board[3][0] = " "
        self.__board[3][1] = " "
        self.__board[3][2] = "\\"
        self.__board[3][3] = " "
        self.__board[3][4] = "/"
        self.__board[3][5] = " "
        self.__board[3][6] = " "
        self.__board[4][0] = " "
        self.__board[4][1] = " "
        self.__board[4][2] = " "
        self.__board[4][3] = "O"
        self.__board[4][4] = " "
        self.__board[4][5] = " "
        self.__board[4][6] = " "
        self.__board[5][0] = " "
        self.__board[5][1] = " "
        self.__board[5][2] = "/"
        self.__board[5][3] = "|"
        self.__board[5][4] = "\\"
        self.__board[5][5] = " "
        self.__board[5][6] = " "
        self.__board[6][0] = " "
        self.__board[6][1] = " "
        self.__board[6][2] = "/"
        self.__board[6][3] = " "
        self.__board[6][4] = "\\"
        self.__board[6][5] = " "
        self.__board[6][6] = " "
        self.__board[7][0] = " "
        self.__board[7][1] = " "
        self.__board[7][2] = " "
        self.__board[7][3] = " "
        self.__board[7][4] = " "
        self.__board[7][5] = " "
        self.__board[7][6] = " "
        self.__board[8][0] = " "
        self.__board[8][1] = " "
        self.__board[8][2] = " "
        self.__board[8][3] = " "
        self.__board[8][4] = " "
        self.__board[8][5] = " "
        self.__board[8][6] = " "
        self.__board[9][0] = "^"
        self.__board[9][1] = "^"
        self.__board[9][2] = "^"
        self.__board[9][3] = "^"
        self.__board[9][4] = "^"
        self.__board[9][5] = "^"
        self.__board[9][6] = "^"
    
    def draw_jumper(self):
        """ Draw by means of characters the skydiver (jumper) on the screen
        Args:
            self (Jumper): An instance of Jumper.

        """

        for i in range(10):
            for j in range(7):
                character = self.__board[i][j]
                print(f"{character}",end="")
            print()

    def rest_oportunities(self,letter_found):
        """ This method decreases the number of opportunities to enter characters 
            and thus the user guesses the word, increasing the possibilities counter,
            to a maximum of 5, which is the limit of attempts.
        Args:
            self (Jumper): An instance of Jumper.

        """
        if(letter_found==False):
            if(self.__oportunity == 4):
                self.__board[self.__oportunity][3] = "x"
            else:
                for i in range(7):
                    self.__board[self.__oportunity][i] = " "
            self.__oportunity +=1
        