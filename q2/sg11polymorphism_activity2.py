class Boat:
    # creates the Boat class
    def move(self):
        # defines the move method for Boat
        print("The boat sails on water.")
        # prints how the boat moves


class Drone:
    # creates the Drone class
    def move(self):
        # defines the move method for Drone
        print("The drone flies in the sky.")
        # prints how the drone moves


def start_trip(vehicle):
    # defines a function that takes a vehicle object
    vehicle.move()
    # calls the move method of the passed object


car = Car()
# creates a Car object
boat = Boat()
# creates a Boat object
drone = Drone()
# creates a Drone object

start_trip(car)
# calls start_trip for the car object
start_trip(boat)
# calls start_trip for the boat object
start_trip(drone)
# calla start_trip for the drone object
