import unittest
from game import RPSGame
from scoreboard import ScoreBoard

class TestRPS(unittest.TestCase):
    def setUp(self):
        self.game = RPSGame("Test", ScoreBoard())

    def test_win(self):
        self.assertEqual(self.game.get_result("rock","scissors"), "win")

    def test_loss(self):
        self.assertEqual(self.game.get_result("rock","paper"), "loss")

    def test_draw(self):
        self.assertEqual(self.game.get_result("rock","rock"), "draw")

if __name__ == "__main__":
    unittest.main()
