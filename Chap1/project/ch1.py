#!/user/bin/env python3
#coding:utf-8

import sys
from sys import exit
filename = "weather_info.txt"

print('输入城市名查询天气，或输入“help“查看用户帮助指南，或输入“quit”退出程序')

weather_dict = {}
history_dict = {}
# 将读取文件内容，存入字典

with open("weather_info.txt") as file:
   for info in file.readlines():   
        city = info.split(',')[0]
        weather = info.split(',')[1].rstrip('\n')
        weather_dict[city] = weather  

while True:
	   user_input = input('请输入指令或输入城市名：')
	   if user_input in weather_dict.keys():
                    weather = weather_dict[user_input]
                    history_dict[user_input] = weather #保存查询结果
                    print('{}的天气状况为：{}'.format(user_input, weather))#显示查询结果
        
	   elif user_input == 'help':
	       print("""
		    Tips:
		    - 输入城市名，查询该城市天气数据；
		    - 输入指令help,打印帮助文档；
		    - 输入指令quit, 退出程序交互。
		    """)
	   elif user_input == 'quit' or user_input == 'q':
	       print("退出程序") 
	       for user_input in history_dict:
	            print(user_input, history_dict[user_input])
	       break
	   else:
	       print("没有该城市信息！请输入help查看帮助文档或quit退出")



