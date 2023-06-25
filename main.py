# Kerrianne Crawford Student ID:000988956
from data.truck import deliver_packages, truck_1, truck_2, final_load
from data.package import load_package_data, lookup_package, get_all, lookup_at_time, get_all_at_time
from datetime import datetime


# Main function that will be called and handle both delivery of the packages and the user input
def main():  # O(n^2) SPACE_TIME_COMPLEXITY
    # Calls out to the package service and loads the packages into the hash table
    # as well as separating the loads into trucks
    load_package_data()  # O(n) SPACE_TIME_COMPLEXITY
    # Calls out to the truck service for truck 1 and truck 2 to begin delivery
    deliver_packages(truck_1)  # O(n^2) SPACE_TIME_COMPLEXITY
    deliver_packages(truck_2)  # O(n^2) SPACE_TIME_COMPLEXITY

    # We will send out the next truck depending on who returns first
    # if Truck 1 returns first, they will take the last load
    if truck_1.time < truck_2.time:
        truck_1.packages = final_load
        truck_1.depart_time = truck_1.time
        deliver_packages(truck_1)  # O(n^2) SPACE_TIME_COMPLEXITY
    # Otherwise, truck 2 will take the last load
    else:
        truck_2.packages = final_load
        truck_2.depart_time = truck_2.time
        deliver_packages(truck_2)  # O(n^2) SPACE_TIME_COMPLEXITY

    # Starting here are all the UI pieces
    print('-' * 10 + ' WGUPS ' + '-' * 10)
    # Here are where the mileages are returned both by individual truck and combined
    print('Total mileage traveled by truck 1: ' + str(truck_1.mileage.__round__(2)))
    print('Total mileage traveled by truck 2: ' + str(truck_2.mileage.__round__(2)))
    print('Total mileage traveled combined: ' + str((truck_1.mileage.__round__(2) + truck_2.mileage.__round__(
        2)).__round__(2)))

    # While loop that will continue to run until we have user selection or an error occurs
    run = True
    while run:
        # User will select whether they want to view timed results or non timed results
        choice = input('Please select a number:\n[1] - See Packages \n[2] - See Packages at Specific Time\n[3] - '
                       'Quit\n')
        if choice == '3':  # Quit choice
            print('Goodbye')
            break

        if choice == '1':  # See without time filter choice
            second_choice = input('Please input "all" to see all packages or an ID to view a single package\n')
            if 'all' in second_choice:  # The user indicated they want to see all packages
                display_all_packages(None)  # O(n) SPACE_TIME_COMPLEXITY
                break
            else: # The user has given us a package ID
                display_individual(second_choice)  # O(1) SPACE_TIME_COMPLEXITY
                break

        elif choice == '2':  # See with time filter
            time = input('Please enter a time in the format HH:MM:SS, including zeroes.\n').strip(' ')
            if time == '':  # User did not enter a time, so program exits.
                print('No time provided. Exiting.')
                break
            # Take the user input and format it into a date/time
            search_time = datetime.strptime(time, '%H:%M:%S')

            # Ask the user if they want to view all packages with that time frame, or a specific package
            second_choice = input('Please input "all" to see all packages or an ID to view a single package\n')
            if 'all' in second_choice:  # User indicated they want to see all packages
                display_all_packages(search_time)  # O(n) SPACE_TIME_COMPLEXITY
                break
            else:  # User provided an individual ID to search
                display_individual(second_choice, search_time)  # O(1) SPACE_TIME_COMPLEXITY
                break
        else:  # Catch all for any other incorrect inputs
            print('Please enter a valid selection')
            # We will loop again until the user inputs something valid
            continue


def display_individual(package_id, time=None):  # O(1) SPACE_TIME_COMPLEXITY
    # Checks for a valid package id, exits if not found
    if package_id == '':
        print('No package ID provided. Exiting.')
        return

    # if there is a time provided, we will use the filtered search
    if time:
        package = lookup_at_time(package_id, time)  # O(1) SPACE_TIME_COMPLEXITY
        if package is None:  # No package found, so exiting
            print('No package found with that ID. Exiting.')
            return
        # Adds headers to the response string
        response = 'Package ID, Address, City, State, Zip, Deadline, Status, Delivery Time, Departure Time\n'
        print(response + package.__str__())
        return
    # Otherwise we will use regular methods
    else:
        package = lookup_package(package_id)  # O(1) SPACE_TIME_COMPLEXITY
        if package is None:  # Package wasn't found, exiting program
            print('No package found with that ID. Exiting.')
            return
        # Adds headers to the response string
        response = 'Package ID, Address, City, State, Zip, Deadline, Status, Delivery Time, Departure Time\n'
        print(response + package.__str__())
        return


def display_all_packages(time):  # O(n) SPACE_TIME_COMPLEXITY
    if time is None:  # If no Time is provided, we will not filter search
        packages = get_all()  # O(n) SPACE_TIME_COMPLEXITY
        print(packages)
    else:  # Otherwise we will
        packages = get_all_at_time(time)  # O(n) SPACE_TIME_COMPLEXITY
        print(packages)


# Invoke the main function
main()

