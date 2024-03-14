from Expense_Class import Expense

class Service:
    def __init__(self, repo):
        self.repo = repo

    def add_expense(self, day, amount, type):
        expense = Expense(day, amount, type)
        self.repo.add_expense(expense)

    def show_expense(self):
        self.repo.show_expense()

    def filter_expense(self, value):
        self.repo.filter_expense(value)

    def undo_expense(self):
        self.repo.undo_expense()
    
