class GameBoard:
    def __init__(self, size=8):
        """
        __init__ method sets up the board with a default size of 8x8.
        the board is represented as a list of lists, 
        with ~ indicating water.
        """
        self.size = size
        self.board = [["~" for _ in range(size)] for _ in range(size)]
        # loop runs size times.
        # _ a variable name
        # no intent to use the loop variable,
        # the loop variable index is not needed.

        #additional initialization
    
    def print_board(self):
        """
        prints the game board to the console,
        displays the current state of the board in the console.
        """
        for row in self.board:
            print("_**_".join(row))
        print() # Extra newline for better readability

    def place_ship(self, ship):
        """
        places a ship on the board,
        responsible for placing ships on the board.
        """
        pass

    def take_shot(self, coordinates):
        """
        handles shots taken by the player or computer,
        logic for shots taken.
        """
        pass   