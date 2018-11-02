# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:03:13 2018

@author: ac1695
"""

def merge(a,b):
    c = []
    indexA = 0
    indexB = 0
    
    
    while indexA < len(a) and indexB <len(b):
        if a[indexA] < b[indexB]:
            c.append(a[indexA])
            indexA+=1
        else:
            c.append(b[indexB])
            indexB+=1
            
    if indexA == len(a):
        c.extend(b[indexB:])
    else:
        c.extend(a[indexA:])
    return c
        
def Problem1Sort(x):
    if len(x) <= 1:
        return x
    
    mid = len(x) // 2
    
    left = Problem1Sort(x[:mid])
    right = Problem1Sort(x[mid:])
    a = merge(left,right)
    return a
    
y = [15,9,60,44,12,1,4]

print(Problem1Sort(y))