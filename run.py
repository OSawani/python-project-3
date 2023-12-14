# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Global variable for difficulty
current_difficuty = "Easy"


def display_main_menu():
    """
    Displays the main menu options and handles user input
    """
    print("\nWelcome to Battleship!")
    print("1. Start New Game")
    print("2. Change Difficulty")
    print("3. View Leaderboard")
    print("4. Quit\n")

    choice = input("Enter your choice (1-4): \n")
    return choice


def initialise_game_board(difficulty):
    """
    Initializes and returns a game board based on the selected difficulty.

    :param difficulty: A string representing the game difficulty ('Easy' or 'Hard')
    :return: A 2D list representing the game board
    """
    if difficulty == "Easy":
        size = 8
    elif difficulty == "Hard":
        size = 5
    else:
        size = 8
    
    # Create a 2D list filled with '.' representing water
    board = [["." for _ in range(size)] for _ in range(size)]


def change_difficulty():
    """
    Allows the user to change the game difficulty 
    and updates the global difficulty variable.

    """
    global current_difficulty
    # Placeholder for changing difficulty
    # This should update current_difficulty based on user input
    print("\nChange Difficulty:")
    print("1. Easy")
    print("2. Hard")

    choice = input("Select difficulty (1-2): ")

    if choice == "1":
        current_difficutly = "Easy" 
        print("Changing difficulty...")
        print("Difficulty set to Easy.")
    elif choice == "2":
        current_difficutly = "Hard" 
        print("Changing difficulty...")
        print("Difficulty set to Hard.")
    else: 
        print("Invalid choice. Difficulty unchanged.")


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




"""
Allows run.py script to be imported in other Python files
without automatically running the game. 
Useful to reuse certain functions or classes in other scripts.
"""
if __name__ == "__main__":
    main()
