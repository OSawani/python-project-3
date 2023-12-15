# Functions used across the project. 
# This include input validation, error handling, and any other reusable code.

def validate_input(user_input, expected_type, range=None):
    """
    validates/checks if given user input matches
    the expected type and falls within an optional range.

    :param user_input: input to validate
    :param expected_type: type that the input is expected to be
    :param range: optional range (inclusive) for numeric inputs
    :return: (bool, any) tuple
            first element is a boolean indicates if input valid,
            second element is converted input or an error message.
    """
    try:
        # Convert input to expected type
        converted_input = expected_type(user_input)
        # Check if input is within the specified range
        if range and not (range[0] <= converted_input <= range[1]):
            return False, "Input is out of range."
        return True, converted_input
    except ValueError:
        return False, "Invalid input type."


def is_within_board(coordinates, board_size):
    """
    checks if given coordinates are within the bounds of the board.

    :param coordinates: A tuple (x, y) representing coordinates.
    :param board_size: The size of game board.
    :return: True if  coordinates are within board, False otherwise.
    """
    x, y = coordinates
    return 0 <= x < board_size and 0 <= y < board_size


def convert_to_coords(input_str):
    """
    converts input string like 'A5' into board coordinates.

    :param input_str: input string to convert.
    :return: (int, int) tuple representing the coordinates (x, y).
    :raises: ValueError if input format is invalid.
    """
    if len(input_str) != 2 or not input_str[0].isalpha() or not input_str[1].isdigit():
        raise ValueError("Invalid input format.")

    x = ord(input_str[0].upper()) - ord('A')
    # Convert letter to number (A -> 0, B -> 1, ...)
    y = int(input_str[1]) - 1
    # Convert 1-based index to 0-based
    return x, y
