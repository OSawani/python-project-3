# Manages leaderboard:
# recording game outcomes,
# displaying leaderboard.


class Leaderboard:
    def __init__(self):
        """
        initialises leaderboard with an empty score dict.

        manages player scores with functions to:
        update scores,
        display leaderboard.
        """
        self.scores = {}
        # Format: {'player_name': {'wins': 0, 'losses': 0}}

    def update_score(self, player_name, won):
        """
        updates the win/loss count for a player based on outcome.

        :param player_name: Name of player.
        :param won: Boolean indicating if player won the game.
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


    def save_to_file(self, filename="leaderboard.txt"):
        """
        saves leaderboard to a file.

        :param filename: Name of file to save the leaderboard.
        """
        with open(filename, 'w') as file:
            for player, score in self.scores.items():
                file.write(f"{player}: {score['wins']} wins, {score['losses']} losses\n")


    def load_from_file(self, filename="leaderboard.txt"):
        """
        loads leaderboard from a file.

        :param filename: Name of file to load the leaderboard.
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    player, scores = parts[0], parts[1].strip().split(",")
                    wins, losses = [int(s.split()[0]) for s in scores]
                    self.scores[player] = {'wins': wins, 'losses': losses}
        except FileNotFoundError:
            print(f"No saved leaderboard found at '{filename}'. Starting fresh.")


