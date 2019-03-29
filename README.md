# LibraryScript
写了一个图书馆抢座位的脚本，大概支持8个学校，代码没有优化，这个是雏形，供交流学习

#环境是python3以上
我是在win10下运行，大家可以在服务器上跑

测试抢座成功后的输出如下：
获取到的cookies值为：JSESSIONID=B97672684733A7298A9136EC4AF0F2FE
获取sign到的JSON为： {"Data":[{"beginTime":"14:35:00","beskCanId":1,"endTime":"17:20:00","id":21,"isUseDay":0,"roomName":"捐赠书借阅处","roomNo":1,"sign":"5d821bcddc14d370f27f8f92139030d9"}],"Msg":"获取成功","ReturnValue":0}
获取到该小时内的sign值为： 5d821bcddc14d370f27f8f92139030d9
时间校验成功并已返回： {"CanBaskID":"1","Msg":"认证通过","ReturnValue":0}
阅览室列表校验成功并已返回： {"Data":[{"usedayid":0,"usedayname":"2019-03-29"}],"Msg":"获取成功","ReturnValue":0}
<Response [200]>
座位请求已提交并返回： {"Msg":"预约成功","ReturnValue":0}

交流QQ:1947719574
个人博客：https://blog.netimed.cn

