import unittest
from eightdtddcode5 import *

class MyFirstTests(unittest.TestCase):

    # Test Output
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    # Test Custom Number List
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    # Test Custom Function
    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)
        self.assertEqual(custom_non_lin_num_list(5,3,2)[4], 48)

if __name__ == '__main__':
    unittest.main()
