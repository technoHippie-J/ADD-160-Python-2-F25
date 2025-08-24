"""
    
Objective:

    In this assignment, you will create a Python class for a toy car. This class will include attributes for the brand, color, type of car, and whether it is motorized or not. You will also implement class and instance variables and create methods for playing with the toy car and making it sound. Finally, you will create instances of the class and use the __class__ and __dict__ attributes appropriately.

Instructions:

1. Create a class named ToyCar with the following attributes:
    - brand (instance variable)
    - color (instance variable)
    - car_type (instance variable)
    - motorized (instance variable)
    - toy_type (class variable set to "car")

2. Use the __init__ method to initialize the brand, color, car_type, and motorized attributes when an instance of ToyCar is created.

3. Create a method named play that prints "The toy car moves forward.".

4. Create a method named sound that prints "Vroom".

5. Create three instances of the ToyCar class:
    - race_car with brand "Hot Wheels", color "red", type "race car", and motorized set to True.
    - pickup_truck with brand "Tonka", color "yellow", type "pickup truck", and motorized set to False.
    - police_car with brand "Matchbox", color "blue", type "police car", and motorized set to True.

6. Print the class of each instance using the __class__ attribute.

7. Print the dictionary representation of one of the instances using the __dict__ attribute.

Sample Output:

<class '__main__.ToyCar'>
{'brand': 'Hot Wheels', 'color': 'red', 'car_type': 'race car', 'motorized': True}
The toy car moves forward.
Vroom
    
"""

# Create ToyCar class


class ToyCar:
    # Set class variable
    toy_type = "car"

    # Initialize
    def __init__(self, brand, color, car_type, motorized):
        self.brand = brand
        self.color = color
        self.car_type = car_type
        self.motorized = motorized

    def play(self):
        return "The toy car moves forward."

    def sound(self):
        return "Vroom."

    def no_play(self):
        return "The toy car stands still... \nNo fun today."

    def does_it_move(self):
        if self.motorized == True:
            return f"{self.play()}\n{self.sound()}"
        else:
            return self.no_play()

# Instantiation


race_car = ToyCar(brand="Hot Wheels", color="red",
                  car_type="race car", motorized=True)

pickup_truck = ToyCar(brand="Tonka", color="yellow",
                      car_type="pickup truck", motorized=False)

police_car = ToyCar(brand="Matchbox", color="blue",
                    car_type="police car", motorized=True)


# Main function
def main():
    print(race_car.__class__)
    print(race_car.__dict__)
    print(race_car.does_it_move())
    print("\n")
    print(pickup_truck.__class__)
    print(pickup_truck.__dict__)
    print(pickup_truck.does_it_move())
    print("\n")
    print(police_car.__class__)
    print(police_car.__dict__)
    print(police_car.does_it_move())


# Main program
main()
