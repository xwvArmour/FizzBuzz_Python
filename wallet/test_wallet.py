import pytest

class InsufficientFundsError(BaseException):
    pass

class Wallet(object):
    def __init__(self, initialAmount=0):
        self.balance = initialAmount

    def spend(self, spendAmount):
        if self.balance < spendAmount:
            raise InsufficientFundsError('Funds not available')
        self.balance -= spendAmount
        

@pytest.mark.parametrize('initialAmount,spendAmount,expected', [
    (5.00, 2.20, 2.80),
    (7.50, 2.50, 5.00),
    (1.00, .50, .50),
    (.50, .50, 0)
])
def test_givenInitialAmount_whenMoneySpent_decreasesBalance(initialAmount,spendAmount,expected):
    wallet = Wallet(initialAmount)
    wallet.spend(spendAmount)
    assert wallet.balance == expected
    
@pytest.mark.parametrize('initialAmount,spendAmount', [
    (1.00, 1.50),
    (0, .50)
])
def test_giveInitialAmount_whenOverspent_raisesError(initialAmount,spendAmount):
    wallet = Wallet(initialAmount)
    with pytest.raises(InsufficientFundsError):
        wallet.spend(spendAmount)