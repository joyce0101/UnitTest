import unittest
from test_func import *
if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[Test_Func("test_add"),Test_Func("test_postmessage")]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)