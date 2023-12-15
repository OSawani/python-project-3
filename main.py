# Serves as entry point for game. 
# Sets up main loop and calls main menu.
# Connects main menu options with corresponding game actions:
# 1.starting a new game, 2.changing difficulty, 3.viewing the leaderboard.

import random
from utils import validate_input, typing_effect, convert_to_coords, is_within_board
from gameboard import GameBoard
from ship import Ship
from leaderboard import Leaderboard

global_leaderboard = Leaderboard()
# Global leaderboard instance

def display_main_menu():
    """
    displays the main menu options and handles user input.
    returns a valid choice as an integer.
    """
    while True:
        print("\n" + "=" * 28)
        print("||    BATTLESHIP GAME    ||")
        print("=" * 28)
        print("1. Start New Game")
        print("2. Change Difficulty")
        print("3. View Leaderboard")
        print("4. Quit")
        print("=" * 28 + "\n")
        
        choice = input("Enter your choice (1-4): \n")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 4")



def start_new_game(difficulty, leaderboard):
    """
    initializes a new game with current difficulty.
    creates a GameBoard instance based on difficulty,
    handles random ship placement & game progression.
    """
    print(f"Starting a new game with difficulty: {difficulty}")
    board_size = 8 if difficulty == 'Easy' else 5
    game_board = GameBoard(size = board_size)
    
    ships = [Ship("Battleship", 4), Ship("Cruiser", 3), 
            Ship("Submarine", 3), Ship("Destroyer", 2), 
            Ship("Patrol Boat", 1)]
    # Define ships

    for ship in ships:
        placed = False
        while not placed:
            x = random.randint(0, board_size -1)
            y = random.randint(0, board_size -1)
            horizontal = random.choice([True, False])
            placed = game_board.place_ship(ship, (x, y), horizontal)
            # Generate ranom position & orientation
    # Automatically place ships on board

    typing_effect("Game started! Here's your board:")
    game_board.print_board(reveal_ships = True)
    
    # Continues until the game is over, 
    # Alternating between player turns 
    # and a placeholder for the computer's turn.
    while not game_board.is_game_over():
        player_turn(game_board)
    # Checks after each turn if the game is over.  
    # If all ships of player/computer are sunk, 
    # Game ends!
        if game_board.is_game_over():
            print("Congratulations! You won!")
            update_leaderboard(leaderboard, True)
            break

        computer_turn(game_board)
        if game_board.is_game_over():
            print("Sorry, the computer won this time.")
            update_leaderboard(leaderboard, False)
            break

        game_board.print_board(reveal_ships=False)

    print("Game over! Here's the final board:")
    game_board.print_board(reveal_ships = True)


def change_difficulty():
    """
    allows player to change the game's difficulty level.
    presents player with two difficulty options.
    player's choice determines the size of board used in the new game.
    returns chosen difficulty as string.
    """
    while True: 
        print("\nSelect Difficulty:")
        print("1. Easy! (8x8 Board for both player & computer.)")
        print("2. Hard! (5x5 Board for player, 8x8 for computer!)")

        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Hard"
        else:
            print("Invalid choice. Please try again.")
    # Return a new difficulty value based on user choice


def view_leaderboard():
    """
    displays the current leaderboard

    :param leaderboard: Leaderboard class instance to display.
    """
    global global_leaderboard
    global_leaderboard.display_leaderboard()


def player_turn(game_board):
    """
    handles player's turn to guess & attack a coordinate.
    allows player to input coordinates for an attack,
    handles the shot logic.
    """
    while True:
        try:
            input_coords = input("Enter coordinates to attack (e.g., 'A5'): ")
            x, y = convert_to_coords(input_coords)
             # Convert input to board coordinates
            if not is_within_board((x, y), game_board.size):
                print("Coordinates out of range. Please try again.")
                continue
            result = game_board.take_shot((x, y))
            print(result)
            if result not in ["Already hit", "Coordinates out of range"]:
                break
        except ValueError as e:
            print(e)
        # Improved input handling


def computer_turn(game_board):
    """
    Handles the computer's turn to guess and attack a coordinate.
    enables the computer to randomly choose a target,
    ensures the computer does not attack a previously hit coordinate.
    """
    while True:
        x = random.randint(0, game_board.size - 1)
        y = random.randint(0, game_board.size - 1)
        result = game_board.take_shot((x, y))
        if result != "Already hit":
            print(f"Computer attacked {chr(65 + x)}{y + 1} and {result}")
            break


def update_leaderboard(leaderboard, player_won):
    """
    updates the leaderboard based on game outcome
    """
    player_name = "Player"
    # Placeholder for player's name
    leaderboard.update_score(player_name, player_won)


def main():
    """
    main game loop.
    """
    current_difficulty = "Easy" 
    # Default difficulty
    

    while True:
        choice = display_main_menu()
        
        if choice == 1:
            print("Starting a new game...")
            start_new_game(current_difficulty, global_leaderboard)
        elif choice == 2:
            print("Changing difficulty...")
            current_difficulty = change_difficulty()
        elif choice == 3:
            print("Displaying leaderboard...")
            view_leaderboard()
        elif choice == 4:
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# runs if directly called only
# allows script to be imported in other py files
# without automatically running the game. 
# for reuse of functions/classes in other scripts.