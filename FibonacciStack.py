# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:43:46 2020

@author: ThinkPad
"""

class FibonacciStack :
    def __init__ (self):
        self.items = []
        self.fib_num = 0 # Set initial number as 0
        self.fib = [0,1] # Set first 2 elements of fibonacci sequence
    def push(self, item):
        self.items.append(item)
        if len(self.items) <= 100:
            return True
        else:
            return False
    def pop(self):
        self.fib_num += 1
        self.fib.append(self.fib[self.fib_num - 1] + self.fib[self.fib_num]) # Calculate new fibonacci element
        return self.items.pop() * self.fib[self.fib_num - 1] # the value requested
    def empty(self):
        # back to initial setting.
        self.fib_num = 0 
        self.fib = [0,1]
        self.items = []
    def is_empty (self):
        return (self.items == [])
    