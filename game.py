#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:29:13 2018

@author: koen
"""

symbols = dict([(0, 'o'), (1, 'x')])
class Game:
    """
    Connect Four (4 op een rij)
    """
    def __init__(self, nrows=8, ncols=8, goal=4):
        self.nrows, self.ncols = nrows, ncols
        self.goal = goal
        self.board = dict(zip([(x,y) for x in range(nrows) for y in range(ncols)], ['.' for ii in range(nrows*ncols)]))
        #self.board = dict(zip([(x,y) for x in range(nrows) for y in range(ncols)], range(nrows*ncols)))
    
    def drop(self, col, player):
        ii = self.nrows-1
        if self.board[(col, self.nrows-1)] != '.':
            raise ValueError('Column {} is full'.format(col))
        while ii > -1 and self.board[(col, ii)] == '.':
            ii -= 1
        self.board[(col, ii+1)] = symbols[player]      
    
    def __str__(self):
        s = ''
        for row in range(self.nrows-1,-1,-1):
            for col in range(self.ncols):
                s += str(self.board[(col, row)]) + ' '
            s += '\n'
        return s
    
    def check(self, player):
        # check row by row
        for row in range(self.nrows):
            if self.check_row(row, player):
                return True
        # check col by col
        for col in range(self.ncols):
            if self.check_col(col, player):
                return True
        
        for diag in self.get_diags():
            if self.check_list(diag, player):
                return True
    
    def get_row(self, r):
        row = []
        for col in range(self.ncols):
            row.append(self.board[(col, r)])
        return row
    
    def get_rows(self):
        rows = []
        for r in range(self.nrows):
            rows.append(self.get_row(r))
        return rows
    
    def get_col(self, c):
        col = []
        for row in range(self.nrows):
            col.append(self.board[(c, row)])
        return col
    
    def get_cols(self):
        cols = []
        for c in range(self.ncols):
            cols.append(self.get_col(c))
        return cols
    
    def check_row(self, r, player):
        row = self.get_row(r)
        return self.check_list(row, player)
    
    def check_col(self, c, player):
        col = self.get_col(c)
        return self.check_list(col, player)
    
    def check_list(self, list, player):
        total = 0
        for char in list:
            if char == symbols[player]:
                total += 1
                if total == self.goal: return True
            else:
                total = 0
    
    def get_diags(self):
        diags = []
        for k in range(self.nrows + self.ncols - 1):
            diag = []
            for col in range(0, min(k+1, self.ncols)):
                row = k - col
                if row < self.nrows:
                    #print(k, col, row)
                    diag.append(self.board[(col, row)])
            diags.append(diag)
            
        for k in range(self.nrows + self.ncols - 1):
            diag = []
            for col in range(0, min(k+1, self.ncols)):
                row = self.nrows - k + col - 1
                if row < self.nrows and row > -1:
                    diag.append(self.board[(col, row)])
            diags.append(diag)
        return diags
    
    def moves(self, player):
        return [col for col in range(self.ncols)
                if self.board[(col, self.nrows-1)] == '.']
        