# -*- coding:UTF-8 -*-
"""
描述
实现一个队列，完成以下功能：

入列
出列
询问队列中位置Y是谁
一开始队列为空。队列中的位置从1开始（即队头位置为1）。

输入
第一行一个整数n，表示操作个数。

接下来n行，每行第一个数字表示操作（见描述）：

若为数字1，则接下来有一串字符串X，表示将X加入队列。
若为数字2，表示出列（保证队列非空），并输出出列的这个人。
若为数字3，则接下来有一个整数Y，表示询问队列中位置Y是谁（保证位置Y合法），并输出名字。
输出
将所有操作2和操作3输出，一行一个。

empty()
not_empty()

# in queue
put()    

# out queue
get() 

qsize() 

分左右半区域查找,以免超时
"""

class Queue():
	_element=[]
	def __init__(self, ):
	  self._element=[]

	def put(self,v):
		self._element.append(v)

	def putLeft(self,v):
		self._element.insert(0,v)

	def get(self):
		# remove and  return  elemnt in head
		if self._element==[]:
			raise StackUnderflow("in get()")
		head=self._element[0]
		self._element=self._element[1:]
		return head

	def getRight(self):
		if self._element==[]:
			raise StackUnderflow("in pop()")
		return self._element.pop()

	def qsize(self):
		return len(self._element)


def printValueByIndex(q,locLst):
	lsTemp=[]

	if max(locLst)<q.qsize()/2:
		for _ in xrange(max(locLst)):
			lsTemp.append(q.get())

		for loc in locLst:
			print lsTemp[loc-1]

		while lsTemp:
			q.putLeft(lsTemp.pop())

	# elif min(locLst)>=q.qsize()/2 :
	else:
		gap=min(locLst)
		for _ in xrange(gap,q.qsize()+1):
			lsTemp.append(q.getRight())

		for v in locLst:
			print lsTemp[-(v-gap+1)]

		while lsTemp:
			q.put(lsTemp.pop())


que=Queue()
count=int(raw_input())
locLst=[]

for _ in xrange(count):
	cmdStr=raw_input()
	# in queue
	if cmdStr[0]=='1':
		que.put(cmdStr[2:])

	# out que
	elif cmdStr[0]=='2':
		if locLst==[]:
			print que.get()
		else:
			# process before strive
			printValueByIndex(que,locLst)
			locLst=[]
			# process prompt command
			print que.get()

	# store loc in locLst		
	elif cmdStr[0]=='3':
		loc=int(cmdStr[2:])
		locLst.append(loc)

if locLst:
	printValueByIndex(que,locLst)
	locLst=[]





