import pytest
import datetime
from datetime import timedelta
from providers import datetimeNowProxy
from checkoutService import CheckoutService
from models import Book, Member, Checkout
from bookInventory import BookInventory
from errors import BookUnavilableError, OutstandBalanceError
from pytest_mock import mocker
from unittest.mock import Mock

bookInventory = Mock()
member = Member()
book = Book()
checkoutService = CheckoutService(bookInventory)

def test_Checkout_MemberWithNoHistory_CheckoutIs7Days(mocker):
    mocker.patch(
        'checkoutService.datetimeNowProxy',
        return_value = datetime.datetime(2000, 1, 1)
    )
    
    checkout = checkoutService.checkout(member, book)
    assert checkout.dueDate == datetime.datetime(2000, 1, 8)

def test_Checkout_MemberWithHistory_CheckoutIs14Days(mocker):  
    member.hasCheckoutHistory = True
      
    mocker.patch(
        'checkoutService.datetimeNowProxy',
        return_value = datetime.datetime(2000, 1, 1)
    )
    
    checkout = checkoutService.checkout(member, book)
    assert checkout.dueDate == datetime.datetime(2000, 1, 15)

def test_Checkout_MemberWithBalanceDue_ThrowsException():
    member.outstandingBalance = 1
    with pytest.raises(OutstandBalanceError):
        checkoutService.checkout(member, book)

def test_Checkout_BookNotAvailable_ThrowsException():
    book.isUnavailable = True
    member.outstandingBalance = 0
    with pytest.raises(BookUnavilableError):
        checkoutService.checkout(member, book)

def test_Checkout_OnSuccess_BookRemovedFromInventory():
    book.isUnavailable = False
    bookInventory.removeBook = Mock()
    checkoutService.checkout(member, book)
    bookInventory.removeBook.assert_called_with(book)