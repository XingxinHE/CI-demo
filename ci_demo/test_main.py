import unittest
from main import is_even


class Tests(unittest.TestCase):
    def test_str(self):
        """Test if the function returns the correct output for a string input"""
        self.assertFalse(is_even('x'))

    def test_float(self):
        """Test if the function returns the correct output for a float input"""
        self.assertFalse(is_even(2.5))
    
    def test_even(self):
        """Test if the function returns True for an even number"""
        self.assertTrue(is_even(2))
    
    def test_odd(self):
        """Test if the function returns False for an odd number"""
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    unittest.main()

