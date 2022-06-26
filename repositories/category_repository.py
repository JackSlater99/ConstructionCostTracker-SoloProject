from db.run_sql import run_sql
from models.category import Category

#Save new Category

def save(category):
    sql = "INSERT INTO categories (main_cat, sub_cat) VALUES (%s, %s) RETURNING *"
    values = [category.main_cat, category.sub_cat]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

#Select all Categories

def select_all():
    categories = []
    sql = "SELECT * FROM categories ORDER BY main_cat, sub_cat ASC"
    results = run_sql(sql)
    for result in results:
        category = Category(result['main_cat'], result['sub_cat'], result['id'])
        categories.append(category)
    return categories

#Select Category by ID

def select(id):
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    category = Category(result['main_cat'], result['sub_cat'], result['id'])
    return category

#Update existing Category

def update(category):
    sql = "UPDATE categories SET (main_cat, sub_cat) = (%s, %s) WHERE id = %s"
    values = [category.main_cat, category.sub_cat, category.id]
    run_sql(sql, values)

#Delete all Categories

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

#Delete Category by ID

def delete(id):
    sql = "DELETE FROM categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#EXTENSIONS
#PRINT MAIN CATEGORY HEADING AND SUB CATEGORIES UNDER

def group_categories(categories):
    output = {}
    for item in categories:
        if item.main_cat not in output:
            output[item.main_cat] = []
        output[item.main_cat].append(item)
    return output
