from invoice import Invoice    

class InvoiceCalculator(object):
    _taxRateHelper = None

    def __init__(self, taxRateHelper):
        self._taxRateHelper = taxRateHelper

    def calculate(self, invoice: Invoice):
        taxRate = self._taxRateHelper.getTaxRate(invoice.postalCode)
        invoice.taxAmount = invoice.subTotal * taxRate