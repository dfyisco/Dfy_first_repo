# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 03:32:07 2020

@author: ThinkPad
"""

def crazyRecur(x):
    a = [0, -1, -2] # set initial elements
    display(a, -3, 0, x) # recursive function
    list1 = a[:x]
    print((',').join(str(x) for x in list1))


def display(a, b, reset, x): # build recursive function
    if x <= 3:
        return a[:x]
    else:
        b = a[-1] + a[-2] + a[-3] # the new element is sum of 3 previous elements
        if b >= -125: 
            a.append(b) # add new elements
            display(a, b, reset, x-1)
        else: #reset if series's value is under -125
            reset += 1 # calculate reset times
            b = reset + 10 
            a.append(b)
            display(a, b, reset, x - 1)



def main():
    print("Enter your x:", end=" ")
    x = int(input())
    crazyRecur(x)


if __name__ == "__main__":
    main()