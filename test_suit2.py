import unittest
from test_func import *

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Func))  # TestLoader不能保证按照顺序执行
    runner = unittest.TextTestRunner()
    runner.run()
