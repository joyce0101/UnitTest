import unittest
from test_func import *
if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[Test_Func("test_add"),Test_Func("test_postmessage")]
    suite.addTests(tests)
	#with的用法，需要注意和学习一下
    with open('UnittestReport.txt','a') as f:
        runner=unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)