class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"
    
    def __repr__(self):
        return f"wheel Size: {self.wheel_size}\nWheel Number: {self.wheel_number}" 
    


truck = Vehicle(17, 10)
sedan = Vehicle(10,4)
print(type(sedan))
print(type(truck))

