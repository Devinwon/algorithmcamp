# -*- coding: UTF-8 -*-
"""
栈排序

时间限制：1 sec

空间限制：256 MB

问题描述
给定一个序列 A，请你将它升序排序。

输入格式
第一行一个正整数 n，表示序列长度。

第二行 n 个用空格隔开的非负整数，描述这个序列。

输出格式
n 行，每行一个非负整数，表示排序后的序列。

样例输入:
4
1 3 2 10

样例输出
1
2
3
10

数据范围
保证 n<=1000，保证序列中的数不超过 32767

提示
请使用课堂中讲解的栈排序来完成此题。

为了帮助大家完成题目，
我们提供了只包含了输入输出功能的程序模板，也提供了含有算法的大部分实现细节的程序。
"""
class StackUnderflow(ValueError):
	pass

class Stack():
	_element=[]
	def __init__(self, ):
	  self._element=[]

	def push(self,v):
		self._element.append(v)

	def pop(self):
		if self._element==[]:
			raise StackUnderflow("in pop()")
		return self._element.pop()

	def top(self):
		if self._element==[]:
			raise StackUnderflow("in top()")
		return self._element[-1]

	def is_empty(self):
		return self._element==[]

length=int(raw_input())
lst=list(map(int,raw_input().split(' ')))
st=Stack()
for v in lst:
	st.push(v)

stSorted=Stack()

while not st.is_empty():
	temp=st.pop()
	if stSorted.is_empty():
		# 首次为空直接插入
		stSorted.push(temp)
	else:
		while True:
			# 不为空,进行循环比较
			if stSorted.is_empty() or stSorted.top()<=temp:
				stSorted.push(temp)
				break
			else:
				st.push(stSorted.pop())
			# 这里需要比较弹出首元素后 stSorted.top()与temp的大小关系

rel=[]
while not stSorted.is_empty():
	rel.append(str(stSorted.pop()))
print '\n'.join(rel[::-1])


