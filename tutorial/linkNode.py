class LinkNode():
	"""docstring for LinkNode
	default parameter located in __init__(),not essential 
	linkList store students' score

	def __init__(self,score=0,name=None):
		self.score = score
		self.name = name
	"""
	def __init__(self):
		self.name = ""
		self.score = 0
		self.next=None


# 建立链表头部
head=LinkNode()

# 当前没有下一个元素
head.next=None

# 设置存取指针的位置
ptr=head

total=int(input("学生的总数是: "))
for _ in range(total):
	data=LinkNode()
	data.name=input("学生姓名: ")
	data.score=input("学生成绩: ")
	ptr.next=data 	# 存储指针为新元素所在的位置
	print()
	data.next=None	# 下一个元素的next设置为None
	ptr=ptr.next		# 移动(更新)ptr

# 遍历单项链表

print("姓名\t成绩")
ptr=head.next			# 从链表的头部开始,注意这里不能是head,head中存储的是初始化数据
while ptr!=None:
	nm=ptr.name
	score=ptr.score
	print("%s  %s"%(nm,score))
	ptr=ptr.next # 移动(更新)ptr


		