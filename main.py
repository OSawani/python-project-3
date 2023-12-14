# Serves as entry point for game. 
# Sets up main loop and calls main menu.
# Connects main menu options with corresponding game actions:
# 1.starting a new game, 2.changing difficulty, 3.viewing the leaderboard.

import random
from gameboard import GameBoard
from ship import Ship
from leaderboard import Leaderboard

global_leaderboard = Leaderboard()
# Global leaderboard instance

def display_main_menu():
    """
    Displays the main menu options and handles user input.
    Returns a valid choice as an integer.
    """
    print("\n" + "=" * 28)
    print("||    BATTLESHIP GAME    ||")
    print("=" * 28)
    print("1. Start New Game")
    print("2. Change Difficulty")
    print("3. View Leaderboard")
    print("4. Quit")
    print("=" * 28 + "\n")

    choice = input("Enter your choice (1-4): \n")
    return choice


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
    displays the leaderboard
    """
    leaderboard.display_leaderboard()


def start_new_game(difficulty):
    """
    initializes a new game with current difficulty.
    creates a GameBoard instance based on difficulty,
    handles random ship placement & game progression.
    """
    print(f"Starting a new game with difficulty: {difficulty}")
    board_size = 8 if difficulty == 'Easy' else 5
    game_board = GameBoard(size = board_size)
    
    ships = [Ship("Battleship", 4), Ship("Cruiser, 3"),
            Ship("Submarine", 3), ("Destroyer", 2), Ship("Patrol Boat", 1)]
    # Define ships

    for ship in ships:
        placed = False
        while not placed:
            x = radnom.randint(0, board_size -1)
            y = random.randint(0, board_size -1)
            horizontal = random.choice([True, False])
            placed = game_board.place_ship(ship, (x, y), horizontal)
            # Generate ranom position & orientation
    # Automatically place ships on board

    print("Game started! Here's your board:")


def main():
    """
    The main game loop.
    """
    current_difficulty = "Easy" 
    global_leaderboard = Leaderboard()
    # Default difficulty

    while True:
        choice = display_main_menu()
        
        if choice == '1':
            print("Starting a new game...")
            start_new_game(current_difficulty, global_leaderboard)
        elif choice == '2':
            print("Changing difficulty...")
            current_difficulty = change_difficulty()
        elif choice == '3':
            print("Displaying leaderboard...")
            view_leaderboard(global_leaderboard)
        elif choice == '4':
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