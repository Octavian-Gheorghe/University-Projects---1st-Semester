class Expense:
    def __init__(self, day, amount, type):
        self.day = day
        self.amount = amount
        self.type = type
        
    def __str__(self):
        return f"{self.day} {self.amount} {self.type}"