# Functions used across the project. 
# This include input validation, error handling, and any other reusable code.

import sys 
import time 

def display_game_instructions():
    """
    displays game instructions with a border
    waits for the user to continue.
    """
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    width = 70  # Set the width for the instructions and border

    def center_text(text, symbol=' '):
        return f"{text.center(width, symbol)}"
    # Function to create centered text with the specified width

    border_line = center_text("+", "-")
    # Create the border lines

    instructions = [
        " ",
        "Welcome to Battleship!",
        "The game is played on two grids, one for each player.",
        "The grids are square, 5X5 for easy, 8X8 for Hard.",
        "Each square is identified by letter and number.",
        "On the enemy's grid, you track your own shots.",
        " ",
        "Before play, the game randomly arranges ships for both players.",
        "Ships occupy consecutive squares, arranged horizontally/vertically.",
        "Ships cannot overlap. After positioning, the game proceeds in rounds.",
        "Players take turns announcing a target square to shoot at.",
        "If all your ships are sunk, the game ends and the opponent wins.",
        " ",
        "Press 'y' to start the game or 'n' to return to main menu"
    ]

    typing_effect(border_line, speed=0.007)
    typing_effect(center_text("B A T T L E S H I P S", ' '), end='|\n', speed = 0.01)
    # Print the top border


    for line in instructions:
        typing_effect(green_color_code + center_text(line) + reset_color_code, end='|\n', speed=0.01)
    # Print each line of the instructions

    typing_effect(border_line, speed = 0.007)
    # Print the bottom border

    while True:
        user_input = input().strip().lower()
        if user_input == 'y':
            return 'continue'
        elif user_input == 'n':
            return 'quit'
        else:
            typing_effect("Please press 'y' to start the game or 'n' to return to the main menu." + reset_color_code)
    # Wait for user input to continue


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


def typing_effect(text, end="\n", speed=0.05):
    """
    simulates typing effect for given text.

    :param text: The text to be printed with typing effect.
    :param speed: Delay between each character (lower is faster).
    :param end: to control the end character after the text effect.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(end=end, flush=True)  # Move to the next line after finishing


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
