import math
import numpy as np
import itertools
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def lcm(nums):
    totalFactors = []
    lcm = 1
    c = 0
    y = 0
    for x in nums:
        totalFactors.append([])
        totalFactors[c] = primeFactors(x)
        c += 1
    print(totalFactors)
    while y < len(totalFactors):
        for x in totalFactors[y]:
            if lcm % x != 0 or lcm % pow(x, totalFactors[y].count(x)) != 0 :
                lcm = lcm * x
        y += 1
    print(lcm)

def primeFactors(num):
    primeFactorList = []
    while num != 1:
        for i in range(2, num + 1):
            if (num % i) == 0:
                primeFactorList.append(i)
                num = (int(num / i))
                break
    return(primeFactorList)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Sudoku:
    board = [[], [], [], [], [], [], [], [], []]
    def __init__(self, game):
        self.game = game
    def fullBoard(self):
        for x in range(0, 81):
            Sudoku.board[math.floor(x/9)].append(self.game[x])
        print(np.matrix(Sudoku.board))
    def getRow(self, row):
        print(Sudoku.board[row])
    def getCol(self, col):
        colMatrix = []
        for y in range(0, 9):
          colMatrix.append(Sudoku.board[y][col])
        print(colMatrix)
    def getSqr(self, row, col):
        print(Sudoku.board[row][col])
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def canPayCost(manaPool, cost):
    x=0
    anyMana = ""
    while cost[x].isdigit():
        anyMana += cost[x]
        x+=1
    anyMana = int(anyMana)
    for c in manaPool:
        if c in cost:
            cost = cost.replace(c, "", 1)
        elif anyMana > 0:
            anyMana -= 1
            if anyMana <= 0:
                for y in range(0,x):
                    cost = cost[1:]
    if cost != "":
        return False
    else:
        return True
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def digits(number):
    totalDigits = 0
    n = len(str(number))
    digits = n * number
    for x in range (0, n):
        digits -= pow(10, x)
    return digits
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def crackPincode(pincode):
    possibleNumbers = [
        ["8", "0"], #0
        ["1", "2", "4"], #1
        ["1", "2", "3", "5"], #2
        ["2", "3", "6"], #3
        ["1", "4", "5", "7"], #4
        ["2", "4", "5", "6", "8"], #5
        ["3", "5", "6", "9"], #6
        ["4", "7", "8"], #7
        ["5", "7", "8", "9", "0"], #8
        ["6", "8", "9"], #9
    ]
    combs = []
    for x in pincode:
        combs.append(possibleNumbers[int(x)])
    combs = [p for p in itertools.product(*combs)]
    combs.sort()
    return combs

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////