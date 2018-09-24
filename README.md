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
# skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
