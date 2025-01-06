from pywebio import start_server
from pywebio.output import *
from pywebio.input import *
from gameboard import GameBoard
from ship import Ship
from leaderboard import Leaderboard
import random
from utils import convert_to_coords, is_within_board

global_leaderboard = Leaderboard()

def render_board(board, reveal_ships=False):
    """Convert GameBoard to HTML table representation"""
    table = []
    # Header row with column letters
    header = [''] + [chr(65 + i) for i in range(board.size)]
    table.append(header)
    
    for y in range(board.size):
        row = [str(y + 1)]  # Row numbers
        for x in range(board.size):
            cell = board.board[x][y]
            if cell == 'O' and not reveal_ships:
                cell = '?'
            row.append(cell)
        table.append(row)
    
    put_table(table)

async def display_main_menu():
    """Web-based main menu"""
    clear()
    put_markdown("# BATTLESHIP GAME")
    choice = await actions('Choose an action:', [
        {'label': 'Start New Game', 'value': '1'},
        {'label': 'Change Difficulty', 'value': '2'},
        {'label': 'View Leaderboard', 'value': '3'},
        {'label': 'Quit', 'value': '4'}
    ])
    return int(choice)

async def display_game_instructions():
    """Display game instructions to the player"""
    clear()
    put_markdown("""# How to Play Battleship
    
1. Each player has a board with ships placed on it
2. Take turns attacking coordinates on the enemy's board
3. Use letter + number format (e.g., A5) to specify attack coordinates
4. Hits are marked with 'X', misses with '-'
5. Sink all enemy ships to win!
    """)
    choice = await actions('Ready to play?', [
        {'label': 'Start Game', 'value': 'start'},
        {'label': 'Return to Menu', 'value': 'quit'}
    ])
    return choice

async def start_new_game(difficulty, leaderboard):
    """Web-based game implementation"""
    clear()
    
    # Show instructions first
    choice = await display_game_instructions()
    if choice == 'quit':
        return
        
    player_name = await input("Please enter your player name:", required=True)
    
    put_markdown(f"## Starting new game for {player_name}")
    put_text(f"Difficulty: {difficulty}")
    
    board_size = 5 if difficulty == 'Easy' else 8
    player_board = GameBoard(size=board_size)
    computer_board = GameBoard(size=board_size)
    
    ships = [
        Ship("Battleship", 3),
        Ship("Cruiser", 3),
        Ship("Destroyer", 2),
        Ship("Patrol Boat", 1)
    ]
    
    place_ships_randomly(player_board, ships, board_size)
    place_ships_randomly(computer_board, ships, board_size)
    
    put_markdown("## Your Board:")
    render_board(player_board, reveal_ships=True)
    
    while not (player_board.is_game_over() or computer_board.is_game_over()):
        # Player's turn
        while True:
            try:
                action = await actions("Your turn:", [
                    {'label': 'Attack', 'value': 'attack'},
                    {'label': 'View My Board', 'value': 'view'},
                    {'label': 'View Enemy Board', 'value': 'enemy'},
                    {'label': 'Quit Game', 'value': 'quit'}
                ])
                
                if action == 'quit':
                    return
                
                if action == 'view':
                    put_markdown("## Your Board Status:")
                    render_board(player_board, reveal_ships=True)
                    continue
                
                if action == 'enemy':
                    put_markdown("## Current state of the enemy's board:")
                    render_board(computer_board, reveal_ships=False)
                    continue
                
                coords = await input("Enter attack coordinates (e.g., A5):",
                                   required=True,
                                   validate=lambda x: 'Invalid format' \
                                   if not validate_coords(x, board_size) else None)
                
                x, y = convert_to_coords(coords)
                result = computer_board.take_shot((x, y))
                put_markdown(f"**Attack Result:** {result}")
                
                if result != "Already hit" and result != "Coordinates out of range":
                    put_markdown("## Current state of the enemy's board:")
                    render_board(computer_board, reveal_ships=False)
                    break
                
            except ValueError as e:
                put_error(str(e))
                
        if computer_board.is_game_over():
            put_markdown(f"## 🎉 Congratulations {player_name}! You won!")
            update_leaderboard(leaderboard, player_name, True)
            break
        
        # Computer's turn
        computer_turn_result = computer_turn(player_board)
        put_markdown(f"**Computer's move:** {computer_turn_result}")
        
        if player_board.is_game_over():
            put_markdown(f"## Game Over! {player_name}, the computer won.")
            update_leaderboard(leaderboard, player_name, False)
            break
    
    put_markdown("## Final Boards")
    put_markdown("### Your Board:")
    render_board(player_board, reveal_ships=True)
    put_markdown("### Computer's Board:")
    render_board(computer_board, reveal_ships=True)
    
    await actions('', [{'label': 'Return to Main Menu', 'value': 'menu'}])

async def change_difficulty():
    """Web-based difficulty selection"""
    clear()
    put_markdown("# Select Difficulty")
    choice = await actions('Choose difficulty:', [
        {'label': 'Easy (5x5 Board)', 'value': '1'},
        {'label': 'Hard (8x8 Board)', 'value': '2'}
    ])
    return "Easy" if choice == "1" else "Hard"

def view_leaderboard():
    """Web-based leaderboard display"""
    clear()
    put_markdown("# Leaderboard")
    scores = global_leaderboard.scores  # Use the scores property directly instead of get_scores()
    if not scores:
        put_text("No scores yet!")
    else:
        table = [['Player', 'Wins', 'Losses']]
        for player, (wins, losses) in scores.items():
            table.append([player, wins, losses])
        put_table(table)
    
    # Add return to menu button
    put_button('Return to Menu', onclick=lambda: clear())

def validate_coords(coords, board_size):
    """Validate coordinate input"""
    try:
        x, y = convert_to_coords(coords)
        return is_within_board((x, y), board_size)
    except:
        return False

def computer_turn(player_board):
    """Handle computer's turn and return result message"""
    while True:
        x = random.randint(0, player_board.size - 1)
        y = random.randint(0, player_board.size - 1)
        result = player_board.take_shot((x, y))
        if result != "Already hit":
            return f"{chr(65 + x)}{y + 1} - {result}"

def update_leaderboard(leaderboard, player_name, player_won):
    """Updates the leaderboard with game results"""
    leaderboard.update_score(player_name, player_won)

async def main():
    """Main web application loop"""
    current_difficulty = "Easy"
    
    while True:
        choice = await display_main_menu()
        
        if choice == 1:
            await start_new_game(current_difficulty, global_leaderboard)
        elif choice == 2:
            current_difficulty = await change_difficulty()
        elif choice == 3:
            view_leaderboard()
        elif choice == 4:
            put_markdown("# Thanks for playing!")
            break

def place_ships_randomly(game_board, ships, board_size):
    """Randomly place ships on the board"""
    for ship in ships:
        placed = False
        while not placed:
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1)
            horizontal = random.choice([True, False])
            placed = game_board.place_ship(ship, (x, y), horizontal)

if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
