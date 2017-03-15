class Board:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''  # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'  # add one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # add hyphens for bottom edge
        # twice as many since above code included self.slots
        for col in range(2 * self.width + 1):
            s += '-'

        s += '\n'

        # add column numbers below bottom edge
        num = 0
        for col in range(self.width):
            s += ' ' + str(num)
            num += 1
            num = num % 10

        return s

    def add_checker(self, checker, col):
        """ adds the specified checker to column col
            of the called Board object
        """
        # verify inputs
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while self.slots[row][col] == ' ' and row < self.height - 1:
            row += 1

        if self.slots[row][col] != ' ': # we stopped at a checker
            self.slots[row - 1][col] = checker
        else:                           # row is the bottom slot of col
            self.slots[row][col] = checker

    def reset(self):
        """ resets the Board object on which it
            is called by setting all slots to contain a space character.
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker
            in the column col on the calling Board object, otherwise False
        """
        if col >= self.width:
            return False

        if col < 0:
            return False

        # if the top row is not empty, the column is full
        if self.slots[0][col] != ' ':
            return False
        
        return True

    def is_full(self):
        """ returns True if the called Board object is completely
            full of checkers, and returns False otherwise.
        """
        col = 0
        while not self.can_add_to(col) and col < self.width:
            col += 1

        # if we kept going til the last column, the board is full
        # and col is out of range of self.slots
        if col == self.width:
            return True
        
        return False

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object
        """
        row = 0

        # if col is full, remove checker from top-most space in col
        if not self.can_add_to(col):
            self.slots[row][col] = ' '

        else:
            # if we can add to the col and the bottom row in col
            # is empty, return since the col is already empty
            if self.slots[self.height - 1][col] == ' ':
                return

            while self.slots[row][col] == ' ' and row < self.height - 1:
                row += 1
                
            self.slots[row][col] = ' '

        return

    def is_win_for(self, checker):
        """ calls helper functions that determine all possible ways to win Connect
            Four and returns if the input checker is the winner of the game (True)
            or not (False)
        """
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
        horiz = self.is_horizontal_win(checker)
        vert = self.is_vertical_win(checker)
        ddiag = self.is_down_diagonal_win(checker)
        udiag = self.is_up_diagonal_win(checker)

        return horiz or vert or ddiag or udiag

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four rows in this column
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns and rows (diagonal)
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no down diagonal wins
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next four columns and last rows (diagonal)
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no down diagonal wins
        return False
