"""Tests for the game rules (no window is opened)."""

import unittest

from main import Game


class GameTests(unittest.TestCase):
    def test_all_rules(self):
        cases = (
            ("rock", "scissors", "win"),
            ("rock", "paper", "lose"),
            ("rock", "rock", "draw"),
            ("paper", "rock", "win"),
            ("paper", "scissors", "lose"),
            ("paper", "paper", "draw"),
            ("scissors", "paper", "win"),
            ("scissors", "rock", "lose"),
            ("scissors", "scissors", "draw"),
        )
        for user_move, machine_move, expected in cases:
            with self.subTest(user=user_move, machine=machine_move):
                self.assertEqual(Game.resolve(user_move, machine_move), expected)

    def test_score_changes(self):
        game = Game()
        self.assertEqual(game.play("rock", "scissors"), "win")
        self.assertEqual(game.play("paper", "rock"), "win")
        self.assertEqual(game.play("rock", "paper"), "lose")
        self.assertEqual(game.play("paper", "paper"), "draw")
        self.assertEqual((game.user_score, game.machine_score), (2, 1))

    def test_reset(self):
        game = Game()
        game.play("rock", "scissors")
        game.reset()
        self.assertEqual((game.user_score, game.machine_score), (0, 0))

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            Game.resolve("lagarto", "rock")


if __name__ == "__main__":
    unittest.main()
