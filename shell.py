#!/usr/bin/env python
#encoding=utf-8

import os
from subprocess import call #通过call调用shell命令
from hashlib import sha1    #计算sha1sum值

call(["ls","-l"])

#实现从jenkins环境变量获取值
path=os.getenv("phone_path")
print os.getenv("phone_path")

#实现adb pull,环境变量直接引用不用加引号，用+即可
call(["adb","root"])
call(["adb","pull","/system/lib64/libteec.so",path+"/ree/client/libteec.so_64"])

#实现adb push
#call(["adb","remount"])
#call(["adb","push",path+"/ree/client/libteec.so_64","/system/lib64/libteec.soa"])

#实现adb shell
#call(["adb","root"])
#call(["adb","shell","chmod","-R","777","/system/lib/nutlet_armtz/"])
#call(["adb","shell","./system/lib/nutlet_armtz/nutlet_helloworld"])

#计算sha1sum值
def getSha1(filename): #计算sha1
    sha1Obj = sha1()
    with open(filename,'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

print getSha1(path+"/ree/client/libteec.so_64")

#下面的调用可以当做一个整体，类似于在终端输入命令，其中间仍然可以调用参数，参数在引号外面
call("sha1sum " + path + "/ree/client/libteec.so_64 > remote_sha1", shell=True)
#call(["sha1sum",path+"/ree/client/libteec.so_64",">","remote_sha1"])


print 'ok'
