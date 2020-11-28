# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:35:52 2020

@author: ThinkPad
"""

class Node: # Create a class of node
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next # point to the next node

class PriorityQueue: # Create Priority Queue class
    def __init__(self):
        self.root = Node() # Set the root node
        self.length = 0 #Set the length of queue
    def is_empty(self): 
        return (self.length == 0) # judge by whether length is 0
    def clear(self): # reset the queue
        self.root = Node()
        self.length = 0
    def insertInQueue(self, content, priority): 
        node = Node([content,priority]) # the new node
        if self.root.next is None: # the first node
            self.root.next = node
        else:
            cur_node = self.root.next # define a current node
            for i in range(self.length):
                if self.root.next == cur_node and cur_node.value[1] > node.value[1]: # the situation add a node after root
                    node.next = self.root.next
                    self.root.next = node
                    break
                elif cur_node.next == None and cur_node.value[1] <= node.value[1]: # the situation add a node at the tail
                    cur_node.next = node
                    break
                elif cur_node.value[1] <= node.value[1] and cur_node.next.value[1] > node.value[1]: #the situation add a node between 2 nodes
                    node.next = cur_node.next
                    cur_node.next = node
                    break
                else:
                    cur_node = cur_node.next # current node turn to the next one if can't add after this temporary one
                    
        self.length += 1 # +1 to the length
    def removeFromQueue(self):
        out = self.root.next.value[0] # the value print out
        self.root.next = self.root.next.next 
        self.length -= 1 # -1 to the length
        return out