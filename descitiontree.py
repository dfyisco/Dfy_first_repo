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
 
# Here's the answer from teacher
from operator import itemgetter # We use this import for sorting

class DecisionTree:
    def __init__(self, data):
        self.data = data
        # I will also store a sorted version of the data. Note that we sort according to the feature, but must maintain the correct labels. 
        self.sortedData = sorted(self.data, key=itemgetter(0)) # Sorting the data using the Python standard library

    # An auxiliary method to find all midpoints between the feature, with the corresponding position in the sortedData list where the split should happen.
    def _findAllMidPoints(self,sortedData):
        listOfMidPoints = [] # Start with an empty list, and add the split points one by one
        splitPosition = 0

        for n in range(len(sortedData)-1):
            splitPosition += 1
            if (sortedData[n][0] == sortedData[n+1][0]): # We need to watch out for repeated items                
                continue
            
            listOfMidPoints.append(((sortedData[n][0] + sortedData[n+1][0])/2,splitPosition)) # A tuple representation, to store the splitting value, and also the position in the list that would correspond to that split.

        return listOfMidPoints

    # Calculates the "purity" of a dataset
    def _calculateGini(self,data):
        numZero = 0
        numOnes = 0

        for item in data:
            if (item[1] == 0): # Second element of each item is the label
                numZero += 1
            else:
                numOnes += 1

        # After calculating the number of items with label 0, and with label 1, it is just a straightforward application of the equation.
        return 1 - (numZero/len(data))**2 - (numOnes/len(data))**2

    # Auxiliary method to return a left and right dataset, with its corresponding gini value, given a certain split point.
    def _split(self,splitPoint,splitValue,sortedData):
        # Dividing the dataset into left and right datasets
        leftSide = sortedData[0:splitPoint]
        rightSide = sortedData[splitPoint:]

        # Calculate the Gini index for each one of them
        leftGini = self._calculateGini(leftSide)
        rightGini = self._calculateGini(rightSide)

        # Returns a weighted summation of the left and right gini, based on the size of those datasets in relation to the full dataset.
        giniValue = (len(leftSide)/len(sortedData))*leftGini + (len(rightSide)/len(sortedData))*rightGini

        return (giniValue,splitValue,leftSide,rightSide)            

    # We need to check for and handle the edge cases
    # Here I am checking if there only items of one of the labels. In that case, there are no further splits.
    def _singleLabel(self,sortedData):
        firstLabel = sortedData[0][1]

        for item in sortedData:
            if (item[1] != firstLabel):
                return False

        return True

    # Here I check if all items have the same feature, as in that case a split cannot be created.
    def _singleFeature(self,sortedData):
        firstFeature = sortedData[0][0]

        for item in sortedData:
            if (item[0] != firstFeature):
                return False

        return True

    def _findBestSplit(self):        
        return self._findBestSplitWithData(self.sortedData)

    # I explicitly pass sortedData here because for the full decision tree it won't necessarily be the same as the original dataset, because of the recursive calls.
    def _findBestSplitWithData(self,sortedData):
        # Step 0: edge cases:
        ## If there is a single label or a single feature value, return False, we don't have to split any further
        if (self._singleLabel(sortedData)):
            return False
        if (self._singleFeature(sortedData)):
            return False
                
        # Step 1: find all midPoints:
        listOfMidpoints = self._findAllMidPoints(sortedData)

        # Step 2: calculate split and gini index
        listOfPotentialSplits = []

        for n in range(len(listOfMidpoints)):
            listOfPotentialSplits.append(self._split(listOfMidpoints[n][1],listOfMidpoints[n][0],sortedData))

        # Step 3: find the solution with minimum gini index

        minimumGini = float("inf")
        minimumGiniPos = 0

        for n in range(len(listOfPotentialSplits)):
            if listOfPotentialSplits[n][0] < minimumGini:
                minimumGini = listOfPotentialSplits[n][0]
                minimumGiniPos = n

        ## Check for duplicates:
        for n in range(len(listOfPotentialSplits)):
            if (listOfPotentialSplits[n][0] == minimumGini) and (n != minimumGiniPos):
                print("Duplicated Solution:")
                print (listOfPotentialSplits[n])
                
        return listOfPotentialSplits[minimumGiniPos]
