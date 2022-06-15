from flask import Flask, render_template
import repositories.transaction_repository as transaction_repository
import repositories.stat_repository as stat_repository
from flask import Blueprint


stats_blueprint = Blueprint("stats", __name__)


@stats_blueprint.route("/statistics", methods=["GET"])
def stats():
    stat_repository.graph()
    total = transaction_repository.total_cost()
    total_by_cat = transaction_repository.total_category_cost()
    return render_template("stats/index.html", total = f"{total:,}", total_by_cat = total_by_cat)

