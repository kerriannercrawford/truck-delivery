
 > ### A: Identify a named self-adjusting algorithm that you used to create your program to deliver the packages.
 > (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”)

For this project, I used the Nearest Neighbor algorithm to sort the packages based on closest proximity 

> ### B: Write an overview of your program, in which you do the following:
> 1. Explain the algorithm’s logic using pseudocode.
> 2. Describe the programming environment you used to create the Python application.
> 3. Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O 
notation.
> 4. Explain the capability of your solution to scale and adapt to a growing number of packages.
> 5. Discuss why the software is efficient and easy to maintain.
> 6. Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).

1. The function `deliver_packages` in `./data/truck.py` holds the nearest neighbor algorithm.
   - The function accepts one argument, a truck object. 
   - A new array is created to store the packages that still need to be delivered
   - Iterate over all of the packages loaded up on the truck and add each one to the new array
   - Clear the packages off the truck to reload in the correct order
   - While there are still packages left to be delivered, we will iterate over that list
   - For each package still to be delivered, we will find the distance between that package and our current location.
   - If the value we find is smaller than what we found previously, we replace with the new lower value. 
   - Once we've found the next shortest distance, we remove it from the to be delivered list, update the truck 
     mileage, time, and package status to be delivered. 
   - If the truck is not already back at the starting location, we find the distance to the starting hub and add it 
     back to the mileage and time.
2. I used PyCharm 2023.1.2 (Professional Edition) Build #PY-231.9011.38
3. Please see in code comments with space-time complexity notations. These are indicated by `SPACE_TIME_COMPLEXITY`.
4. I believe my application can scale well, since the packages are handled in their own separate service, as well as 
   being stored in a hash table. A hash table will scale with ease, without losing any speed or efficiency. So even 
   if the number of packages increases, we will still have a constant O(1) look up time.
5. It is efficient and easy to maintain for a similar reason, because there are separations of concerns. With each 
   service (truck, distance, packages..) being handled modular-ly, it is easy to look for package bugs in the 
   package file, rather than having to look at the entire project.
6. Hash table strengths & weaknesses:
    - Strengths
      - Fast inserts/removals/lookups
      - Can be easy to implement
    - Weaknesses
      - Collisions have to be accounted for which can add complexity
      - Slower the speed the higher the number of collisions 

> ### C: Write an original program to deliver all the packages, meeting all requirements.
> 1. Create an identifying comment within the first line of a file named “main.py” that includes your first name, 
last name, and student ID.
> 2. Include comments in your code to explain the process and the flow of the program.

1. See `main.py`
2. N/A, comments are within code

> ### D: Identify a self-adjusting data structure that can be used with the algorithm to store the package data.
> 1. Explain how your data structure accounts for the relationship between the data points you are storing.

For this project, I used a hash table as my self adjusting data structure. The data points being stored are packages.

Hash tables allow for efficient and quick access to stored entries, and make it very easy to store key/value data 
pairs. In our case, that is exactly what we have. We want to store a package and be able to reference it later by 
its id. So, the key would be the package ID and the value of that key is the package itself. 

> ### E:  Develop a hash table, without using any additional libraries or classes:
> 1. that has an insertion function that takes the following components as input and inserts the components into the hash table:
>   -   package ID number
>   -   delivery address
>   -   delivery deadline
>   -   delivery city
>   -   delivery zip code
>   -   package weight
>   -   delivery status (e.g., delivered, en route)

1. See `./data/hashtable.py` `insert`

> ### F: Develop a look-up function:
> 1. that takes the following components as input and returns the corresponding data 
elements:
>    -   package ID number
>    -   delivery address
>    -   delivery deadline
>    -   delivery city
>    -   delivery zip code
>    -   package weight
>    -   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time

1. See `./data/hashtable.py` `lookup`

> ### G: Provide an interface for the user
> to view the status and info (as listed in part F) of any package at any time, 
and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
> 1. Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
> 2. Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
> 3. Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

