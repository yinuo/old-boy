#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @time		：2017/2/23 
# @Author	：ZhangLi
# @File		: buy_car.py

product_list = [["iphone", 6500], ["ipad", 3400], ["mac", 14000], ["bike", 900], ["apple", 8], ["tv", 1890]]
buy_list = []
salary = int(input("请输入您的工资: "))

while True:
	for index, value in enumerate(product_list):#enumerate用于遍历序列中的元素和下标
		print(index, value[0], value[1])
	
	print("退出购物? (exit) ")
	choice = input("请输入:").strip() #s为字符串，rm为要删除的字符系列 s.strip(rm)删除s字符串开头结尾处
	#当rm为空时，默认删除空白符（包括'\n','\r','\t',''）
	if choice == "exit":
		break
	elif choice.isdigit():
		choice = int(choice)
		if choice > len(product_list) - 1:
			print("物品编号不存在!")
		elif product_list[choice][1] > salary:
			print("买不起，穷逼！快去挣钱去吧！")
		else:
			buy_list.append(product_list[choice])
			salary = salary - product_list[choice][1]
			print("%s放入购物车， 你的钱包还剩%s" %(product_list[choice][0], salary))
	else:
		print("非法输入")

print("你已经买了以下物品： ")
for index, value in enumerate(buy_list):
	print(value[0], value[1])
print("你的工资还剩%s" % salary)
