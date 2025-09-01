import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timeh = time.strftime("%H")
timem = time.strftime("%M")
times = time.strftime("%S")
print(timeh,timem,times)




car_info = {
    "car1": {"brand": "Ford", "model": "Mustang", "year": 1964},
    "car2": {"brand": "Tesla", "model": "Model S", "year": 2020}
}
for car, info in car_info.items():
    print(car)
    for key, value in info.items():
        print(f"  {key}: {value}")
