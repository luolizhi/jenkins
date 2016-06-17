#!/usr/bin/env python
#encoding=utf-8

#计算本地文件的sha1sum值

import os #获取环境变量
from subprocess import call
from subprocess import check_call
from hashlib import sha1
from time import clock as now


remote_path = os.getenv("remote_path")
print 'remote_path=' + remote_path    #test
generate_file = os.getenv("generate_remote_name")
print 'generate_file='+generate_file 
#remote_path = os.getenv("phone_path")
print remote_path

def adbpull():
 #   print '---this is in adbpull---'
    check_call("adb root",shell=True)
    check_call("adb pull /system/lib64/libteec.so " + remote_path + "/ree/client/libteec.so_64", shell=True)
    check_call("adb pull /system/lib/libteec.so " + remote_path + "/ree/client/libteec.so_32", shell=True)
    check_call("adb pull /system/bin/tee-supplicant " + remote_path + "/ree/client/", shell=True)
    check_call("adb pull /system/lib/nutlet_armtz/8aaaf200-2450-11e4-abe20002a5d5c5a1.ta " + remote_path + "/ifaa1.0/", shell=True)
    check_call("adb pull /system/lib/libalipayteeclient.so " + remote_path + "/ifaa1.0/", shell=True)
    check_call("adb pull /system/framework/alipaymanager.jar " + remote_path + "/ifaa1.0/", shell=True) 
    check_call("adb pull /system/lib64/hw/nutlet.mt6755.so " + remote_path + "/keymaster/" ,shell=True)
    #check_call("adb pull /system/lib/nutlet_armtz/b657ba17-b3b3-47f5-b3896b53f30c0baf.ta " + remote_path + "/keymaster/" ,shell=True)


#计算sha1sum值,本代码没有使用该方法
def getSha1(filename):
    sha1Obj = sha1()
    with open(filename,'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

def main():
    adbpull()
    paths=[]
    paths.append(remote_path)
    if os.path.exists(generate_file):
        print 'file has exists'
        check_call("rm "+generate_file,shell=True)
    check_call("touch "+generate_file,shell=True)
    start=now()
    for path in paths:
        for file in os.listdir(path):
#            print file
            real_file=os.path.join(path,file)
            if os.path.isfile(real_file) == True:
                check_call("sha1sum "+real_file+" >> "+ generate_file ,shell=True)
            else:
                paths.append(real_file)

    end=now()
    time_last=end-start
    print '耗时：',time_last,'秒' 
    #check_call('exit 1',shell=True)

if __name__=='__main__':
    main()


