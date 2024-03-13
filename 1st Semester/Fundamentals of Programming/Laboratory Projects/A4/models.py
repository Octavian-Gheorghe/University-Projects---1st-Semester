def createExpense(day, amount, category):
    '''
    constructs an expense structure given its day, amount of money and category
    Input: day, amount, category
    Precondition : day - integer, amount - integer, category - string
    Output : list: [day, amount, category]
    '''
    day = int(day)
    if day < 0 or day > 30:
        raise ValueError("Day is between 1 and 30")
    categories = [ "housekeeping", "food", "transport", "clothing", "internet", "others"]
    if not category in categories:
        raise ValueError("Category must be one of the known expenses")
    amount = int(amount)
    if amount <= 0:
        raise ValueError("The amount of money must be a positive integer")
    
    return [day, amount, category]


def getDay(expense):
    '''
    Input: expense (a dictionary formed of [day, amount, category])
    Output : the day from expense dictionary - integer
    Postcondition : re = expense["day"]
    '''
    return expense[0]

def getAmount(expense):
    '''
    Input : expense
    Output : the amount from expense dictionary
    Postcondition : re = expense["amount"]
    '''
    return int(expense[1])

def getCategory(expense):
    '''
    Input : expense
    Output : the category from expense dictionary
    '''
    return expense[2]

def setDay(expense, modified_day):
    '''
    Function that sets the day of an expense
    Input : expense, new_day
    Precondition : expense - dictionary, new_day - integer
    Output : expense with modified day
    '''
    modified_day = int(modified_day)
    if modified_day < 0 or modified_day > 30:
        raise ValueError("Day is between 1 and 30")
    expense[0] = modified_day
    return expense

def setAmount(expense, modified_amount):
    '''
    Function that sets the amount of money of an expense
    Input : Expenses, expense, new_amount
    Precondition : expense - dictionary, new_amount - integer
    Output : expense with modified amount
    '''
    modified_amount = modified_amount
    if modified_amount <= 0:
        raise ValueError("The amount of money must be a positive integer")
    expense[1] = modified_amount
    return expense

def setCategory(expense, changed_category):
    '''
    Function that changes the category of an expense
    Input : Expenses, expense, changed_category
    Precondition : expense - dictionary, changed_category - string
    Output : expense with changed category
    '''
    categories = [ "housekeeping", "food", "transport", "clothing", "internet", "others"]
    if not changed_category in categories:
        raise ValueError("Category must be one of the known expenses")
    expense[2] = changed_category
    return expense

