# # Your code goes here.
# # You can delete these comments, but do not change the name of this file
# # Write your code to expect a terminal of 80 characters wide and 24 rows high

# import random
# # Global variable for difficulty
# current_difficuty = "Easy"





# def initialise_game_board(difficulty):
#     """
#     Initializes and returns a game board based on the selected difficulty.

#     :param difficulty: A string representing the game difficulty ('Easy' or 'Hard')
#     :return: A 2D list representing the game board
#     """
#     if difficulty == "Easy":
#         size = 8
#     elif difficulty == "Hard":
#         size = 5
#     else:
#         size = 8
    
#     # Create a 2D list filled with '.' representing water
#     board = [["." for _ in range(size)] for _ in range(size)]


# def change_difficulty():
#     """
#     Allows the user to change the game difficulty 
#     and updates the global difficulty variable.

#     """
#     global current_difficulty
#     # Placeholder for changing difficulty
#     # This should update current_difficulty based on user input
#     print("\nChange Difficulty:")
#     print("1. Easy")
#     print("2. Hard")

#     choice = input("Select difficulty (1-2): ")

#     if choice == "1":
#         current_difficutly = "Easy" 
#         print("Changing difficulty...")
#         print("Difficulty set to Easy.")
#     elif choice == "2":
#         current_difficutly = "Hard" 
#         print("Changing difficulty...")
#         print("Difficulty set to Hard.")
#     else: 
#         print("Invalid choice. Difficulty unchanged.")


# # def is_valid_placement(board, ship_size, start_row, start_col, orientation):
# #     """
# #     Checks if a ship can be placed at the given location with the given orientation.
# #     """
    


# # def place_ship(board, ship_size, orientation):
# #     """
# #     Places a ship of given size and orientation on the board.
# #     """
# #     max_row, max_col = len(Board), len(board[0])
# #     if orientation == "horizontal":
# #         row, col = random.randint(0, max_row - 1), random.randint(0, max_col - ship_size)
# #     else:  # vertical
# #         row, col = random.randint(0, max_row - ship_size), random.randint(0, max_col - 1)
    
# #     while not is_valid_placement(board, ship_size, row, col, orientation):
# #         row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)

# #     for i in range(ship_size):
# #         board[row + (i if orientation == 'vertical' else 0)][col + (0 if orientation == 'vertical' else i)] = 'S'


# # def place_ships(board, ships):
# #     """
# #      Places ships on the board at random locations.

# #     :param board: The game board (a 2D list).
# #     :param ships: A list of tuples, each representing a ship and its size.
# #     """
# #     for ship, size in ships:
# #         place_ship(board, size, random.choice(["horizontal", "vertical"]))






# """
# Allows run.py script to be imported in other Python files
# without automatically running the game. 
# Useful to reuse certain functions or classes in other scripts.
# """
# if __name__ == "__main__":
#     main()
