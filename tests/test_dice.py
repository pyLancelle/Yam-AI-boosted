import unittest
from src.game.player import DiceSet

class TestDice(unittest.TestCase):
    def setUp(self):
        """Configuration initiale pour chaque test."""
        self.dice_set = DiceSet()

    def test_initial_roll(self):
        """Test le lancement initial des dés."""
        self.dice_set.roll([])
        self.assertTrue(all(1 <= dice.value <= 6 for dice in self.dice_set.set))

    def test_repr(self):
        expected = '\n'.join([f'Dice {i+1} : {str(d)}' for i,d in enumerate(self.dice_set.set)])
        print(expected)
        print('--')
        value = self.dice_set.__repr__()
        print(value)
        self.assertEqual(expected, value)