1. Please see `screenshot_G1_1.png` and `screenshot_G1_2.png`
2. Please see `screenshot_G2_1.png` and `screenshot_G2_2.png`
3. Please see `screenshot_G3_1.png` and `screenshot_G3_2.png`

Two screenshots for each were needed due to size of data returned

> ### H: Provide a screenshot or screenshots showing successful completion of the code
>free from runtime errors or warnings, that includes the total mileage traveled by all trucks.

Please see `screenshot_H.png`

> ### I: Justify the core algorithm you identified in part A and used in the solution by doing the following:
> 1. Describe at least two strengths of the algorithm used in the solution.
> 2. Verify that the algorithm used in the solution meets all requirements in the scenario.
> 3. Identify two other named algorithms, different from the algorithm implemented in the solution, that would meet 
the requirements in the scenario.
>    -  Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.

1. Strengths of the algorithm used:
   - Loads up the trucks based on the next closest delivery location which decreases the miles it takes 
   - Utilizes separate helper functions to increase modularity and enhance readability. Helper functions take some 
     of the unnecessary simple logic out of the way to decrease complexion. 
2. Verify that the algorithm used in the solution meets all requirements in the scenario.
   - All packages delivered on time, can be viewed by viewing all packages without filtering time, by looking at 
     delivered time and deadline.
   - Package #9 not delivered until after 10:20, can be viewed by viewing individual package by ID and looking at 
     delivered time.
   - Delayed packages were put on truck after arriving, can be viewed by viewing all packages without filtering 
     times. Look at depart time. 
   - Packages were manually loaded if needed to be on truck 2 or needed to be sent with other packages. 
3. identify two other named algos
    - One algo I could have used instead of Nearest Neighbor is Breadth First Search. BFS would start at a vertex 
      and each branch at equal distances, until the entire graph has been visited. A positive of this is that no 
      vertex is visited twice. 
    - Another is Dijkstra’s algorithm. This algorithm finds the shortest path from a starting vertex to every other 
      vertex in the graph. 
    - These both differ from my algorithm as I did not do a graph based data set. 


> ### J: Describe what you would do differently if you did this project again.

If I were to do this project again, I think that I would spend more time on the distance data. I think that it would 
be very beneficial, especially if this project were to scale, to similarly store the neighborhood information in a 
hash table or similar data structure as we did with packages. This will improve lookup/insertion/search speeds. It 
will also have the data in a cleaner environment and make the experience interacting with it easier. 

> ### K: Justify the data structure you identified in part D by doing the following:
> 1. Verify that the data structure used in the solution meets all requirements in the scenario.
>    -  Explain how the time needed to complete the look-up function is affected by changes in the number of packages to 
     be delivered.
>    -  Explain how the data structure space usage is affected by changes in the number of packages to be delivered.
>    -  Describe how changes to the number of trucks or the number of cities would affect the look-up time and the space 
      usage of the data structure.
> 2. Identify two other data structures that could meet the same requirements in the scenario.
>    -  Describe how each data structure identified in part K2 is different from the data structure used in the solution.

1. Verify that the data structure used in the solution meets all requirements in the scenario.
   - The time to look up packages does not change based on the number of packages. 
   - As more packages are added, buckets are filled more. Each record in the hash table is also stored in an array 
     to prevent collisions. These internal arrays may increase as collisions happen. As packages are removed, space 
     frees up in these internal buckets.
   - The change to trucks or cities will not affect the lookup speed or space usage of the package hash table, 
     because these factors do not affect the package hash table. 
2. Identify two other data structures that could meet the same requirements in the scenario.
   - One structure that could be used in place of the hash table is a set. This would have automatic de-duplication 
     and built in functionality like filtering, unions, or intersections. 
   - Another structure that could be used is a dictionary. This would increase consistency throughout the codebase 
     as the distance data is currently stored in a dictionary as well. 
