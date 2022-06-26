from flask import Flask, render_template, request, redirect
from repositories import supplier_repository
from repositories import transaction_repository
from models.supplier import Supplier
from flask import Blueprint

suppliers_blueprint = Blueprint("suppliers", __name__)

#SUPPLIER INDEX

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    number_suppliers = len(suppliers)
    return render_template("suppliers/index.html", all_suppliers = suppliers, number_suppliers = number_suppliers)

#NEW SUPPLIER

@suppliers_blueprint.route("/suppliers/new", methods=["GET"])
def new_suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/new.html", all_suppliers = suppliers)

#CREATE SUPPLIER

@suppliers_blueprint.route("/suppliers", methods=["POST"])
def create_suppliers():
    supplier_name = request.form["supplier_name"]
    supplier_number = request.form["supplier_number"]
    supplier_manager = request.form["supplier_manager"]
    supplier_address = request.form["supplier_address"]
    supplier_phone = request.form["supplier_phone"]
    supplier = Supplier(supplier_name, supplier_number, supplier_manager, supplier_address, supplier_phone)
    supplier_repository.save(supplier)
    return redirect("/suppliers")

#SHOW SUPPLIER

@suppliers_blueprint.route("/suppliers/<id>", methods=["GET"])
def show_supplier(id):
    found_supplier = supplier_repository.select(id)
    found_transactions = transaction_repository.select_all_by_supplier(id)
    return render_template("suppliers/show.html", supplier = found_supplier, transactions = found_transactions)


#EDIT SUPPLIER

@suppliers_blueprint.route("/suppliers/<id>/edit")
def edit_suppliers(id):
    supplier = supplier_repository.select(id)
    return render_template("/suppliers/edit.html", supplier = supplier)

#UPDATE SUPPLIER

@suppliers_blueprint.route("/suppliers/<id>", methods=["POST"])
def update_supplier(id):
    supplier_name = request.form["supplier_name"]
    supplier_number = request.form["supplier_number"]
    supplier_manager = request.form["supplier_manager"]
    supplier_address = request.form["supplier_address"]
    supplier_phone = request.form["supplier_phone"]
    supplier = Supplier(supplier_name, supplier_number, supplier_manager, supplier_address, supplier_phone, id)
    supplier_repository.update(supplier)
    return redirect("/suppliers")

#DELETE SUPPLIER

@suppliers_blueprint.route("/suppliers/<id>/delete", methods=["POST"])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect("/suppliers")