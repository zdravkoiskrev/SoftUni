class SteamUser:

    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        g = game
        h = hours
        if g in self.games:
            self.played_hours += h
            return f"{self.username} is playing {g}"
        else:
            return f"{g} is not in library"

    def buy_game(self, game):
        g = game
        if g not in self.games:
            self.games.append(g)
            return f"{self.username} bought {g}"
        else:
            return f"{g} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())