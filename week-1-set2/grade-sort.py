#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
{		1: [95, 85], 
		2: [90, 90], 
		3: [100, 99]}

result:75%,passed

"""
stuTotal=int(input())
gradeLst=[]
for i in range(stuTotal):
	gradeLst.append([(i+1),list(map(int,input().strip().split()))])

rel=sorted(gradeLst,key=lambda x:(-sum(x[1]),-x[1][0]))
idLst=[]
for v in rel:
	idLst.append(v[0])
	print (v[0],sum(v[1]),v[1][0],v[1][1])



# 统计逆序对,并输出
unOrder=0
for i in range(len(idLst)-1):
	if idLst[i]>max(idLst[i+1:]):
		unOrder+=len(idLst[i+1:])
		continue
	elif idLst[i]<min(idLst[i+1:]):
		continue
	for j in range(i+1,len(idLst)):
		if idLst[i]>idLst[j]:
			unOrder+=1
print(unOrder) 
