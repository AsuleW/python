#!/usr/bin/python
# -*- coding:UTF-8 -*-

import socket,time,thread
socket.setdefaulttimeout(3) #设置默认超时时间
Money = 2000

def modify_global_var():
    global Money
    #如果要修改全局变量则必须申明 该全局变量 global var
    x = Money
    x += 100
    Money = x

def for_loop():
    tup=(1,2,3,4,5,6)
    #元组中的元素不可修改
    x=5
    for i in tup:
        print "currnet elem:",i
        if i ==x :
            print "elem x:",x,"in tuple"

def modify_list():
    list=[1,2,3,4,5,6,7,8]
    index=5
    target=10
    for i in list:
        print "curent elem:",i
        if list.index(i) == index:
            list[list.index(i)] = target
    print "list :",list

def modify_dict():
    dict={'k1':'v1','k2':'v2','k3':'v3'}
    print 'before modify dict elem:',dict
    dict['k2']='modify'
    print 'after modify dict elem:',dict          

def while_loop():
    count = 0
    while (count < 4):
        print 'The count is:', count
        count = count + 1


def operator_time():
    localtime=time.localtime(time.time())
    print "local time:",localtime
    formattime = time.asctime( time.localtime(time.time()) )
    print "local time(format):",formattime
    # 格式化成2016-03-20 11:45:39形式
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

class Base:
    __private_var = 0   #私有变量
    _protect_var = 0    #保护变量
    public_var = 0      #公开变量
 
    def prt(self,str):
        print str,": private: ",self.__private_var," protect: ",self._protect_var," public:",self.public_var
    def count(self,nr):
        self.__private_var += (nr+1)
        self._protect_var +=(nr+2)
        self.public_var += (nr+3)

def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否占用
    """
    try:
        if port >=65535:
            print u'端口扫描结束'
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip, port))
        if result==0:
            lock.acquire()
            print ip,u':',port,u'端口已占用'
            lock.release()
    except:
        print u'端口扫描异常'

def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print u'开始扫描 %s' % ip
        start_time=time.time()
        for i in range(0,65534):
            thread.start_new_thread(socket_port,(ip, 5))
        print u'扫描端口完成，总共用时：%.2f' %(time.time()-start_time)
#       raw_input("Press Enter to Exit")
    except:
        print u'扫描ip出错'

if __name__ == '__main__':
    url=raw_input('Input the ip you want to scan: ')
    lock=thread.allocate_lock()
    ip_scan(url)
    #operator_time()
    #modify_global_var()
    #for_loop()
    #while_loop()
    #modify_list()
    #modify_dict()
    #var=10
    #baseobj = Base()
    #baseobj.prt("before")
    #baseobj.count(var)
    #baseobj.prt("after")