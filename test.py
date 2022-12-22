import unittest
import bot as testing

class BotTest(unittest.TestCase):

    def setUp(self):
        testing.bot.config['TESTING'] = True
        self.bot = testing.bot.test_client()

if __name__ == '__main__':
    unittest.main()