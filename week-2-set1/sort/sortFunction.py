#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
描述
给出n个整数，将它们从小到大排序后输出。

输入
第一行为一个正整数n，第二行为n个整数。

输出
输出一行n个整数，表示排序后的n个整数。

case:
5
5 4 2 3 -1
"""
total=int(input().strip())
lst=list(map(int,input().strip().split()))
lst.sort()
for v in lst[:-1]:
	print(v,' ',sep='',end='')
print(lst[-1])