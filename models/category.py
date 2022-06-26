class Category():
    def __init__(self, main_cat, sub_cat, id=None):
        self.main_cat = main_cat
        self.sub_cat = sub_cat
        self.id = id
        self.number_of_transactions = 0
        self.amount_of_transactions = 0

    def total_transactions(self, transactions):
        total_number = 0
        for transaction in transactions:
            if self.id == transaction.category.id:
                total_number += 1
        return total_number

    def total_amount_of_transactions(self, transactions):
        total_amount = 0
        for transaction in transactions:
            if self.id == transaction.category.id:
                total_amount += transaction.price
        return total_amount