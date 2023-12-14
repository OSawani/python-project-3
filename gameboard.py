class GameBoard:
    def __init__(self, size=8):
        """
        sets up board with a default size of 8x8.
        board is represented as a list of lists, 
        with ~ indicating water.
        """
        self.size = size
        self.board = [["~" for _ in range(size)] for _ in range(size)]
        self.ships = []
        # loop runs size times.
        # _ a variable name
        # no intent to use the loop variable,
        # the loop variable index is not needed.

        #additional initialization
    
    def print_board(self, reveal_ships = False):
        """
        prints the game board to the console,
        displays the current state of the board in the console.
        """
        for row in self.board:
            print("_**_".join(row))
        print() # Extra newline for better readability


    def place_ship(self, ship, position, horizontal):
        """
        places a ship on the board:
        checks if placement is valid,
        updates ship's positions
        marks ship on the board.
        """
        if self.is_valid_placement(ship, position, horizontal):
            ship.place(position, horizontal)
            self.ships.append(ship)
            # Update board with ship's position
            for x, y in ship.positions:
                self.board[x][y] = 'S' if reveal_ships else '~'
            return True
        else:
            return False

    
        
    def is_valid_placement(self, ship, position, horizontal):
        """
        checks if ship placement is within board boundaries
        without overlapping.
        """
        for i in range(ship.size):
            x = position[0] + i if horizontal else position[0]
            y = position[1] if horizontal else position[1] + i
            if x >= self.size or y >= self.size or self.board[x][y] != "~"
                return False
        return True


    def take_shot(self, coordinates):
        """
        handles shots taken by the player or computer,
        logic for shots taken.
        """
        pass   