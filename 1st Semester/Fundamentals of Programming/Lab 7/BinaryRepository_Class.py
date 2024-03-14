from Repository_Class import MemoryRepository
from Expense_Class import Expense
import pickle

class BinaryRepository(MemoryRepository):
    def __init__(self):
        super(BinaryRepository, self).__init__()
        self.read_file()

    def read_file(self):
        myfile = open("A7.bin", "rb")
        self.expenses = pickle.load(myfile)
        myfile.close()

    def write_file(self):
        myfile = open("A7.bin", "wb")
        pickle.dump(self.expenses, myfile)
        myfile.close()

    def add_expense(self, expense):
        super(BinaryRepository, self).add_expense(expense)
        self.write_file()
    
    def filter_expense(self, value):
        super(BinaryRepository, self).filter_expense(value)
        self.write_file()

    def undo_expense(self):
        super(BinaryRepository, self).undo_expense()

    '''def create_expense(self):
        self.expenses.clear()
        super(BinaryRepository, self).create_expense()
        self.write_file()'''
