import unittest
from test_func import *
if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[Test_Func("test_add"),Test_Func("test_postmessage")]
    suite.addTests(tests)
    with open('UnittestReport.txt','a') as f:
        runner=unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)