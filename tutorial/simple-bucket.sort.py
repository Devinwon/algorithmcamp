"""
简单桶排序
字典是无序的
列表实现
"""
rsc=[23,12,34,56,6,89,10,100,72,56]


print("before")
print(rsc)
rel=[]
for i in range(max(rsc)+1):
	rel.append(0)
for v in rsc:
	rel[v]+=1

print("after-ascend")
for i in range(len(rel)):
	if rel[i]:
		for _ in range(rel[i]):
			print(str(i),' ',end='')
print()

print("after-decend")
for j in range(len(rel)-1,-1,-1):
	if rel[j]:
		for _ in range(rel[j]):
			print(str(j),' ',end='')
print()



