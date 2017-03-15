from ConnectFour_BoardClass import Board

class Player:

    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object
        """
        return "Player " + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing
            the checker of the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        
        return 'X'

    def next_move(self, board):
        """ returns the column where the player wants to make the next move.
            accepts a Board object as a parameter
        """
        while True:
            col = int(input("Enter a column: "))
            if board.can_add_to(col):
                break
            else:
                print("Try again!")
        
        self.num_moves += 1
        return col
