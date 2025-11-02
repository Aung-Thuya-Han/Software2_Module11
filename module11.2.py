class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, volume_of_tank):
        super().__init__(reg_number, max_speed)
        self.volume_of_tank = volume_of_tank



electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.current_speed = 150
gasoline_car.current_speed = 100

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car has travelled {electric_car.travelled_distance} km.")
print(f"Gasoline Car has travelled {gasoline_car.travelled_distance} km.")
