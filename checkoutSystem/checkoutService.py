from datetime import timedelta
from providers import datetimeNowProxy
from models import Book, Member, Checkout
from bookInventory import BookInventory
from errors import BookUnavilableError, OutstandBalanceError

class CheckoutService(object):
    _bookInventory = None
    
    def __init__(self, bookInventory):
        self._bookInventory = bookInventory
        pass
    
    def _validate(self, member: Member, book: Book):
        if (member.outstandingBalance > 0):
            raise OutstandBalanceError("Member has an outstanding balance")
        
        if (book.isUnavailable):
            raise BookUnavilableError("Book not avialable")
        
    def checkout(self, member: Member, book: Book) -> Checkout: 
        self._validate(member, book)

        checkout = Checkout()
        currentDate = datetimeNowProxy()
        lengthOfCheckout = 7
        if member.hasCheckoutHistory:
            lengthOfCheckout = 14
            
        self._bookInventory.removeBook(book)

        checkout.dueDate = currentDate + timedelta(days=+lengthOfCheckout)
        return checkout