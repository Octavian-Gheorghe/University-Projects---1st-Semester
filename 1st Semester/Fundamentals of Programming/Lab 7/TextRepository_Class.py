from Repository_Class import MemoryRepository
from Expense_Class import Expense

class TextRepository(MemoryRepository):
    def __init__(self):
        super(TextRepository, self).__init__()
        self.read_file()

    def read_file(self):
        self.expenses.clear()
        myfile = open("A7.txt", "r")
        for text in myfile:
            text = text.split()
            day = int(text[0])
            amount = int(text[1])
            type = text[2]
            c = Expense(day, amount, type)
            self.expenses.append(c)
        myfile.close()

    def write_file(self):
        myfile = open("A7.txt", "w")
        for i in range(0, len(self.expenses)):
            myfile.write(str(self.expenses[i]))
            myfile.write('\n')
        myfile.close()
    
    def add_expense(self, expense):
        super(TextRepository, self).add_expense(expense)
        self.write_file()
    
    def filter_expense(self, value):
        super(TextRepository, self).filter_expense(value)
        self.write_file()

    def undo_expense(self):
        super(TextRepository, self).undo_expense()
        self.write_file()

    '''def create_expense(self):
        self.expenses.clear()
        super(TextRepository, self).create_expense()
        self.write_file()'''
