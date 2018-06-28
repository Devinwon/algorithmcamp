#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
time exceed >2s
"""


def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low
def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v

total=int(input().strip())
lst=list(map(int,input().strip().split()))
rel = quicksort(lst, left = 0, right = len(lst) - 1)
for v in rel[:-1]:
    print(v,' ',sep='',end='')
print(rel[-1])
