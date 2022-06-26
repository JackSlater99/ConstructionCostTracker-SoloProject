from db.run_sql import run_sql
from repositories import supplier_repository
from repositories import category_repository
from models.transaction import Transaction
from models.category import Category

#Save new Transaction

def save(transaction):
    sql = "INSERT INTO transactions (supplier_id, category_id, product, price, po_number, order_date, invoice_number) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.supplier.id, transaction.category.id, transaction.product, transaction.price, transaction.po_number, transaction.date, transaction.invoice_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

#Select all Transactions

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY order_date DESC"
    results = run_sql(sql)
    for result in results:
        supplier = supplier_repository.select(result['supplier_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(supplier, category, result['product'], result['price'], result['po_number'], result['order_date'], result['invoice_number'], result['id'])
        transactions.append(transaction)
    return transactions

#Select Transaction by ID

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    supplier = supplier_repository.select(result['supplier_id'])
    category = category_repository.select(result['category_id'])
    transaction = Transaction(supplier, category, result['product'], result['price'], result['po_number'], result['order_date'], result['invoice_number'], result['id'])
    return transaction

#Update Existing Transaction

def update(transaction):
    sql = "UPDATE transactions SET (supplier_id, category_id, product, price, po_number, order_date, invoice_number) = (%s, %s, %s,%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.supplier.id, transaction.category.id, transaction.product, transaction.price, transaction.po_number, transaction.date, transaction.invoice_number, transaction.id]
    run_sql(sql, values)

#Delete all Transactions

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

#Delete Transaction by ID

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#OVERALL TOTAL

def total_cost():
    total = []
    sql = "SELECT price FROM transactions"
    results = run_sql(sql)
    for result in results:
        value = result["price"]
        total.append(value)
    return sum(total)

#EXTENSIONS
#TOTAL FOR EACH CATEGORY

def total_category_cost():
    sql = """SELECT category_id, sum(price) AS amount
                FROM transactions
                GROUP BY category_id
                ORDER BY category_id;"""
    results = run_sql(sql)
    for item in results:
        item_category = category_repository.select(item[0])
        item[0] = item_category.sub_cat
    return results

#SELECT ALL TRANSACTIONS FOR EACH CATEGORY

def select_all_by_category(id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE category_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        supplier = supplier_repository.select(result['supplier_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(supplier, category, result['product'], result['price'], result['po_number'], result['order_date'], result['invoice_number'], result['id'])
        transactions.append(transaction)
    return transactions

#SELECT ALL TRANSACTIONS FOR EACH SUPPLIER

def select_all_by_supplier(id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE supplier_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        supplier = supplier_repository.select(result['supplier_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(supplier, category, result['product'], result['price'], result['po_number'], result['order_date'], result['invoice_number'], result['id'])
        transactions.append(transaction)
    return transactions

#FILTER TRANSACTIONS BY MONTH

def select_by_month(month):
    transactions = []
    sql = "SELECT * FROM transactions WHERE EXTRACT(month from date(order_date)) = %s"
    values = [month]
    results = run_sql(sql, values)
    for result in results:
        supplier = supplier_repository.select(result['supplier_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(supplier, category, result['product'], result['price'], result['po_number'], result['order_date'], result['invoice_number'], result['id'])
        transactions.append(transaction)
    return transactions

