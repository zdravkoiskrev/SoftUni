from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            if player.name == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
        elif not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"

        for i in self.players:
            result += "\n"
            result += Player.player_info(i)
        return result
