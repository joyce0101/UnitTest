import json
import requests
"""jieshou=serial.Serial('/dev/ttyACM0',9600,timeout=1)"""
def add(a,b):
    return a+b
def postmessage(temp, url, name,apikey):
    if type(temp)==type({}):
        #temp=eval(temp)
        #s=temp
        if int(temp['Value']) > 20 and int(temp['Value']) <= 90:
            payload = [{'Name': name, 'Value': int(temp['Value'])}]
            apiheaders=apikey
            datas=str(payload)
            try:
                r=requests.post(url,headers=apiheaders,data=datas)
                if(r.status_code==200):
                    return "ok"
                else:
                    return str(r.status_code)
            except Exception as e:
                return str(e)
        else:
            #将错误信息写至日志
            return "OverRange"
    else:
        #将错误信息写至日志
        return "BadData"
"""
def get_data(url):
    try:
        r = requests.get(url)
        states = json.loads(r.text)
        if states["states"] == False:
            jieshou.write("off")
            jieshou.write("\n")
            return "off"
        else:
            jieshou.write("on")
            jieshou.write("\n")
            return "on"
    except Exception as e:
        Manual()
        return "ConnectionError"
def Manual():
    return "ok"
def get_arduino():
    temp=jieshou.readline()
    return temp
"""
"""
if __name__=='__main__':
    url="http://www.lewei50.com/api/V1/gateway/UpdateSensors/01"
    payload = {'Name': 'D_On-Off', 'Value': 21}
    apiheader = {'userkey': '00757a1f7cd34dea88dc52b34aec9d98'}
    res= postmessage(payload,url,'D_on-off',apiheader)
    print(res)
"""








