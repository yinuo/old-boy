#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time		: 2017-2-9
# @Author	: ZhangLi
# @File		: menu.py


menu = {
	'北京':{
		'海淀':{
			'五道口':{
				'soho':{},
				'网易':{}
			},
			'上地':{
				'百度':{},
				'民贷天下':{}
			}
		},
		'朝阳':{
			'雍和宫':{
				'易买车':{},
				'Admaster':{}
			},
			'大望路':{
				'神奇时代':{},
				'看书网':{}
			},
			'望京':{
				'乐视':{},
				'360':{}
			}
		}
	},
	'河北':{
		'沧州':{
			'东光':{
				'信和商厦':{}
			},
			'泊头':{
				'泊头一中':{}
			}
		},
		'唐山':{
			'路北':{
				'唐山学院':{},
				'心怡网吧':{}
			},
			'丰润':{
				'冀东石油':{}
			}
		}
	},
	'山东':{
		'德州':{
			'市政府':{},
			'公园':{}
		},
		'济南':{
			'山东大学':{},
			'医院':{}
		}
	},
	'上海':{
		'闵行':{
			"人民广场":{},
			"炸鸡店":{}
		},	
		'闽北':{
			"火车站":{},
			"携程":{}
		}
	}
}

current_level = menu
current_list = [menu]

while True:
	for k in current_level:
		print(k)
	print("返回上一级?(b) 退出?(q)")
	choice = input(">>:").strip()
	if choice == "q":
		break
	elif choice == "b":
		if current_list:
			current_level = current_list[-1]
			current_list.pop()
		else:
			print("已处于最高级，无法返回上一级!")
	elif choice not in current_level:
		print("输入非法")
		continue
	else:
		current_list.append(current_level)
		current_level = current_level[choice]
	
	
