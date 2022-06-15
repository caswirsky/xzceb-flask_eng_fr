"""This file tests the functions in translator.py"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Tests both functions in translator.py"""
    def test_english_to_french(self):
        """Tests english to french function"""
        self.assertEqual(english_to_french('Hello'),'Bonjour') # Tests that hello returns bonjour

    def test_french_to_english(self):
        """Tests french to english"""
        self.assertEqual(french_to_english('Bonjour'),'Hello') # Tests that bonjour returns hello

if __name__=='__main__':
    unittest.main()
