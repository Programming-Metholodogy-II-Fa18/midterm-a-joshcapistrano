# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:38:59 2018

@author: ac1695
"""

class Problem3:
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
        print("Returned value at index " + str(i) + ": ")
        return self.items[i]
        
    def search(self, i):
        for j in range(len(self.items)):
            print("Comparing " +str(self.items[j]) + " with " + str(i))
            if self.items[j] == i:
                print("Found value!")
                return True
        
        
        

        
x = Problem3(10)
x.add(1)
x.add(5)
x.add(8)
x.add(10)
x.add(12)
x.add(14)
x.add(18)
x.add(20)
x.add(33)
x.add(41)
x.search(8)
x.search(33)