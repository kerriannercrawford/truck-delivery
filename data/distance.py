import csv

# Opens and saves locally the distance data information
with open("./data/csv/distance_data.csv") as distance_file:
    distances = csv.reader(distance_file)
    distances = list(distances)

# Opens and saves locally the distance name/address information
with open("./data/csv/distance_name_data.csv") as address_file:
    addresses = csv.reader(address_file)
    addresses = list(addresses)


# Helper function that takes two address strings
# From the address string, the numerical reference number
# for the hub is found and then used to obtain the distance
def find_distance(x, y):  # O(n) SPACE_TIME_COMPLEXITY
    x = get_address_id(x)
    y = get_address_id(y)
    distance = distances[x][y]
    if len(distance) > 0:
        return float(distance)

    distance = distances[y][x]
    return float(distance)


# Additional helper function that returns the reference number
# of a given address
def get_address_id(address):  # O(n) SPACE_TIME_COMPLEXITY
    for row in addresses:
        if address in row[2]:
            return int(row[0])
