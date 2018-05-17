import unittest
import logging
from func import *
logger = logging.getLogger("threading_test")
name=''
values=[]
temps=[]
url=""
apikey={}
class Test_Func(unittest.TestCase):
    @classmethod
	#只执行一次
    def setUpClass(cls):
        global name;
        name='D_On-Off'
        values.append(10)
        values.append(21)
        values.append(89)
        #values=[10,21,89,]
        temps.append({'Name':name,'Value':values[1]})
        temps.append("{'Name':name,'Value':")
        #temps=["{'Name':self.name,'Value':self.values[1]}","{'Name':name,'Value':"]
        global url
        url="http://www.lewei50.com/api/V1/gateway/UpdateSensors/01"
        apikey={'userkey': '00757a1f7cd34dea88dc52b34aec9d98'}
        print(" environment prepareed succesful.")
        #print(apikey)
        #print(url)
        logger.setLevel(logging.DEBUG)  # 级别
        fh = logging.FileHandler("threading.log")
        fmt = '%(asctime)s-%(threadName)s-%(levelname)s-%(message)s'
        formatter = logging.Formatter(fmt)  # 定义输出格式
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    """
    def tearDown(self):
        connection=pymongo.MongoClient('')
        db=connection.mgdb
        db.authenticate("account","password")
        post=db.test
        post.update({"_id":objectId("4ff...04")},{$pop:{"soils":1}})#删除soils数组中的最后一行；
    """
    def test_postmessage(self):
        self.assertEqual("BadData", postmessage(temps[1], url, name,apikey))
        logger.debug("data:"+str(temps[1]))
        self.assertEqual("ok", postmessage(temps[0], url, name, apikey))
        logger.debug("data:" + str(temps[0]))
        #self.assertEqual(3,add(1,2))
    def test_add(self):
        self.assertEqual(3,add(1,2))

if __name__ == '__main__':
    unittest.main()


