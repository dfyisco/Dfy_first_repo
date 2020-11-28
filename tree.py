# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:08:49 2020

@author: ThinkPad
"""

class Tree :
    def __init__(self, content, left = None, right = None):
        self.content = content
        self.left = left
        self.right = right
        
def sum_tree(tree): # define a function calculate the sum of the tree
    SUM = 0 # set the original value as 0
    if tree != None:
        SUM += tree.content # add the root 
        SUM += sum_tree(tree.left) # add the left leave
        SUM += sum_tree(tree.right) # add the right leave
    return SUM

def leave(tree): # define a function calculate the number of nodes of tree
    if tree == None: # if the tree is None
        return 0 
    elif tree.left == None and tree.right == None: # if the node don't have child
        return 1
    else:
        return (leave(tree.left) + leave(tree.right)) + 1 # sum the num of nodes

def average(tree):
    return sum_tree(tree) / leave(tree) #calculate the average value on every nodes in the tree

#For example
#t = Tree(10, Tree(2,None,None), Tree(3,Tree(4,None,None),Tree(5,None,None)))



