# Serves as entry point for game. 
# Sets up main loop and calls main menu.
# Connects main menu options with corresponding game actions:
# 1.starting a new game, 2.changing difficulty, 3.viewing the leaderboard.

import random
from utils import display_game_instructions, validate_input, typing_effect, convert_to_coords, is_within_board
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
        typing_effect("||    BATTLESHIP GAME    ||", speed = 0.01)
        print("=" * 28)
        print("1. Start New Game")
        print("2. Change Difficulty")
        print("3. View Leaderboard")
        print("4. Quit")
        typing_effect("=" * 28 + "\n", speed = 0.01)
        
        choice = input("Enter your choice (1-4): \n")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 4")


def place_ships_randomly(game_board, ships, board_size):
    """
    randomly place ships on both boards
    """
    for ship in ships:
        placed = False
        while not placed:
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1)
            horizontal = random.choice([True, False])
            placed = game_board.place_ship(ship, (x, y), horizontal)
            # Generate ranom position & orientation


def start_new_game(difficulty, leaderboard):
    """
    initializes a new game with current difficulty.
    creates a GameBoard instance based on difficulty,
    handles random ship placement & game progression.
    asks player for username.
    """
    typing_effect("Please enter a player name: ")
    player_name = input()

    print(f"{player_name}, We are now starting a new game with difficulty: {difficulty}")
    board_size = 5 if difficulty == 'Easy' else 8
    player_board = GameBoard(size = board_size)
    computer_board = GameBoard(size = board_size)
    
    ships = [Ship("Battleship", 3), Ship("Cruiser", 3), 
            Ship("Destroyer", 2), 
            Ship("Patrol Boat", 1)]
    # Define ships

    place_ships_randomly(player_board, ships, board_size)
    place_ships_randomly(computer_board, ships, board_size)
    # Place ships for both player and computer

    typing_effect("\nGame started! Here's your board:")
    player_board.print_board(reveal_ships=True)
    
    # Continues until the game is over, 
    # Alternating between player turns 
    # and a placeholder for the computer's turn.
    while not (player_board.is_game_over() or computer_board.is_game_over()):
        turn_result = player_turn(player_board, computer_board)

        if turn_result == "quit":
            typing_effect("Returning to the main menu...")
            return
            # Exit the function, returning to the main menu

        if computer_board.is_game_over():
            print(f"Congratulations, {player_name}! You won!")
            update_leaderboard(leaderboard, player_name, True)
            break

        computer_turn(player_board)
        if player_board.is_game_over():
            print(f"Sorry, {player_name}. the computer won this time.")
            update_leaderboard(leaderboard, player_name, False)
            break
        # Checks after each turn if the game is over.  
        # If all ships of player/computer are sunk, 
        # Game ends!

        typing_effect("Current state of the enemy's board:")
        computer_board.print_board(reveal_ships=False)

    typing_effect("Game over! Here's the final computer board:")
    computer_board.print_board(reveal_ships = True)
    typing_effect("Here's your final board:")
    player_board.print_board(reveal_ships = True)


def change_difficulty():
    """
    allows player to change the game's difficulty level.
    presents player with two difficulty options.
    player's choice determines the size of board used in the new game.
    returns chosen difficulty as string.
    """
    while True: 
        print("\nSelect Difficulty:")
        print("1. Easy! (5X5 Board for both player & computer.)")
        print("2. Hard! (8X8 Board for both player & computer!)")

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


def player_turn(player_board, computer_board):
    """
    handles player's turn to guess & attack a coordinate.
    allows player to input coordinates for an attack,
    handles the shot logic.
    allows user to quit to main menu by pressing n.
    """
    while True:
        print('\nEnter "n" to quit or "my" to view computer attacks on your board: ')
        typing_effect('Enter coordinates to attack (e.g., "A5")')
        input_str = input().strip().lower()

        if input_str == "n":
            return "quit"
        elif input_str == "my":
            typing_effect("Here's the current state of your board:")
            player_board.print_board(reveal_ships=False)
            # Show player's board without revealing ship locations
            continue  # Prompt for input again

        try:
            x, y = convert_to_coords(input_str)
             # Convert input to board coordinates
            if not is_within_board((x, y), computer_board.size):
                print("Coordinates out of range. Please try again.")
                continue
            result = computer_board.take_shot((x, y))
            typing_effect(result)
            if result not in ["Already hit", "Coordinates out of range"]:
                break
        except ValueError as e:
            print(e)
        # Improved input handling


def computer_turn(player_board):
    """
    Handles the computer's turn to guess and attack a coordinate.
    enables the computer to randomly choose a target,
    ensures the computer does not attack a previously hit coordinate.
    """
    while True:
        x = random.randint(0, player_board.size - 1)
        y = random.randint(0, player_board.size - 1)
        result = player_board.take_shot((x, y))
        if result != "Already hit":
            typing_effect(f"Computer attacked {chr(65 + x)}{y + 1} and {result}")
            break


def update_leaderboard(leaderboard, player_name, player_won):
    """
    updates the leaderboard based on game outcome
    """
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
            instruction_result = display_game_instructions()
            if instruction_result == "quit":
                print("Returning to the main menu...")
                continue # Goes back to main menu
            print("Starting a new game...\n")
            start_new_game(current_difficulty, global_leaderboard)
        elif choice == 2:
            print("Changing difficulty...\n")
            current_difficulty = change_difficulty()
        elif choice == 3:
            print("Displaying leaderboard...\n")
            view_leaderboard()
        elif choice == 4:
            print("Exiting game. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
# runs if directly called only
# allows script to be imported in other py files
# without automatically running the game. 
# for reuse of functions/classes in other scripts.