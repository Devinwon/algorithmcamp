#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input().strip())
if n==1:
	print('01')
elif n==2:
	print('0110')
elif n==3:
	print('01011100')
else:
	rel=[0]*(2**n)
	print(''.join(list(map(str,rel))))
