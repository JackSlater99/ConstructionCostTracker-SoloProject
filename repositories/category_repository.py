from db.run_sql import run_sql
from models.category import Category


def save(category):
    sql = "INSERT INTO categories (main_cat, sub_cat) VALUES (%s, %s) RETURNING *"
    values = [category.main_cat, category.sub_cat]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category


def select_all():
    categories = []
    sql = "SELECT main_cat, sub_cat, id FROM categories" #ORDER BY main_cat"
    results = run_sql(sql)
    for result in results:
        category = Category(result['main_cat'], result['sub_cat'], result['id'])
        categories.append(category)
    return categories

def select(id):
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    category = Category(result['main_cat'], result['sub_cat'], result['id'])
    return category


def update(category):
    sql = "UPDATE categories SET (main_cat, sub_cat) = (%s, %s) WHERE id = %s"
    values = [category.main_cat, category.sub_cat, category.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# #EXTENSIONS

def group_categories(categories):
    output = {}
    for item in categories:
        if item.main_cat not in output:
            output[item.main_cat] = []
        output[item.main_cat].append(item)
    return output


# def total_category_cost(id):
#     category = select(id)
#     sql = "SELECT SUM(price) FROM transactions WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     return result
    # category.category_total += result
    # return category.category_total

    # category = Category(result['main_cat'], result['sub_cat'], result['id'])
    # return category







# def sort_categories_alphabetically():
#     categories = []
#     sql = "SELECT * FROM categories ORDER BY main_tag ASC;"
#     results = run_sql(sql)
#     for result in results:
#         category = Category(result['main_cat'], result['sub_cat'], result['id'])
#         categories.append(category)
#     return categories.sort()