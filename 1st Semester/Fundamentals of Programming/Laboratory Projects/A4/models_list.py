from models_functions import *

def addNewExpense(Expenses, words, undoStack):
    '''
    Function that adds a new expense to the current day's expense for a given category and adds the function onto the undo stack
    '''
    new_amount = words[1]
    new_category = words[2]
    new_amount = int(new_amount)
    new_day = findCurrentDay(Expenses)
    new_day = int(new_day)
    expense = createExpense(new_day, new_amount, new_category)
    Expenses[new_day].append(expense)
    undoStack.append([new_day, new_amount, new_category, "add"])
    return (Expenses, undoStack)

def insertNewExpense(Expenses, new_day, new_amount, new_category):
    '''
    Function that inserts a new expense consisted in a given amount of money
    '''
    expense = createExpense(new_day, new_amount, new_category)
    new_day = int(new_day)
    if len(Expenses[new_day]) > 0:
        Expenses[new_day].append(expense)
    else:
        Expenses[new_day] = [expense]

    return Expenses

def modifyDay1(Expenses, new_day):
    '''
    Function that removes all the expenses made in a given day
    '''
    new_day = int(new_day)
    Expenses.remove(Expenses[new_day])
   
    return Expenses

def modifyDays(Expenses, day1, day2, undoStack):
    '''
    Function that removes all the expenses from given parameter day1 to given parameter day2 and adds the function onto the undo stack
    '''
    day1 = int(day1)
    day2 = int(day2)
    x = day1 + 1 
    cnt = 0
    while x < day2:
        if len(Expenses[x]) > 0:
            for y in range(0, len(Expenses[x])):
                undoStack.append([x + cnt, getAmount(Expenses[x][y]), getCategory(Expenses[x][y]), "remove"])
                cnt += 1
            Expenses.remove(Expenses[x])
        else:
            x += 1
    return (Expenses, undoStack, cnt)

def modifyCategory(Expenses, selected_category, undoStack):
    '''
    Function that removes all the expenses made for a given category and adds the function onto the undo stack
    '''
    x = 1
    cnt = 0
    while x < 31:
        y = 0
        while y < len(Expenses[x]):
            if getCategory(Expenses[x][y]) == selected_category:
                undoStack.append([x, getAmount(Expenses[x][y]), selected_category, "remove"])
                cnt += 1
                Expenses[x].remove(Expenses[x][y])
            else:
                y += 1
        x += 1
        
    return (Expenses, undoStack, cnt)

def sumOfCategory(Expenses, selected_category):
    '''
    Function that calculates the total expense for a given category
    '''
    sum = 0
    for x in range(0, len(Expenses)):
        for y in range(0, len(Expenses[x])):
            if getCategory(Expenses[x][y]) == selected_category:
                sum += getAmount(Expenses[x][y])
                
    return sum

def maxExpenses(Expenses):
    '''
    Function that returns the day with the maximum expenses
    '''
    daily_expenses = [0] * 32
    max = 0
    day = 0
    for x in range(0, len(Expenses)):
        for y in range(0, len(Expenses[x])):
            daily_expenses[getDay(Expenses[x][y])] += getAmount(Expenses[x][y])
        
    for x in  range(1, 31):
        if max < daily_expenses[x]:
            max = daily_expenses[x]
            day = x
        
    return day
        
def sortDay(Expenses):
    '''
    Function that returns the list of total daily expenses sorted in ascending order by amount of money spent
    '''
    sortList = []
    for x in range(0, len(Expenses)):
        for y in range(0, len(Expenses[x])):
            if len(Expenses[x]) > 0:
                sortList.append(Expenses[x][y])
                
    sortList.sort(key = getAmount)
    return sortList

