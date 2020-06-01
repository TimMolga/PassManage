import unittest
import unittest.mock as mock
from password_generator import generate_words, generate_password
from test_functions import hasNumber, hasSpecialCharacter, hasUppercase

class TestPasswordGenerator(unittest.TestCase):

    #test generate_words function
    def test_check_words(self):
        words = generate_words()
        words_length = len(words)
        word_count = 4
        self.assertEqual(words_length, word_count)

    @unittest.expectedFailure
    def test_check_different_words(self):
        words_list_one = generate_words()
        words_list_two = generate_words()
        self.assertListEqual(words_list_one, words_list_two)
        
    def test_check_words_number(self):
        words = generate_words()
        self.assertFalse(hasNumber(words))

    def test_check_words_character(self):
        words = generate_words()
        self.assertFalse(hasSpecialCharacter(words))

    def test_check_words_upper(self):
        words = generate_words()
        self.assertFalse(hasUppercase(words))
    
    #test generate_password function
    def test_check_password_number(self):
        password = generate_password()
        self.assertTrue(hasNumber(password))

    def test_check_password_character(self):
        password = generate_password()
        self.assertTrue(hasSpecialCharacter(password))

    def test_check_password_upper(self):
        password = generate_password()
        self.assertTrue(hasUppercase(password))

if __name__ == '__main__':
    unittest.main()