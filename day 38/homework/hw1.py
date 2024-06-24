"""Thinkful - Dictionary drills: Order filler"""

def fillable(stock, merch, n):
    return True if merch in stock and stock[merch] >= n else False