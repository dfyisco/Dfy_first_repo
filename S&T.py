# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 04:09:24 2020

@author: ThinkPad
"""

def stPrinter(n, shape, character, filled, fillCharacter="*"):
    if shape == 0:
        for i in range(n):
            for j in range(n):
                if i != 0 and i != n - 1:
                    if j == 0 or j == n - 1: # left and right side of square
                        print(character, end = "")
                    else: #middle part of the square
                        if filled == True:
                            print(fillCharacter, end = "")
                        elif filled == False:
                            print(" ", end = "")
                else: # up and down side of square
                    print(character, end = "")
                j += 1
            i += 1
            print("\n", end = "") # change the line
    elif shape == 1:
        for i in range(n):
            for j in range(n):
                if i < j: # these parts are not in right-angled triangle
                    print("", end = "")
                elif i == j or j == 0 or i == n - 1: # the sides of triangle
                    print(character, end = "")
                else:
                    if filled == True:
                        print(fillCharacter, end = "")
                    elif filled == False:
                        print(" ", end = "")
                j += 1
            i += 1
            print("\n", end = "")

def main():
    print("Enter n:")
    n = int(input())
    print("Enter your 0 or 1:")
    shape = int(input())
    print("Enter character:")
    character = str(input())
    print("Enter True or False:")
    filled = input()
    print("Enter fill Character:")
    fillCharacter = str(input())
    stPrinter(n, shape, character, filled, fillCharacter)

if __name__ == "__main__":
    main()