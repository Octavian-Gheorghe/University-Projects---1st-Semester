from Expense_Class import Expense
import random
import copy

class MemoryRepository:
    def __init__(self):
        self.allexpenses = []
        self.expenses = []
        self.create_expense()
        self.copy_expense()
    
    def add_expense(self, expense):
        self.expenses.append(expense)
        self.copy_expense()

    def filter_expense(self, value):
        i = 0
        while i < len(self.expenses):
            if self.expenses[i].amount <= value:
                self.expenses.pop(i)
                i = i - 1
            i = i + 1
        self.copy_expense()
    
    def create_expense(self):
        type_list = ['in', 'out']
        for i in range(0,10):
            day = random.randint(1,30)
            amount = random.randint(1,500)
            type = type_list[random.randint(0,1)]
            c = Expense(day, amount, type)
            self.expenses.append(c)
        self.copy_expense()
    
    def show_expense(self):
        print()
        for i in range(0, len(self.expenses)):
            print(self.expenses[i].day, self.expenses[i].amount, self.expenses[i].type)
        print()
    
    def copy_expense(self):
        j = self.expenses[:]
        self.allexpenses.append(j)

    def undo_expense(self):
        if len(self.allexpenses)!=1:
            self.allexpenses.pop(-1)
            j = copy.deepcopy(self.allexpenses[-1])
            self.expenses = j