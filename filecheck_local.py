#!/usr/bin/env python
#encoding=utf-8

#计算本地文件的sha1sum值

import os #获取环境变量
from subprocess import call
from subprocess import check_call
from hashlib import sha1
from time import clock as now


local_path = os.getenv("local_path")
print 'local_path='+local_path    #test
generate_file = os.getenv("generate_local_name")
print 'generate_file='+generate_file 


#计算sha1sum值,本代码没有使用该方法
def getSha1(filename):
    sha1Obj = sha1()
    with open(filename,'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

def main():
    paths=[]
    paths.append(local_path)
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


