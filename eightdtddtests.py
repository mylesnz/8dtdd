import unittest
from eightdtddcode import *

class MyFirstTests(unittest.TestCase):

    # Test Output
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    # Test 2
    def test_custom_num_list(self):
       self.assertEqual(len(create_num_list(10)), 10)
    

    # Test 3
    def test_custom_func_x(self):
       self.assertEqual(custom_func_x(3,2,3), 54)

    # Test 4
    def test_custom_non_lin_num_list(self):
       self.assertEqual(custom_non_lin_num_list(5,2,3)[2], 16)
       self.assertEqual(custom_non_lin_num_list(5,3,2)[4], 48)

if __name__ == '__main__':
    unittest.main()

# IGNORE THIS
# def testadd(self):
#     self.assertEqual(add(7,3), 10)
#     self.assertTrue(add(5,9) == 14)
