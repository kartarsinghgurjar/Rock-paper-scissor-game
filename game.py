import random
from scoreboard import ScoreBoard

CHOICES = ("rock", "paper", "scissors")

class RPSGame:
    def __init__(self, player_name, scoreboard: ScoreBoard):
        self.player_name = player_name
        self.scoreboard = scoreboard

    def get_result(self, player, computer):
        if player == computer:
            return "draw"
        if (player, computer) in {("rock","scissors"),("paper","rock"),("scissors","paper")}:
            return "win"
        return "loss"

    def play_round(self):
        print("\nChoose: 1.Rock  2.Paper  3.Scissors")
        options = {"1":"rock","2":"paper","3":"scissors"}
        while True:
            raw = input("Your choice: ").strip()
            if raw in options:
                break
            print("Invalid choice. Enter 1, 2 or 3.")
        player = options[raw]
        computer = random.choice(CHOICES)
        result = self.get_result(player, computer)
        print(f"Computer chose: {computer.title()}")
        print(f"Result: {result.title()}")
        self.scoreboard.update(self.player_name, result)
