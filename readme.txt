从SVNcheck代码到本地，在本地编译ta和ca，然后将生产的文件.ta push到手机中，通过adb shell（在ant中调用shell脚步实现）执行ca的生成文件，可以在控制台看到结果。见consoleText附件。
相应的build.xml和adb.sh。