products = [
{"name": "Monitor", "category": "Electronics", "price": 200},
{"name": "Keyboard", "category": "Electronics", "price": 50},
{"name": "Chair", "category": "Furniture", "price": 120},
{"name": "Table", "category": "Furniture", "price": 180},
{"name": "Mouse", "category": "Electronics", "price": 25},
]

#Create an empty dictionary to accumulate totals by category

category_totals= {}

# Loop through each product in the list

for product_info in products:
    product_category = product_info["category"]
    product_price= product_info["price"]
    if product_category not in category_totals:      #If the category is not in the dictionary, initialize it with 0
        category_totals[product_category] = 0

    category_totals[product_category] += product_price     # Add the product price to the total of its category



print(category_totals)