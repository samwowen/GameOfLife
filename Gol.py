# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 21:57:51 2016

@author: SamOwen

Conway's game of life, made for a bit of fun
"""
import numpy as np
import time


class InputError(Exception):
    
    def __init__(self, string):
        self.s = string
    
    def __str__(self):
        return 'Input must be a numpy array at least 2x2, also: ' + self.s

class Gol:
    """Game of life"""

    def __init__(self, board):
        """Define the game board on init as a numpy array as its similar to use as matlab"""
        if type(board) != np.ndarray:
            raise InputError('!= np array')
        else:
            self.board = board
            self.x = np.shape(self.board)[0]
            self.y = np.shape(self.board)[1]
            self.generation = 0
            print(board)


    def iterate(self, t):
        """Takes int t, the GOL iterates t times with a second between each iteration"""
        for o in range(t):
            self.generation += 1
            self.next = np.zeros((self.x, self.y))
            
            for i in range(self.x):
                for j in range(self.y):
                    n = 0
                    en = 0
                    try:
                        if i-1 < 0 or j-1 < 0:
                            raise IndexError
                        if self.board[i - 1, j - 1] == 1:
                            n+=1
                    except IndexError:
                        en += 1
                    try:
                        if j-1 < 0:
                            raise IndexError
                        n = n + 1 if self.board[i, j-1] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        if j-1 < 0:
                            raise IndexError
                        n = n + 1 if self.board[i+1, j-1] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        n = n + 1 if self.board[i+1, j] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        n = n + 1 if self.board[i+1, j+1] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        n = n + 1 if self.board[i, j+1] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        if i-1 < 0:
                            raise IndexError
                        n = n + 1 if self.board[i-1, j+1] == 1 else n
                    except IndexError:
                        en += 1
                    try:
                        if i-1 < 0:
                            raise IndexError
                        n = n  + 1 if self.board[i-1, j] == 1 else n
                    except IndexError:
                        en += 1
                    #print i,j,' : ',n
                    
                    if n == 3.:
                        self.next[i, j] = 1
                        
                    if self.board[i, j] == 1:
                        #print 1
                        if n < 2 or n > 3:
                            #print 0
                            self.next[i, j] = 0
                        else:
                            self.next[i, j] = 1
                        
            self.board = self.next
            print(self.next)
            print ' '
            time.sleep(1)


"""Example"""
g = Gol(np.array([[1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
g.iterate(10)



    