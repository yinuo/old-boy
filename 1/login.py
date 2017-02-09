#/usr/bin/env python3
# -*- coding: utf-8 -*-

#@Time		: 2017-02-09
#@Author	: ZhangLi
#@File		: login.py


import getpass

# Variable
count = 0

# Main

while count < 3:
	name = input('请输入用户名：')
	pwd = getpass.getpass('请输入密码：')
	if name == "zhangli" and pwd == "123456":
		print("欢迎， %s !" % name)
		break
	else:
		print("用户名或密码错误，请重新输入！")
	count += 1

else:
	print("超过三次， 账号锁定！")
