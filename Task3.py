class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int, speed_limit:int):
        self.brand = brand
        self.model = model
        self.year = year
        self. speed = speed
        self. speed_limit = speed_limit

    
    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        if self.speed > 0:
            self.speed -= 5
            return self.speed
    
    def display_speed(self):
        return self.speed
    
    
first_car = Car('Nissan', 'Juke', 2015, 0, 60)
print(f'Car brand is {first_car.brand}')

while first_car.speed < first_car.speed_limit:
    first_car.accelerate()

print(f'speed limit {first_car.speed_limit}mph reached')
first_car.brake()
print(f' safe speed {first_car.display_speed()}mph set')

