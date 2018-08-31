import unittest
from eightdtddcode2 import *

class MyFirstTests(unittest.TestCase):

    # Test Output
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

if __name__ == '__main__':
    unittest.main()

# IGNORE THIS
# def testadd(self):
#     self.assertEqual(add(7,3), 10)
#     self.assertTrue(add(5,9) == 14)
