#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json
from requests.exceptions import RequestException
import os 
import time
import datetime
from datetime import timedelta,datetime

#以下以天水师范学院七楼34号座位为例#

'''全部参数预设'''
#用户名和密码
login_user       = '学号'
login_passwd     = '密码'
#获取sign签名
beskids          = '20'
roomid           = '19'
#提交时间认证
id_time          = '19'
#阅览室列表查询
beskid_1         = '20'
#查询表单
roomno           = '19'
isuseday         = '1'
begintime        = '07:59:59'
endtime          = '22:00:00',
beskid_2         = '20',
beskCanId        = '20',
#提交表单
tableid          = 1396
tableno          = '七楼-034' 
'''全部参数设置完毕'''

#创建该目录下的该文件
file = open (r'/www/Library/LogEmail.txt','w')



''' 向网页发起get请求，回传server时间，如果时间等于预设值，则执行系统命令，注意格式！24小时制 '''
while True:
    #设置需要执行命令的时间，时间精确到分钟
    #即在该分钟内的任何一秒内等于预设值，命令都会执行，防止丢包导致匹配失败

    if time == '07:00:0':

        #需要执行的命令
        '''登录系统'''
        url_login ='http://tsgzwyy.tsnu.edu.cn:8060/login'
        login_form = {
            'user':login_user,
            'passwd':login_passwd,
            }
    
        cookies = ''
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Content-Length': '30',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookies,
            'DNT': '1',
            'Host': 'tsgzwyy.tsnu.edu.cn:8060',
            'Origin': 'http://tsgzwyy.tsnu.edu.cn:8060',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/unlogin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36',
            }
    
        session = requests.Session()
        resp_login = session.post(url_login, headers=headers,data=login_form)
        resp_login = session.get(url_login)
        cookie_str = session.cookies.get_dict()
        cookies = 'JSESSIONID=' + cookie_str['JSESSIONID']
        print('获取到的cookies值为：' + cookies)
        '''登录完成'''
     
     
        '''获取sign签名'''
        def get_data():
            url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroom/getbesktimelist'
        #根据阅览室编号获取sign值，如下是七楼大厅的beskids和roomid
            data = {
                'beskids' : beskids,
                'roomid' : roomid,
                }
            try:
                response = requests.post(url,params=data)
                if response.status_code == 200:
                    #print('获取sign到的JSON为： ' +  response.text)
                    return(response.text)
                else:
                    print("sign获取失败")
                    return None
            except RequestException as E:
                print(E)
                print("Except_Error_get_data")
                return None 
             
        
        json_sign = json.loads(get_data())
        sign = (json_sign['Data'][0]['sign'])
        print('获取到该小时内的sign值为： ' + sign)  
         
         
        '''向服务器提交时间认证表单信息'''
        def url_checktime():
            url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroom/checktimecanbesk'
            headers = {
                'Host': 'tsgzwyy.tsnu.edu.cn:8060',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/selectreadingroom',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Length': '5',
                'Connection': 'keep-alive',
                'Cookie': cookies,
                }
            
            form_checktime = {
                'id' : id_time                                    
                }
            try:
                response = requests.post(url,headers=headers,data=form_checktime)
                if response.status_code == 200:
                    return(response.text)
                else:
                    return "时间校验失败"
            except RequestException as E:
                print(E)
                return 'Except_Error_url_checktime'
        print('时间校验成功并已返回： '  + url_checktime())
        
        
         
        '''阅览室列表数据获取'''
        def url_getbeskusedaylist():
            url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroom/getbeskusedaylist'
            headers = {
                'Host': 'tsgzwyy.tsnu.edu.cn:8060',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/selectreadingroom',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Length': '9',
                'Connection': 'keep-alive',
                'Cookie': cookies,
                }
            form_getbeskusedaylist = {
                'beskid' : beskid_1
                }
            try:
                response = requests.post(url,headers=headers,data=form_getbeskusedaylist)
                if response.status_code == 200:
                    return(response.text)
                else:
                    return "获取使用列表失败"
            except RequestException as E:
                print(E)
                return 'Except_Error_url_getbeskusedaylist'
             
        print('阅览室列表校验成功并已返回： ' + url_getbeskusedaylist())
         
         
        ''' 查询表单 '''
        url_readingroomtablelist_url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroomtablelist'
        headers = {
                'Host': 'tsgzwyy.tsnu.edu.cn:8060',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/selectreadingroom',        
                'Connection': 'keep-alive',
                'Cookie': cookies,
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0',
                }
        
        form_readingroomtablelist={
                'roomno':roomno,
                'isuseday':isuseday,
                'begintime':begintime,
                'endtime':endtime,
                'beskid':beskid_2,
                'beskCanId':beskCanId,
                'sign':sign,                                  
                }
        
        response = requests.get(url_readingroomtablelist_url,headers=headers,params=form_readingroomtablelist)
        print(response)
        
        s = '准备预约的座位是：'+  tableno+ '号'
        print (s,file = file)
        # '''提交座位数据'''
        
        def url_postbeskdata():
            global tableid
            mintableid   = tableid-4
            
            url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroom/postbeskdata'    
            headers = {
                'Host': 'tsgzwyy.tsnu.edu.cn:8060',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Content-Length': '114',
                'Origin': 'http://tsgzwyy.tsnu.edu.cn:8060',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/readingroomtablelist?roomno=19&isuseday=1&begintime=07:59:59&endtime=22:00:00&beskid=20&beskCanId=20&sign=' + sign,
                'Cookie': 'SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; ' + cookies,
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                }    
            form_postbeskdata = {
                'roomno':roomno,
                'tableid':str(tableid),
                'tableno':tableno,
                'begintime':begintime,
                'endtime':endtime,
                'beskid':beskid_2,
                'beskCanId':beskCanId,
                }
        
        
            response = requests.post(url,headers=headers,data=form_postbeskdata)
            ReturnValue =json.loads(response.text)["ReturnValue"]
            Reason = json.loads(response.text)["Msg"]
            new_tableno = 34 
            s =  tableno+ '号预约已提交，状态为：' + Reason 
            print (s,file = file)
            while True:
                if ReturnValue == 0:
                    return Reason
                    break
                
                elif ReturnValue == -1:
                    #楼层不变，座位号减1
                    
                    tableid -= 1
                    new_tableno -= 1
                    
                    newtableno   = str('七楼-0' + str(new_tableno))
                    oldtableno   = str('七楼-0' + str(new_tableno-1)) 
                    
                    s = newtableno+ '号预约失败，Reason： ' + Reason + '，尝试预约: '  + oldtableno
                    print (s,file = file)
                    #如果座位号小于设定的座位号，则继续执行座位号加1,继续提交表单
                    if tableid >= mintableid:
                        form_new_postbeskdata = {
                            'roomno':roomno,
                            'tableid':str(tableid),
                            'tableno':newtableno,
                            'begintime':begintime,
                            'endtime':endtime,
                            'beskid':beskid_2,
                            'beskCanId':beskCanId,
                            }
                        response = requests.post(url,headers=headers,data=form_new_postbeskdata)
                        ReturnValue =json.loads(response.text)["ReturnValue"]
                       
                    else:
                        return "没机会了!洗洗睡吧！"
                        
                else:
                    return "2号循环体出错，请检查脚本"
                    
            else:
                return "1号循环体出错，请检查脚本"
                
        
        s = str(url_postbeskdata())
        print(s,file = file)
        file.close()       
        os.system('python3  /www/Library/SendEmail.py')
        break
    else:
#         #填写需要获取时间的web站点
#         url = "http://tsgzwyy.tsnu.edu.cn:8060/"
#         r=requests.get(url)
#         #获取web上的date时间
#         date=r.headers["Date"][17:25]
#         #转换为时间格式
#         time_format=datetime.strptime(date,'%H:%M:%S')
#         #增加8小时转为北京时间
#         time_time = time_format + timedelta(hours=8)
#         print (str(time_time)[11:19])
#         #提取时间中的小时和分钟值并返回
#         time = str(time_time)[11:18]
        url = 'http://tsgzwyy.tsnu.edu.cn:8060/readingroom/checktimecanbesk'
        headers = {
            'Host': 'tsgzwyy.tsnu.edu.cn:8060',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://tsgzwyy.tsnu.edu.cn:8060/selectreadingroom',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '5',
            'Connection': 'keep-alive',
            'Cookie': '',
            }
        
        form_checktime = {
            'id' : id_time                                    
            }
        response = requests.post(url,headers=headers,data=form_checktime)
        time = json.loads(response.text)["Msg"][6:13]
        print(time)
        
'''退出循环'''
