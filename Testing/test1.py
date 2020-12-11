import unittest

from prime import is_prime

class Tests(unittest.TestCase):
    
    def test_1(self):
        """Check that 1 is not a prime. """
        self.assertFalse(is_prime(1))
       
       
    def test_2(self):
        """Check that 25 is a prime. """
        self.assertFalse(is_prime(25))
       


if __name__ == "__main__":
    unittest.main()
    
