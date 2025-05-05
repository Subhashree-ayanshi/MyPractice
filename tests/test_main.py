import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','src')))
from main_py import add,multiply
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5) 
        self.assertEqual(add(-1,1),0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(0,5),0)
if __name__ =="__main__":
    unittest.main()
