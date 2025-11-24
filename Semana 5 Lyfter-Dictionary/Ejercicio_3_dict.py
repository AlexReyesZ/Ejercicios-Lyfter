car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "color": "Red",
    "price": 15000
}

keys_to_remove = ["color", "price"]

for key in keys_to_remove:

    car.pop(key, None)    # use the loop variable 'key' and provide None as default to avoid KeyError

print(car)
