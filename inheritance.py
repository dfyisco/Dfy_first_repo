# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:08:51 2020

@author: ThinkPad
"""

class Stack :
    def __init__ ( self ):
        self.items = 100*[0];
        self.position = 0;
    def push (self, item):
        if (self.position < 100) :
            self.items[self.position] = item ;
            self.position = self.position + 1;
            return True ;
        else :
            return False ;
    def pop(self):
        if (self.position <= 0):
            return False ;
        else :
            self.position = self.position - 1;
            return self.items[self.position];
    def empty(self):
        self.position = 0;
    def is_empty(self):
        return (self.position == 0)
    
class Node :
    def __init__(self, content =None, next = None):
        self.content = content
        self.next = next
        
class Queue :
    def __init__(self):
        self.length = 0
        self.head = None
    def is_empty(self):
        return self.length == 0
    def clear(self):
        self.length = 0
        self.head = None
    def insert(self, content):
        node = Node(content)
        if self.head is None :
            #If list is empty the new node goes first
            self.head = node
        else :
            # Find the last node in the list
            last = self.head
            while last.next :
                last = last.next
                # Append the new node
            last.next = node
        self.length = self.length + 1
    def remove(self):
        content = self.head.content
        self.head = self.head.next
        self.length = self.length - 1
        return content

class FibonacciStack(Stack): # Inherit from class Stack
    def __init__(self):
        Stack.__init__(self) # inheritance
        # For keeping track of Fibonacci Sequence. Note that these attributes allow us to get the next number without having to re-calculate the whole sequence.
        self.previous = 1 #set the first 2 numbers in sequnce
        self.secondPrevious = 0
        self.numRemoved = 0 
    def pop(self):
        if (self.position <= 0):
            return Stack.pop(self);
        else:
            self.position = self.position - 1
            content = self.items[self.position]     
        ## Here we must modify the number
        if (self.numRemoved == 0):
            self.numRemoved = self.numRemoved + 1
            return 0 * content
        if (self.numRemoved == 1):
            self.numRemoved = self.numRemoved + 1
            return 1 * content
        ## From here on, we must keep track of the Fibonacci Sequence
        if (self.numRemoved > 1):
            tmp = self.previous + self.secondPrevious
            self.secondPrevious = self.previous
            self.previous = tmp
            return tmp*content
        ## We should never reach here. If we return False, then something is wrong
        return False
    def empty(self): # reset the sequence
        Stack.empty(self) # What father have
        self.previous = 1 # son's new items
        self.secondPrevious = 0
        self.numRemoved = 0

class PriorityQueue(Queue):
    def insert(self, content, priority):
        Queue.insert(self,[content,priority])
    def remove(self):
        # First I will go over the queue, in order to discover the current highest priority
        # 1 is the highest. 2 is lower than 1.
        # I assume that no item would have "0" or negative priority.
        
        # Obs 1: It should be possible to modify the insert method, so that this step is not necessary.
        # Obs 2: It should also be possible to already find the correct node at this step. However,
        # I will go over the list two times for the code to be clear
        currentNode = self.head
        highestPriority = self.head.content[1]
        
        while (currentNode != None):
            if (currentNode.content[1] < highestPriority):
                highestPriority = currentNode.content[1]
            currentNode = currentNode.next
        # So now the highestPriorityFound holds the highest priority that exists in the queue.
        # Hence, now I just need to find the first node (since the Queue is in order of arrival)
        # which holds that priority    
        currentNode = self.head
        previousNode = None
        found = False
        
        while (found == False):
            if (currentNode.content[1] == highestPriority):
                # If the node should be removed is found, then remove it
                out = currentNode.content[0]
                
                if (previousNode == None): #If this node is the head of the queue
                    self.head = self.head.next
                else: #If there is a previous node
                    previousNode.next = currentNode.next
                self.length = self.length - 1
                
                return out
            # Prepare for next iteration
            previousNode = currentNode
            currentNode = currentNode.next
        return -999 #If return -999, sth got wrong