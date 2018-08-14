

class Duck(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# Quack Behavior
class LoudDuck(Duck):
    def quack(self):
        print("QUACK! QUACK!! QUACK!!!")

class GentleDuck(Duck):
    def quack(self):
        print("quack!")

# Types of Ducks
class VillageDuck(LoudDuck):
    def go_home(self):
        print("Going to river")

class ToyDuck(GentleDuck):
    def lights_on(self):
        print("Lights on for 10 seconds")

class CityDuck(GentleDuck):
    def go_home(self):
        print("Going to central Park pond")