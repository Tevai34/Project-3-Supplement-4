import unittest 
from main import is_prime, split_range 

class TestPrimeFunctions (unittest.TestCase):
    # Test for is_prime 
    def test_is_prime(self):
        self.assertFalse(is_prime(1)) #is not a prime number
        self.assertTrue(is_prime(2))  # is a prime numner 
        self.assertTrue(is_prime(13)) # is a prime number 
        self.assertFalse(is_prime(25)) # is not a prime number 
        
    # test for split_range
    def test_split_range(self):
        # Splitting range 1-10 into 2 parts unless they are (1, 5), (6, 10)
        self.assertEqual(split_range(1, 10, 2), [(1, 5), (6, 10)])
        # Splitting range 1-9 into 3 parts unless they are (1, 3), (4, 6), (7, 9)
        self.assertEqual(split_range(1, 9, 3), [(1, 3), (4, 6), (7, 9)])
    
# driver code        
if __name__ == '__main__':
    unittest.main()