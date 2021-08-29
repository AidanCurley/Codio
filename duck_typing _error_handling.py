class Plane:
    def fly(self):
        return "Zooooom!!"

class Bird:
    def fly(self):
        return "I am flapping my wings"

class Car:
    def drive(self):
        return "My wheels are turning"

def print_fly(obj):
    try:
        print(obj.fly())
    except AttributeError as e:
        print(e)

# Test
my_things = []
my_bird = Bird()
my_things.append(my_bird)
my_plane = Plane()
my_things.append(my_plane)
my_car = Car()
my_things.append(my_car)

for thing in my_things:
    print_fly(thing)