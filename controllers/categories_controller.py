from flask import Flask, render_template, request, redirect
from repositories import category_repository
from repositories import transaction_repository
from models.category import Category
from flask import Blueprint

categories_blueprint = Blueprint("categories", __name__)

#CATEGORY INDEX

@categories_blueprint.route("/categories")
def categories():
    categories = category_repository.select_all()
    grouped_categories = category_repository.group_categories(categories)
    transactions = transaction_repository.select_all()
    number_categories = len(categories)
    category_total = []
    for category in categories:
        category.number_of_transactions = category.total_transactions(transactions)
        category.amount_of_transactions = category.total_amount_of_transactions(transactions)
        category_total.append(category)
    return render_template("categories/index.html", all_categories = category_total, group_cat = grouped_categories, number_categories = number_categories)

#NEW CATEGORY

@categories_blueprint.route("/categories/new", methods=["GET"])
def new_categories():
    categories = category_repository.select_all()
    return render_template("categories/new.html", all_categories = categories)

#CREATE CATEGORY

@categories_blueprint.route("/categories", methods=["POST"])
def create_categories():
    main_cat = request.form["main_category_name"]
    sub_cat = request.form["sub_category_name"]
    category = Category(main_cat, sub_cat)
    category_repository.save(category)
    return redirect("/categories")

#SHOW CATEGORY

@categories_blueprint.route("/categories/<id>", methods=["GET"])
def show_category(id):
    found_category = category_repository.select(id)
    found_transactions = transaction_repository.select_all_by_category(id)
    return render_template("categories/show.html", category = found_category, transactions = found_transactions)


#EDIT CATEGORY

@categories_blueprint.route("/categories/<id>/edit")
def edit_categories(id):
    category = category_repository.select(id)
    return render_template("/categories/edit.html", category = category)

#UPDATE CATEGORY

@categories_blueprint.route("/categories/<id>", methods=["POST"])
def update_category(id):
    main_cat = request.form["main_category_name"]
    sub_cat = request.form["sub_category_name"]
    category = Category(main_cat, sub_cat, id)
    category_repository.update(category)
    return redirect("/categories")

#DELETE CATEGORY

@categories_blueprint.route("/categories/<id>/delete", methods=["POST"])
def delete_category(id):
    category_repository.delete(id)
    return redirect("/categories")