**0wd3**

#print在python2中python3的区别

## print在3中的变化

-python2 中print是一个命令，输入格式： print xxx

- python3 print命令多了一个（）：print（xxx)

一个括号带来了什么区别？
实质是print以函数的方式调用

**0wd4**

##探索记录

- 进一步对照print在P3中的应用

在练习8中有详细示例，print以函数运行，在P3中想调用调试信息，也开始采用调用函数的方法。
如
> formatter = "{}{}{}{}"
  print(formatter.format(1,2,3,4))

## rawinput()变为input()

- jupyternote安装（1h)
最简单的方法就是用anaconda安装，不用折腾，科学上网安装下载速度更快。
