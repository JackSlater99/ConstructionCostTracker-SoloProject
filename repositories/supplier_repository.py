from db.run_sql import run_sql
from models.supplier import Supplier


def save(supplier):
    sql = "INSERT INTO suppliers (supplier_name, supplier_number, supplier_manager, supplier_address, supplier_phone) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [supplier.supplier_name, supplier.supplier_number, supplier.supplier_manager, supplier.supplier_address, supplier.supplier_phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier


def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for result in results:
        supplier = Supplier(result['supplier_name'], result['supplier_number'], result['supplier_manager'], result['supplier_address'], result['supplier_phone'], result['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        supplier = Supplier(result['supplier_name'], result['supplier_number'], result['supplier_manager'], result['supplier_address'], result['supplier_phone'], result['id'])
    return supplier

def update(supplier):
    sql = "UPDATE suppliers SET (supplier_name, supplier_number, supplier_manager, supplier_address, supplier_phone) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [supplier.supplier_name, supplier.supplier_number, supplier.supplier_manager, supplier.supplier_address, supplier.supplier_phone, supplier.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)