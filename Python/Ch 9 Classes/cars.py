class Car:
    def __init__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year
            self.odometer_reading=0
    def get_name(self):
        long_name =f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def update_odometer(self,milege):
        if milege>=self.odometer_reading:
                self.odometer_reading=milege
                
        else:
                print("You can't roll an odometer back.")
    def read_odometer(self):
             print(f"This car has {self.odometer_reading} miles on it.")                       
my_car= Car('audi','a4',2019)
my_car.odometer_reading=23
print(my_car.get_name()) 
print(my_car.read_odometer())         