"""
Its OBJECT oriented programing, so its fitting we start with what the heck is an object?

Well, let's say we have a dict with some data about a tank in a game:

tank_data = {'health': 1200, 'speed': 0, ...}


And let's say that we have some functions which are called to modify this data:

def accelerate_tank(tank_data, acceleration):
    tank_data['speed'] += acceleration

def tank_shot(tank_data, damage):
    tank_data['health'] -= damage


Ok, so now we need more than one tank:

So, we want to separate the data between what is common to all tanks, which is for
example that they start the battle with 0 speed:

base_tank_data = {'initial_speed': 0, ...}

And the data which is specific to every tank in particular, which we'll add with a
function:

def initialise_tank_data(initial_health, ...):
    tank_data = copy(base_tank_data)  # <- we want a copy of the dict so each tank has his own dict.
    tank_data['health'] = initial_health
    ...
    return tank_data

So, we have some data & some functions all about a tank in the game. We can say that
these functions are only applied to tank_data, & that calling any of these functions
without passing into it tank_data doesn't make much sense.

So, we're feeling fancy & decide to invent an entire paradigm to encompass this.

We can create the concept of a class in which we define what functions will
apply to what data:

class Tank:  # <- We've named this 'Tank' now, because it's cooler, & also an abstraction
             # which might help us think about this as the tank itself.
             # By convention class names should start by capital and use no '_'
             # So, TankDestroyer yes, Tank_destroyer no.

    def __init__(  # This is like initialise_tank_data function from before, when a new tank is created
                   # the __init__ METHOD can provide the initial data for the tank_data dict.
                   # (Yes, we now call functions methods because they are in a class)

            self,  # Instead of calling the dict tank_data we now call it 'self' since we now
                   # think of this as a tank we pass self, i.e. the tank to every function.

            initial_health,  # We can pass other arguments to this __init__ to initialise 'self' dict
            ...
    ):

        # Instead of accessing out tank_data dict with a bunch of [] and '' we can just do it with a '.'
        # so where before we did tank_data['speed'] = 0 now we can so self.speed = 0
        self.speed = 0

        # Or we can initialise another ATTRIBUTE of tank with the value we passed to __init__
        # (What before we called elements in a dict, or key-value pairs, we now call attributes)
        self.health = initial_health

        # P.D. There are other ways of initialising attributes, & you don't even have to write an
        # __init__ method for a class to work & have attributes, but it's a good practice to
        # have all the attributes initialised here, even if you don't have the data yet.
        # These are python minutia, but other languages have class constructors which are similar,
        # & similar conventions.

    # Not too much more to explain here, these methods do the same thing as before but we call them
    # methods now instead of functions, & we pass self to them instead of the tank_data dict.
    def accelerate(self, acceleration):
        self.speed += acceleration

    def was_shot(self, damage):
        self.health -= damage

    ...

So, now we've defined what data will our object hold and what methods can operate on this data,
all we need to do now is create some tanks.

tank = Tank(initial_health=1200)

And that's it, we've created a tank object, the python magic automatically calls the __init__
when calling the class itself (Tank()), & the __init__ automatically returns self
(not really, __new__ returns self, & __new__ is the auto-called & it calls __init__ but yeah python details)

So lets run this code:

"""


class Tank:
    def __init__(self, initial_health):
        self.speed = 0
        self.health = initial_health

    def accelerate(self, acceleration):
        self.speed += acceleration

    def was_shot(self, damage):
        self.health -= damage

tank = Tank(1200)

print('tank.health', tank.health)
print('tank.speed', tank.speed)
print()

print('Accelerating...')
tank.accelerate(1)
tank.accelerate(1)
tank.accelerate(1)
tank.accelerate(1)
print('tank.speed', tank.speed)
print()

print('Tank getting shot')
tank.was_shot(250)
print('tank.health', tank.health)
