# Serves as entry point for game. 
# Sets up main loop and calls main menu.


def display_main_menu():
    """
    Displays the main menu options and handles user input.
    Returns a valid choice as an integer.
    """
    print("\nWelcome to Battleship!")
    print("1. Start New Game")
    print("2. Change Difficulty")
    print("3. View Leaderboard")
    print("4. Quit\n")

    choice = input("Enter your choice (1-4): \n")
    return choice


def main():
    """
    The main game loop.
    """
    global current_difficulty
    while True:
        choice = display_main_menu()
        
        if choice == '1':
            print("Starting a new game...")
            game_board = initialise_game_board(current_difficulty)
            # Placeholder for starting a new game with game_board
        elif choice == '2':
            change_difficulty()
            # Placeholder for changing difficulty
        elif choice == '3':
            print("Displaying leaderboard...")
            # Placeholder for viewing the leaderboard
        elif choice == '4':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")