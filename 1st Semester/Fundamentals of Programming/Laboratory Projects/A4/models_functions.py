from models import *
def findCurrentDay(Expenses):
    '''
    Function that finds the current day(the last day in which was made an expense)
    Input: Expenses- list of lists of lists (list of days, with each day having a list of expenses, each of them being a list formed of 3 elements (see models.py))
    Output: current_day - integer
    '''
    x = 30
    current_day = 0
    while x > 0:
        y = len(Expenses[x])
        while y > 0:
            y -= 1
            if getDay(Expenses[x][y]) > 0:
                current_day = getDay(Expenses[x][y])
                y = 0
                x = 0
        x -= 1 
    return current_day

def toString(parameter):
    '''
    converts a given parameter to a string
    '''
    return str(parameter)

def isNumber(x):
    '''
    determines if a given parameter is a number or not
    '''
    try:
        int(x)
        return True
    except ValueError:
        return False
    
def isDay(x):
    '''
    verifies if the given parameter x is a day of a month or not
    '''
    if isNumber(x):
        x = int(x)
        if 0 < x and x < 31:
            return True
    return False