def sortCategory(Expenses, selected_category):
    '''
    Function that returns the list of daily expenses for a given category, new_category, sorted in ascending order by amount of money spent
    '''
    sortList = []
    for x in range(0, len(Expenses)):
        for y in range(0, len(Expenses[x])):
            if len(Expenses[x]) > 0  and getCategory(Expenses[x][y]) == selected_category:
                sortList.append(Expenses[x][y])
                
    sortList.sort(key = getAmount)
    return sortList

def filterCategory(Expenses, selected_category, undoStack):
    '''
    Function that keeps only the expenses made in a given category, new_category and adds the function onto the undo stack
    '''
    cnt = 0
    for x in range(0, len(Expenses)):
        for y in range(0, len(Expenses[x])):
            if not getCategory(Expenses[x][y]) == selected_category:
                undoStack.append([x, getAmount(Expenses[x][y]), getCategory(Expenses[x][y]), "filter"])
                cnt += 1
                Expenses[x].remove(Expenses[x][y])
    
    return (Expenses, undoStack, cnt)

def filterProperty(Expenses, selected_category, symbol, new_amount, undoStack):
    '''
    Function that keeps only the expenses made in a given category, new_category, and with a certain property given by the parameters symbol and new_amount and adds the function onto the undo stack
    '''
    cnt = 0
    if symbol == "<":
        for x in range(0, len(Expenses)):
            for y in range(0, len(Expenses[x])):
                if not getCategory(Expenses[x][y]) == selected_category or getAmount(Expenses[x][y]) >= new_amount:
                    cnt += 1
                    undoStack.append([x, getAmount(Expenses[x][y]), getCategory(Expenses[x][y]), "filter"])
                    Expenses[x].remove(Expenses[x][y]) 
    elif symbol == "=":
        for x in range(0, len(Expenses)):
            for y in range(0, len(Expenses[x])):
                if not getCategory(Expenses[x][y]) == selected_category or not getAmount(Expenses[x][y]) == new_amount:
                    cnt += 1
                    undoStack.append([x, getAmount(Expenses[x][y]), getCategory(Expenses[x][y]), "filter2"])
                    Expenses[x].remove(Expenses[x][y])
    else:
        for x in range(0, len(Expenses)):
            for y in range(0, len(Expenses[x])):
                if not getCategory(Expenses[x][y]) == selected_category or getAmount(Expenses[x][y]) <= new_amount:
                    cnt += 1
                    undoStack.append([x, getAmount(Expenses[x][y]), getCategory(Expenses[x][y]), "filter2"])
                    Expenses[x].remove(Expenses[x][y])
                    
    return (Expenses, undoStack, cnt)

def undo(Expenses, undoStack, numberUndos):
    '''
    Function that reverses the last operation made upon the given list Expenses
    '''
    if len(undoStack) == 0:
        raise ValueError("No more possible undos")
    x = len(undoStack) - 1
    if undoStack[x][3] == "add":
        day = findCurrentDay(Expenses)
        expense = createExpense(day, int(undoStack[x][1]), undoStack[x][2])
        Expenses[day].remove(expense)
        undoStack.pop()
    elif undoStack[x][3] == "insert":
        day = int(undoStack[x][0])
        expense = createExpense(day, undoStack[x][1], undoStack[x][2])
        Expenses[day].remove(expense)
        undoStack.pop()
    else:
        if undoStack[x][3] == "remove":
            y = len(numberUndos) - 1
            while numberUndos[y] > 0 and x >= 0:
                Expenses = insertNewExpense(Expenses, undoStack[x][0], undoStack[x][1], undoStack[x][2])
                undoStack.pop()
                x -= 1
                numberUndos[y] -= 1
            numberUndos.remove(numberUndos[y])
        else:
            if undoStack[x][3] == "filter":
                y = len(numberUndos) - 1
                while numberUndos[y] >= 0 and x >= 0:
                    Expenses = insertNewExpense(Expenses, undoStack[x][0], undoStack[x][1], undoStack[x][2])
                    undoStack.pop()
                    x -= 1
                    numberUndos[y] -= 1
                numberUndos.remove(numberUndos[y])
    return Expenses