# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:56:04 2020

@author: ThinkPad
"""

class DecisionTree():
    def __init__(self, data):
        self.data = data
    def _findBestSplit(self):
        l = []
        split_point = []
        All = [] # record all the output
        gini = [] # record the gini index
        length= len(self.data)
        dataset = self.data
        sum_class = 0
        for i in range(length):
            sum_class += dataset[i][1]
            l.append(dataset[i][0])
        if sum_class == 0 or sum_class == length or len(set(l)) == 1: #if all item belong to same class, return False
            return False
        for index in range(length):
            for j in range(1, length - index):
                if dataset[j-1][0]>dataset[j][0]:
                    dataset[j-1], dataset[j] = dataset[j], dataset[j-1]
        # sort the data from min to max by bubble_sort
        L = list(set(l)) # remove the repetitive elements
        for index in range(len(L)): # sort the list L
            for j in range(1, len(L) - index):
                if L[j-1]>L[j]:
                    L[j-1], L[j] = L[j], L[j-1]
        for i in range(len(L) - 1):
            split_point.append((L[i+1] + L[i])/2) # calculate and record the split point
        for k in range(len(split_point)):
            left = []
            right = []
            for j in dataset: # split the node
                if split_point[k] > j[0]: # go to left leaf if less than split
                    left.append(j) 
                else: # go to right leaf if larger than split
                    right.append(j)
            # calculate the partition in each class
            left_zero = 0
            left_one = 0
            right_zero = 0
            right_one = 0
            for m in left:
                if m[1] == 0:
                    left_zero += 1
                else:
                    left_one += 1
            for n in right:
                if n[1] == 0:
                    right_zero += 1
                else:
                    right_one += 1
            # calculate the gini index
            gini_left = 1 - (left_zero/len(left))**2 - (left_one/len(left))**2 #gini index in left node
            gini_right = 1 - (right_zero/len(right))**2 - (right_one/len(right))**2 # gini index in right node
            gini_index = (len(left)/len(self.data))*gini_left + (len(right)/len(self.data))*gini_right
            gini.append(gini_index)
            All.append([gini_index, split_point[k], left, right]) # form the output together
        num = gini.index(min(gini)) # get where is the minimum gini
        return (All[num][0], All[num][1], All[num][2], All[num][3])  