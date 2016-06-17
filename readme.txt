通过不同参数执行不同的编译环境，不用手动修改MakeFile。
在job配置中，勾选参数化构建过程，选择extend choice parameter（需要安装extended choice parameter 插件）或者choice parameter，目前感觉效果一样。
这个参数可以在execute shell中调用：echo ${ta_path}
也可以在ant中直接调用具体在build.xml在compile过程中使用。