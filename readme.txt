将待编译的源代码放在SVN上，
ant会自动将代码拷贝到/home/archermind/jenkins/public/compile/ca/nutlet_helloworld/jni/host

在/home/archermind/jenkins/public/compile/ca/nutlet_helloworld执行ndk-build命令

由于在Android.mk中使用了通配符，可以不用修改这个文件就可以自动生成。
这个生成的文件名默认为helloworld在/home/archermind/jenkins/public/compile/ca/nutlet_helloworld/libs/arm64-v8a

会自动拷贝到dest/ca中。