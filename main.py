from game import RPSGame
from scoreboard import ScoreBoard
from storage import load_scores, save_scores
from utils import ask_name, menu

def main():
    scores = ScoreBoard(load_scores())
    name = ask_name()
    game = RPSGame(name, scores)
    while True:
        choice = menu()
        if choice == "1":
            game.play_round()
        elif choice == "2":
            scores.show()
        elif choice == "3":
            scores.reset()
            save_scores(scores.data)
            print("Scoreboard reset.")
        elif choice == "4":
            save_scores(scores.data)
            print("Thank you for playing.")
            break

if __name__ == "__main__":
    main()
