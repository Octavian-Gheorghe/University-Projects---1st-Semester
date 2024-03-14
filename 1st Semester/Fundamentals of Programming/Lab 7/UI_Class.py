class UI:
    def __init__(self, serv):
        self.serv = serv

    def menu(self):
        print("1 - add expense")
        print("2 - display all expense")
        print("3 - filter expenses by a value")
        print("4 - undo")
        print()

    def add_expense(self):
        '''
        receives: the list of classes within the repository of choice: Memory / Text / Binary
        the program allows you to input 3 variables: day, an integer; amount, an integer as well and the string type
        the program will call the function add_expense within the 'Service_Class', where the 3 variables will be added to an Expense and then added to the list
        the program 'returns' the list with the new added expense
        '''
        day = int(input("enter a day: "))
        amount = int(input("enter an amount: "))
        type = str(input("enter a type: "))
        self.serv.add_expense(day, amount, type)

    def show_expense(self):
        self.serv.show_expense()

    def filter_expense(self):
        value = int(input("Insert a value: "))
        self.serv.filter_expense(value)

    def undo_expense(self):
        self.serv.undo_expense()
    
    def run(self):
        while True:
            self.menu()
            command = int(input("Command: "))
            if command == 1:
                self.add_expense()
            elif command == 2:
                self.show_expense()
            elif command == 3:
                self.filter_expense()
            elif command == 4:
                self.undo_expense()
            elif command == 0:
                return