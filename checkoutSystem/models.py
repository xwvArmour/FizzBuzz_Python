import datetime

class Checkout(object):
    def __init__ (self):
        self.dueDate = datetime.datetime.now()
        
class Book(object):
    def __init__ (self):
        self.isUnavailable = False

class Member(object):
    def __init__ (self):
        self.hasCheckoutHistory = False
        self.outstandingBalance = 0