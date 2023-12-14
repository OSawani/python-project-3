#Ship class represent real world entity ship
#Ship class has attributes: size, name.
#Ship has methods/functions to track positions & determine status.

class Ship:
    """
    represents the different types of ships in the game, 
    attributes: size, position, and status (hit or not).
    """
    def __init__(self, name, size):
        """"
        sets ship's name & size.
        initialises positions.
        initialises list & hit counter.
        """
        self.name = name
        self.size = size
        self.positions = [] 
        # List of tuples(x, y) for each ship segment
        self.hits = 0 
        # Number of hits the ship has taken

    def place(self, start_position, horizontal = True):
        """
        takes a start position & orientation (horizontal/vertical).
        calculates ship's positions on board.
        """
        self.positions = [(start_position[0] + i if horizontal else start_position[0], 
                           start_position[1] if horizontal else start_position[1] + i) 
                          for i in range(self.size)]


    def is_sunk(self):
        """
        returns True if ship has been hit enough times to sink.
        """
        return self.hits >= self.size

    def take_hit(self):
        """
        increments hit counter when ship is hit.
        """
        self.hits += 1
