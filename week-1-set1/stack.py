# -*- coding: UTF-8 -*-
"""
描述
实现一个栈，完成以下功能：

入栈
出栈
询问栈中位置Y是谁

一开始栈为空。栈中的位置从1开始（即栈底位置为1）。

输入
第一行一个整数n，表示操作个数。

接下来n行，每行第一个数字表示操作（见描述）：

若为数字1，则接下来有一串字符串X，表示将X压入栈中。
若为数字2，表示弹出栈顶（保证栈非空），并输出出栈的这个人。
若为数字3，则接下来有一个整数Y，表示询问栈中位置Y是谁（保证位置Y合法），并输出名字。
输出
将所有操作2和操作3输出，一行一个。

-----解题说明:

将需要检索的位置存储在列表locLst中,在下次弹出前,
检查列表不为空的情况下,将栈中部分元素(取决于最小检索位置)弹出至临时列表中lsTemp,
然后通过临时列表索引访问需要检索的的元素,这样迅速,不然会超时,最后清空检索列表

所有操作命令执行完毕后,检查locLst不为空下,执行上述步骤,打印检索结果

-----

"""

# define exception
class StackUnderflow(ValueError):
	pass

# define stack()
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

	def empty(self):
		return self._element==[]

def printValueByIndex(st,locLst,length):
	lsTemp=[]

	# 栈中剩下不弹出的元素数量
	leftInst=min(locLst)-1
	for _ in xrange(length-leftInst):
		lsTemp.append(st.pop())
	for l in locLst:
		print lsTemp[leftInst-l]

	while lsTemp:
		st.push(lsTemp.pop())


count=int(raw_input())
st=Stack()
length=0
locLst=[]
for _ in xrange(count):
	cmdStr=raw_input()
	# in stack
	if cmdStr[0]=='1':
		st.push(cmdStr[2:])
		length+=1

	# out stack
	elif cmdStr[0]=='2':
		if locLst==[]:
			print st.pop()
			length-=1
		else:
			# process before strive
			printValueByIndex(st,locLst,length)
			locLst=[]

			# process prompt command
			print st.pop()
			length-=1

	# store loc in locLst		
	elif cmdStr[0]=='3':
		loc=int(cmdStr[2:])
		locLst.append(loc)

if locLst:
	printValueByIndex(st,locLst,length)
	locLst=[]


