# -*- coding: UTF-8 -*-
"""
问题描述
你有一个盒子，你可以往里面放数，也可以从里面取出数。

初始时，盒子是空的，你会依次做 Q 个操作，操作分为两类：

插入操作：询问盒子中是否存在数 x，如果不存在则把数 x 丢到盒子里。
删除操作：询问盒子中是否存在数 x，如果存在则取出 x。
对于每个操作，你需要输出是否成功插入或删除。

输入
第一行一个正整数 Q，表示操作个数。

接下来 Q 行依次描述每个操作。每行 2 个用空格隔开的非负整数 op,x 描述一个操作：op 表示操作类型，op=1 则表示这是一个插入操作，op=2 则表示这是一个删除操作；x 的意义与操作类型有关，具体见题目描述。

输出
按顺序对所有操作输出，对于每个操作输出一行，
如果成功则输出“Succeeded”（不含引号），
如果失败则输出“Failed”（不含引号）。

"""

total=int(raw_input())
dictBox={}
for _ in range(total):
	cmdStr=raw_input()
	value=cmdStr[2:]
	if cmdStr[0]=='1':
		# insert op
		if dictBox.get(value,None):
			print "Failed"
		else:
			dictBox[value]=1
			print "Succeeded"
	else:
		# delete op
		if dictBox.get(value,None):
			del dictBox[value]
			print "Succeeded"
		else:
			print "Failed"



