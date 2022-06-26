from flask import Flask, render_template
import repositories.transaction_repository as transaction_repository
import repositories.supplier_repository as supplier_repository
import repositories.category_repository as category_repository
import repositories.stat_repository as stat_repository
from flask import Blueprint


stats_blueprint = Blueprint("stats", __name__)

#Stats Controller - Home Page for Site

@stats_blueprint.route("/", methods=["GET"])
def stats():
    stat_repository.graph()
    total = transaction_repository.total_cost()
    total_by_cat = transaction_repository.total_category_cost()
    transactions = transaction_repository.select_all()
    number_transactions = len(transactions)
    suppliers = supplier_repository.select_all()
    number_suppliers = len(suppliers)
    categories = category_repository.select_all()
    number_categories = len(categories)
    return render_template("index.html", total = f"{total:,}", total_by_cat = total_by_cat, number_suppliers = number_suppliers, number_categories = number_categories, number_transactions = number_transactions)

