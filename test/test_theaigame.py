import sys
import unittest
from pokeher.game import *
from pokeher.game import Constants as C
from pokeher.theaigame import *

class CardBuilderTest(unittest.TestCase):
    def test_from_string(self):
        """Tests building our cards from theaigame text strings"""
        b = CardBuilder()

        self.assertEqual(b.from_string('Th'), Card(10, C.HEARTS))
        self.assertEqual(b.from_string('9s'), Card(9, C.SPADES))
        self.assertEqual(b.from_string('Ad'), Card(C.ACE, C.DIAMONDS))
        self.assertEqual(b.from_string('2c'), Card(2, C.CLUBS))

class SettingsParserTest(unittest.TestCase):
    def test_parse_settings(self):
        """Tests that the beginning settings are passed to the data model"""
        lines = ['Settings gameType NLHE',
                 'Settings gameMode tournament',
                 'Settings timeBank 5000',
                 'Settings timePerMove 500',
                 'Settings handsPerLevel 10',
                 'Settings yourBot bot_0']

        data = {}
        parser = SettingsParser(sys.stdout, data)

        for line in lines:
            handled = parser.handle_line(line)
            self.assertTrue(handled)

        self.assertEqual(data['yourBot'], 'bot_0')