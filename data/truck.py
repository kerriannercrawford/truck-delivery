import datetime
from data.package import packages_hash
from data.distance import find_distance
from datetime import datetime as date_time


class Truck:
    def __init__(self, data):  # O(1) SPACE_TIME_COMPLEXITY
        self.capacity = data['capacity']
        self.speed = data['speed']
        self.packages = data['packages']
        self.mileage = data['mileage']
        self.address = data['address']
        self.depart_time = data['depart_time']
        self.time = data['depart_time']

    def __str__(self):  # O(1) SPACE_TIME_COMPLEXITY
        return '%s, %s, %s, %s, %s, %s' % (
            self.capacity,
            self.speed,
            self.packages,
            self.mileage,
            self.address,
            self.depart_time
        )


# Loads up truck 1 with packages and a departure time of 8:00
truck_1 = Truck({
    'capacity': 16,
    'speed': 18,
    'packages': [1, 13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40, 25],
    'address': '4001 South 700 East',
    'depart_time': date_time.strptime('8:00:00', '%H:%M:%S'),
    'mileage': 0
})


# Loads up truck 2 with packages and a departure time of 9:05
truck_2 = Truck({
    'capacity': 16,
    'speed': 18,
    'packages': [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
    'address': '4001 South 700 East',
    'depart_time': date_time.strptime('9:05:00', '%H:%M:%S'),
    'mileage': 0
})


# Last load of packages that will be picked up by the first returning truck
final_load = [2, 4, 5, 6, 7, 8, 9, 10, 11, 28, 32, 33]


def deliver_packages(truck):  # O(n^2) SPACE_TIME_COMPLEXITY
    # Iterates over all the packages loaded up on the truck and puts them
    # into a new array called to be delivered
    to_be_delivered = []
    for package_id in truck.packages:  # O(n) SPACE_TIME_COMPLEXITY
        package = packages_hash.lookup(str(package_id))
        to_be_delivered.append(package)
    # Remove any packages from the truck because we will reload them in sorted order
    truck.packages.clear()

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one

    # Iterates over the to be delivered packages until it is empty
    # Will add the nearest package to the current package one by one
    while len(to_be_delivered) > 0:  # O(n) * O(n) = O(n^2) SPACE_TIME_COMPLEXITY
        shortest_distance = 9999
        current_package = None
        for package in to_be_delivered:  # O(n) SPACE_TIME_COMPLEXITY
            new_distance = find_distance(truck.address, package.address)
            if new_distance <= shortest_distance:
                shortest_distance = new_distance
                current_package = package

        # Load the nearest package back onto the truck
        truck.packages.append(current_package.id)
        # Take the nearest package and remove it from the
        # to be delivered list, as it has already been delivered
        to_be_delivered.remove(current_package)
        # Adds the mileage for this trip
        truck.mileage += shortest_distance
        # Update the trucks address
        truck.address = current_package.address
        # Add the time it took to drive to the next location
        truck.time += datetime.timedelta(hours=shortest_distance / truck.speed)
        # Set the delivery time as the trucks current time
        current_package.delivery_time = truck.time
        # Set the departure time for the package
        current_package.departure_time = truck.depart_time
        current_package.status = 'Delivered'

    # If the truck is not already back at the hub, it needs to return
    # We calculate the miles and the time it takes to return
    if '4001 South 700 East' not in truck.address:
        distance_back = find_distance(truck.address, '4001 South 700 East')
        truck.mileage += distance_back
        truck.time += datetime.timedelta(hours=distance_back / truck.speed)
        truck.address = '4001 South 700 East'





