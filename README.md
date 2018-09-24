"PyUnit框架练习" ，func.py为待测试函数，test_func.py为编写的testcase，test_suit.py为测试套件。

学习笔记部分：

2018.04

unittest核心工作原理

unittest中最核心的四个概念是：test case, test suite, test runner, test fixture。
![笔记](https://github.com/joyce0101/UnitTest/blob/master/pics/system.png)
![笔记](https://github.com/joyce0101/UnitTest/blob/master/pics/1.PNG)
![笔记](https://github.com/joyce0101/UnitTest/blob/master/pics/2.PNG)
![笔记](https://github.com/joyce0101/UnitTest/blob/master/pics/3.PNG)

# 直接使用TestLoader方法（但是无法对case排序）,见test_suit2.py.    
如果用例很多，但是想跳过一部分用例，此时可以使用skip装饰器：   
<pre>    
@unittest.skip("I don't want to run this case.")     
def test_divide(self):    
    print "divide"    
    self.assertEqual(2, divide(6, 3))    
    self.assertEqual(2.5, divide(5, 2))    
</pre> 
## skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
# 总结一下：
1、unittest是Python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架。  
2、unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。  
3、一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase。  
4、verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。  
5、可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法。  
6、用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境  
7、我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法。  

本文参考：https://blog.csdn.net/huilan_same/article/details/52944782?utm_source=copy 
