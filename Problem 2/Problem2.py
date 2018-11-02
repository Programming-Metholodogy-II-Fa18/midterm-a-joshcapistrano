# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:14:41 2018

@author: ac1695
"""

class Problem2:
    def __init__(self , size):
        self.items = [None] * size
        self.size = 0
    
    def add(self, i):
        self.items[self.size] = i
        self.size+=1
        
    def remove(self):
        temp = self.items[0]
        self.items[0] = None
        print(str(temp) + " removed,")
        return temp
        
    def getValue(self , i):
        if i > len(self.items):
            return -1
        print("Returned value at index " + str(i) + ": ")
        return self.items[i]
        

a = Problem2(6)
a.add(1)
a.add(9)
a.add(4)
a.add(5)
a.add(10)
a.add(0)
print(a.getValue(0))
print(a.getValue(3))