from ConnectFour_BoardClass import Board
from ConnectFour_PlayerClass import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    # create a board of default width and height for the player objects to play on
    board = Board(6, 7)
    print(board)
    
    # while we can process the move made, print the board allowing for the players
    # to see the current board object so they can determine their next move
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
    """ takes two parameters: a Player object for the player whose move is being
        processed, and a Board object for the game that is being played
        processes a single move by specified player on specified board
    """
    print("%s's turn" % (player))
    next_col = player.next_move(board)
    board.add_checker(player.checker, next_col)
    print('\n%s' % (board))
    if board.is_win_for(player.checker):
        print(player, "wins in", player.num_moves, "moves.")
        print("Congratulations!")
        return True
    
    if board.is_full():
        print("It's a tie!")
        return True

    return False

if __name__ == "__main__":
    connect_four(Player('X'), Player('O'))
