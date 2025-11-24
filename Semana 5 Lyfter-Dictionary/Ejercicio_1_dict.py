# create a dictionary for a hotel
hotel_rooms = [
    {
    "name": "Sunrise ",
    "star_rating": 4,
    "rooms": [
        {"number": 10, "floor": 1, "price_per_night": 80},
        {"number": 15, "floor": 1, "price_per_night": 90},
        {"number": 20, "floor": 2, "price_per_night": 120},
        {"number": 25, "floor": 2, "price_per_night": 150}
        ]
    },
    {
    "name":'Palace',
    'star_rating': 5,
    "rooms":[
        {"number": 30, "floor": 3, "price_per_night": 200},
        {"number": 35, "floor": 3, "price_per_night": 200},
        {"number": 40, "floor": 4, "price_per_night": 250},
        {"number": 45, "floor": 4, "price_per_night": 250}
        ]
    }
]

for hotel in hotel_rooms:
    print(f"Room Name: {hotel['name']}")
    print(f"Star Rating: {hotel['star_rating']}")
    print("Rooms:")
    for room in hotel["rooms"]:
        print(f"  - Room Number: {room['number']}, Floor: {room['floor']}, Price per night: ${room['price_per_night']}")