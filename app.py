from flask import Flask, render_template
from controllers.suppliers_controller import suppliers_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.categories_controller import categories_blueprint
from controllers.stats_controller import stats_blueprint

app = Flask(__name__)

app.register_blueprint(suppliers_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(stats_blueprint)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)