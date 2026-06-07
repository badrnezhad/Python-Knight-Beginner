def get_rejected_cars(cars):
    rejected_cars = []
    for car in cars:
        if car["co"] > 0.7:
            rejected_cars.append(car)

    return rejected_cars


cars = [
    {"plate": "111k22", "co": 0.5},
    {"plate": "324w56", "co": 0.8},
    {"plate": "358r12", "co": 0.9},
    {"plate": "444z02", "co": 0.1},
    {"plate": "666t78", "co": 0.3}
]

rc = get_rejected_cars(cars)
for car in rc:
    print(car["plate"])
