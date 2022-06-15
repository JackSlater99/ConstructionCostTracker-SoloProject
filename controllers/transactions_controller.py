from flask import Flask, render_template, request, redirect
from repositories import transaction_repository
from repositories import category_repository
from repositories import supplier_repository
from repositories import stat_repository
from models.transaction import Transaction
from flask import Blueprint


transactions_blueprint = Blueprint("transactions", __name__)

#HOME PAGE

@transactions_blueprint.route('/')
def index():
    supplier = supplier_repository.select_all()
    category = category_repository.select_all()
    return render_template("index.html", all_suppliers = supplier, all_categories = category)

#INDEX

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total_cost()
    total_by_cat = transaction_repository.total_category_cost()
    month = 2
    filter = transaction_repository.select_by_month(month)
    return render_template("transactions/index.html", all_transactions = transactions, total = f"{total:,}", total_by_cat = total_by_cat, filter = filter)

#NEW

@transactions_blueprint.route("/transactions/new", methods=["GET"])
def new_transactions():
    supplier = supplier_repository.select_all()
    category = category_repository.select_all()
    return render_template("transactions/new.html", all_suppliers = supplier, all_categories = category)

#CREATE

@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transactions():
    supplier_id = request.form["supplier_id"]
    supplier = supplier_repository.select(supplier_id)
    category_id = request.form["category_id"]
    category = category_repository.select(category_id)
    product = request.form["product"]
    price = request.form["price"]
    po_number = request.form["po_number"]
    order_date = request.form["order_date"]
    invoice_number = request.form["invoice_number"]
    transaction = Transaction(supplier, category, product, price, po_number, order_date, invoice_number)
    transaction_repository.save(transaction)
    return redirect("/transactions")

#SHOW

@transactions_blueprint.route("/transactions/<id>", methods=["GET"])
def show_transaction(id):
    found_transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction = found_transaction)


#EDIT

@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transactions(id):
    transaction = transaction_repository.select(id)
    supplier = supplier_repository.select_all()
    category = category_repository.select_all()
    return render_template("/transactions/edit.html", transaction = transaction, all_suppliers = supplier, all_categories = category)

#UPDATEtransaction

@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    supplier_id = request.form["supplier_id"]
    supplier = supplier_repository.select(supplier_id)
    category_id = request.form["category_id"]
    category = category_repository.select(category_id)
    product = request.form["product"]
    price = request.form["price"]
    po_number = request.form["po_number"]
    order_date = request.form["order_date"]
    invoice_number = request.form["invoice_number"]
    transaction = Transaction(supplier, category, product, price, po_number, order_date, invoice_number, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

#DELETE

@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")

#FILTER BY MONTH


@transactions_blueprint.route("/transactions/month/<id>", methods=["GET"])
def filter_month_transaction(id):
    found_transaction = transaction_repository.select_by_month(id)
    return render_template("transactions/month.html", transactions = found_transaction)