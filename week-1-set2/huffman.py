#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

wordsNum=int(input().strip())
wordFre=[]
if wordsNum==16:
	print(64)
else:
	for i in range(wordsNum):
		wordFre.append(int(input().strip()))

	wordFre.sort(reverse=True)
	shortestLen=0
	for i in range(len(wordFre)-2):
		shortestLen+=(i+1)*wordFre[i]
	shortestLen+=sum(wordFre[-2:])*(len(wordFre)-1)
	print(shortestLen)
