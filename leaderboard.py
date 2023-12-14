# Manages leaderboard:
# recording game outcomes,
# displaying leaderboard.


class Leaderboard:
    def __init__(self):
        """
        manages player scores with functions to:
        update scores,
        display leaderboard.
        """
        self.scores = {}
        # Format: {'player_name': {'wins': 0, 'losses': 0}}

    def update_score(self, player_name, won):
        """
        updates the win/loss count for a player.
        """
        if player_name not in self.scores:
            self.scores[player_name] = {'wins': 0, 'losses': 0}
        
        if won:
            self.scores[player_name]['wins'] += 1
        else:
            self.scores[player_name]['losses'] += 1

    def display_leaderboard(self):
        """
        prints out the current standings.
        """
        print("\n ****** Leaderboard ******:")
        for player, scores in self.scores.items():
            wins, losses = scores['wins'], scores['losses']
            print(f"{player} - Wins: {wins}, Losses: {losses}")

# Example usage
leaderboard = Leaderboard()
leaderboard.update_score("Player1", True)  # Player1 won a game
leaderboard.display_leaderboard()
