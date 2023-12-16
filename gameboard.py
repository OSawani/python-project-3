from utils import is_within_board, typing_effect

class GameBoard:
    def __init__(self, size=8):
        """
        sets up board with a default size of 8x8.
        board is represented as a list of lists, 
        with ~ indicating water.

        :param size: The size of the board (size x size).
        """
        self.size = size
        self.board = [["-" for _ in range(size)] for _ in range(size)]
        self.ships = []
        # loop runs size times.
        # _ a variable name
        # no intent to use the loop variable,
        # the loop variable index is not needed.

        #additional initialization

    def print_board(self, reveal_ships=False):
        """
        prints the game board to the console,
        displays the current state of the board in the console.
        
        :param reveal_ships: If True, ships will be revealed on board.
        """
        color_reset = "\033[0m"
        color_row = "\033[95m"  # Magenta for row letters
        color_column = "\033[96m"  # Cyan for column numbers
        color_line = "\033[93m"    # Yellow for the horizontal line
        # Define the colors

        board_content = []
        # Prepare the board content with padding

        for i, row in enumerate(self.board, start=1):
            row_str = ' | '.join(
                "\033[91mX\033[0m" if cell == 'H' else
                "\033[94mO\033[0m" if cell == 'M' else
                "\033[92mS\033[0m" if reveal_ships and cell == 'S' else "-"
                for cell in row
            )
            row_letter = f"{color_row}{chr(65 + i - 1)}{color_reset}"
            # Convert number to letter
            board_content.append(f"{row_letter} | {row_str} | {row_letter}")

        line_length = 4 * self.size + 3  # Length of line based on the board size
        horizontal_padding = (80 - line_length) // 2  # Padding each side centers line
        # Calculate padding for the horizontal line

        column_numbers = '   '.join([f"{color_column}{str(i + 1)}{color_reset}" for i in range(self.size)])
        print(' ' * (horizontal_padding + 1) + '   ' + column_numbers)
        # Print the top column numbers (1, 2, 3, ...)

        print(' ' * horizontal_padding + color_line + '+' + '-' * (line_length - 2) + '+' + color_reset)
        # Print the board content with horizontal lines
        for line in board_content:
            typing_effect(' ' * horizontal_padding + line, speed = 0.008)
            print(' ' * horizontal_padding + color_line + '+' + '-' * (line_length - 2) + '+' + color_reset)

        print(' ' * (horizontal_padding + 1) + '   ' + column_numbers)
        # Print the bottom column numbers again
        print()  # Extra newline for better readability


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
            if x >= self.size or y >= self.size or self.board[x][y] != "-":
                return False
        return True


    def update_ship_hit(self, coordinates):
        """
        updates ship's status when hit's confirmed.
        calls take_hit on the ship and checks if the ship is sunk.
        """
        for ship in self.ships:
            if coordinates in ship.positions:
                if coordinates in ship.hit_positions:
                    return "Part already hit"
                    # Check if the part of the ship has already been hit
                else:
                    ship.take_hit(coordinates)
                    if ship.is_sunk():
                        return f"{ship.name} sunk!"
                        # If the ship is hit but not sunk
                    else:
                        return f"{ship.name} hit!"
        return ""
        # Return an empty string if no ship was hit
        

    def take_shot(self, coordinates):
        """
        handles shooting at a coordinate:
        updates the board based on the shot's coordinates.
        checks if shot is a hit/miss and marks board with 'H'(hit)/'M'(miss).
        prevents shooting at the same location more than once.

        :param coordinates: The coordinates (tuple) to take a shot at.
        :return: Result of the shot - "Hit", "Miss", or "Already hit".
        """
        if not is_within_board(coordinates, self.size):
            return "Coordinates out of range"

        x, y = coordinates
        if self.board[x][y] in ["H", "M"]:
            return "Already hit"
        
        hit_ship_info = self.update_ship_hit(coordinates)
        if "hit" in hit_ship_info or "sunk" in hit_ship_info:
            self.board[x][y] = "H"
            return "Hit!"
        else:
            self.board[x][y] = "M"
            return "Miss"
    


    def is_game_over(self):
        return all(ship.is_sunk() for ship in self.ships)