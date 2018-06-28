#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
complement by priority queue
done
"""

import heapq

wordsNum=int(input().strip())
wordFre=[]
for _ in range(wordsNum):
	wordFre.append(int(input().strip()))

# Transform list into a heap, in-place, in O(len(heap)) time.
heapq.heapify(wordFre)

cost=0
while len(wordFre)>1:
	smallFirst=heapq.heappop(wordFre)
	smallSecond=heapq.heappop(wordFre)
	temp=(smallFirst+smallSecond)
	cost+=temp
	if wordFre:
		heapq.heappush(wordFre, temp)

# now only one elment on wordFre
if len(wordFre)==1:
	last=heapq.heappop(wordFre)	
	cost+=last
print(cost)





# print (heapq.heappop(wordFre))
