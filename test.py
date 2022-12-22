import unittest
import bot as testing
import json

class BotTest(unittest.TestCase):

    def setUp(self):
        self.entry_points = commands=["start"]
        self.bot = testing.bot.test_client()

if __name__ == '__main__':
    unittest.main()