from re import sub
from turtle import color
import matplotlib.pyplot as plt
from repositories.transaction_repository import total_category_cost 
import os
plt.switch_backend('Agg')


def graph():
    source_list = total_category_cost()
    if source_list == []:
        os.remove("static/graphs/cost_by_cat.png")
        return
    sub_category, total_value = zip(*source_list)
    plt.bar(sub_category, total_value, width=0.5, color="b")
    plt.xlabel('Category')
    plt.ylabel('Total Spent (£)')
    plt.gcf().autofmt_xdate()
    plt.title('Total Spent per Category')
    plt.savefig('static/graphs/cost_by_cat.png')
    plt.close()

