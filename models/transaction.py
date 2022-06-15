class Transaction():
    def __init__(self, supplier, category, product, price, po_number, date, invoice_number, id=None):
        self.supplier = supplier
        self.category = category
        self.product = product
        self.price = price
        self.po_number = po_number
        self.date = date
        self.invoice_number = invoice_number
        self.id = id


