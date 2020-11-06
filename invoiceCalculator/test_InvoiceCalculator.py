from unittest.mock import Mock
from invoice import Invoice
from invoiceCalculator import InvoiceCalculator

def test_Calculate_GivenSubtotalAndPostalCode_SetsCorrectTaxAmount():
    # Arrange
    invoice = Invoice()
    invoice.subTotal = 5.00
    invoice.postalCode = '75111'
    
    taxRateHelper = Mock()
    taxRateHelper.getTaxRate = Mock(return_value=.08)
    
    invoiceCalculator = InvoiceCalculator(taxRateHelper)

    # Act
    invoiceCalculator.calculate(invoice)

    # Assert
    assert invoice.taxAmount == .4
