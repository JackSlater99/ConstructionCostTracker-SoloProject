from repositories.transaction_repository import total_category_cost 

source_list = total_category_cost()
list1, list2 = zip(*source_list)
list1
list2

import matplotlib.pyplot as plt

# def graph():
#     plt.bar(list1,list2)
#     plt.savefig('graphs/cost_by_cat.png')

print(source_list)