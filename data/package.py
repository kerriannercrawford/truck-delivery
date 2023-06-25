import csv
from data.hashtable import HashTable

with open("./data/csv/package_data.csv") as csvfile:
    packages = csv.reader(csvfile)
    packages = list(packages)

packages_hash = HashTable()


class Package:
    def __init__(self, data):  # O(1) SPACE_TIME_COMPLEXITY
        self.id = int(data[0])
        self.address = data[1]
        self.city = data[2]
        self.state = data[3]
        self.zip = data[4]
        self.deadline = data[5]
        self.status = 'at hub'
        self.delivery_time = None
        self.departure_time = None

    def __str__(self):  # O(1) SPACE_TIME_COMPLEXITY
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s' % (
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.deadline,
            self.status,
            self.delivery_time,
            self.departure_time
        )


# Will look up a package by ID at a certain time
def lookup_at_time(package_id, time):  # O(1) SPACE_TIME_COMPLEXITY
    package = packages_hash.lookup(package_id)

    # If package was delivered before or on the user time provided
    if package.delivery_time <= time:
        package.status = 'Delivered'
    # If the package left the hub before or on the user time provided
    elif package.departure_time <= time:
        package.status = 'En route'
        package.delivery_time = None
    # Otherwise, it is still at the hub
    else:
        package.status = 'At hub'
        package.delivery_time = None
        package.departure_time = None

    return package


# Will look up a package by a given ID
def lookup_package(package_id):  # O(1) SPACE_TIME_COMPLEXITY
    return packages_hash.lookup(str(package_id))


# Will look up ALL packages at a given time
def get_all_at_time(time):  # O(n) SPACE_TIME_COMPLEXITY
    response = 'Package ID, Address, City, State, Zip, Deadline, Status, Delivery Time, Departure Time\n'

    for package_id in range(1, 41):
        package = lookup_package(package_id)
        # If package was delivered before or on the user time provided
        if package.delivery_time <= time:
            package.status = 'Delivered'
        # If the package left the hub before or on the user time provided
        elif package.departure_time <= time:
            package.status = 'En route'
            package.delivery_time = None
        # Otherwise, it is still at the hub
        else:
            package.status = 'At hub'
            package.delivery_time = None
            package.departure_time = None
        response += package.__str__() + '\n'
    return response


# Will get all packages
def get_all():  # O(n) SPACE_TIME_COMPLEXITY
    response = 'Package ID, Address, City, State, Zip, Deadline, Status, Delivery Time, Departure Time\n'

    for package_id in range(1, 41):
        package = lookup_package(package_id)
        response += package.__str__() + '\n'

    return response


# Loads in the package data into the hash table at the beginning of program
def load_package_data():  # O(n) SPACE_TIME_COMPLEXITY
    for package_data in packages:
        package = Package(package_data)

        packages_hash.insert(str(package.id), package)
