import unittest
from unittest.mock import Mock, patch
from requests.exceptions import Timeout
from password_generator import generate_words, generate_password
from test_functions import hasNumber, hasSpecialCharacter, hasUppercase

class TestPasswordGenerator(unittest.TestCase):
    #test generate_words function
    @patch('password_generator.requests')
    def test_word_generator_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            generate_words()
        mock_requests.get.assert_called_once()

    #test generate_words function
    def test_generate_words(self):
        words = generate_words()
        words_length = len(words)
        word_count = 4
        self.assertEqual(words_length, word_count)

    def test_generate_different_words(self):
        words_list_one = generate_words()
        words_list_two = generate_words()
        self.assertNotEqual(words_list_one, words_list_two)
        
    def test_generate_words_number(self):
        words = generate_words()
        self.assertFalse(hasNumber(words))

    def test_generate_words_character(self):
        words = generate_words()
        self.assertFalse(hasSpecialCharacter(words))

    def test_generate_words_upper(self):
        words = generate_words()
        self.assertFalse(hasUppercase(words))
    
    #test generate_password function
    def test_generate_password_number(self):
        password = generate_password()
        self.assertTrue(hasNumber(password))

    def test_generate_password_character(self):
        password = generate_password()
        self.assertTrue(hasSpecialCharacter(password))

    def test_generate_password_upper(self):
        password = generate_password()
        self.assertTrue(hasUppercase(password))

if __name__ == '__main__':
    unittest.main()