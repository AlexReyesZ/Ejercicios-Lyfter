# New sales data
sales = [
    {
        'date': '10/03/25',
        'customer_email': 'maria@example.com',
        'items': [
            {'name': 'Bluetooth Speaker', 'upc': 'ITEM-101', 'unit_price': 80.50},
            {'name': 'Wireless Mouse', 'upc': 'ITEM-102', 'unit_price': 25.00},
        ],
    },
    {
        'date': '10/03/25',
        'customer_email': 'carlos@example.com',
        'items': [
            {'name': 'Bluetooth Speaker', 'upc': 'ITEM-101', 'unit_price': 80.50},
            {'name': 'Keyboard', 'upc': 'ITEM-103', 'unit_price': 45.75},
        ],
    },
    {
        'date': '09/03/25',
        'customer_email': 'ana@example.com',
        'items': [
            {'name': 'Keyboard', 'upc': 'ITEM-103', 'unit_price': 45.75},
            {'name': 'Wireless Mouse', 'upc': 'ITEM-102', 'unit_price': 25.00},
            {'name': 'USB Hub', 'upc': 'ITEM-104', 'unit_price': 15.25},
        ],
    },
]

# Dictionary to store total per UPC
result = {}

# Loop through each sale
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']

# Initialize UPC in result if not present
        if upc not in result:
            result[upc] = 0
        result[upc] += price   # Add the price to the total for this UPC

# Display the result
print(result)
