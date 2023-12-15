class GameBoard:
    def __init__(self, size=8):
        """
        sets up board with a default size of 8x8.
        board is represented as a list of lists, 
        with ~ indicating water.

        :param size: The size of the board (size x size).
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

        :param reveal_ships: If True, ships will be revealed on board.
        """
        print() # Extra newline for better readability
        print("\033[0m")  # Reset to default color at the end
        print("\n+" + "-" * (self.size * 2 + 1) + "+")
        # Top border
        for row in self.board:
            colored_row = ""
            for cell in row:
                if cell == 'H':
                    colored_row += "\033[91mX\033[0m "
                    # Red for hits
                elif cell == 'M':
                    colored_row += "\033[94mO\033[0m "
                    # Blue for misses
                elif reveal_ships and cell == 'S':
                    colored_row += "\033[92mS\033[0m "
                    # Green for ships
                else:
                    colored_row += "~ "
            print("| " + colored_row + "|")
            # Add left and right borders
        print("+" + "-" * (self.size * 2 + 1) + "+\n")
        # Bottom border
        print() # Extra newline for better readability


    def place_ship(self, ship, position, horizontal):
        """
        places a ship on the board:
        checks if placement is valid,
        updates ship's positions
        marks ship on the board.

        :param ship: The ship object to be placed.
        :param position: The starting position (tuple) for ship.
        :param horizontal: Orientation of ship. True for horizontal.
        :return: True if ship was placed successfully, False otherwise.
        """
        if self.is_valid_placement(ship, position, horizontal):
            ship.place(position, horizontal)
            self.ships.append(ship)
            # Update board with ship's position for internal tracking
            # Not visible to player
            for x, y in ship.positions:
                self.board[x][y] = 'S'
                # Ships marked on the board but not visible to the player
            return True
        else:
            return False

    
        
    def is_valid_placement(self, ship, position, horizontal):
        """
        checks if ship placement is within board boundaries
        without overlapping.

        :param ship: The ship to be placed.
        :param position: The starting position (tuple) for ship.
        :param horizontal: Orientation of ship.
        :return: True if the placement is valid, False otherwise.
        """
        x, y = position
        for i in range(ship.size):
            x = position[0] + i if horizontal else position[0]
            y = position[1] if horizontal else position[1] + i
            if x >= self.size or y >= self.size or self.board[x][y] != "~":
                return False
        return True


    def take_shot(self, coordinates):
        """
        handles shooting at a coordinate:
        updates the board based on the shot's coordinates.
        checks if shot is a hit/miss and marks board with 'H'(hit)/'M'(miss).
        prevents shooting at the same location more than once.

        :param coordinates: The coordinates (tuple) to take a shot at.
        :return: Result of the shot - "Hit", "Miss", or "Already hit".
        """
        x, y = coordinates
        if self.board[x][y] in ["H", "M"]:
            return "Already hit"
        
        hit = any(ship for ship in self.ships if coordinates in ship.positions)
        if hit:
            self.board[x][y] = "H"
            self.update_ship_hit(coordinates)
            return "Hit!"
        else:
            self.board[x][y] = "M"
            return "Miss"
    

    def update_ship_hit(self, coordinates):
        """
        updates ship's status when hit's confirmed.
        calls take_hit on the ship and checks if the ship is sunk.
        """
        for ship in self.ships:
            if coordinates in ship.positions:
                ship.take_hit()
                if ship.is_sunk():
                    return f"{ship.name} sunk!"


    def is_game_over(self):
        return all(ship.is_sunk() for ship in self.ships)