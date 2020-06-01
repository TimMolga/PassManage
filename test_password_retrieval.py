import unittest
from password_retrieval import get_data, get_password

class TestPasswordRetrieval(unittest.TestCase):

    def test_check_data(self):
        data = get_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
