# Hash Table class
# Referenced from Course Tips / Course Materials for ZyBook
class HashTable:
    # Init function is run on initialization
    # It takes a capacity argument, but if one is not provided,
    # it defaults the capacity to 40.
    # A table is created with whatever value of capacity is set.
    def __init__(self, capacity=40):  # O(n) SPACE_TIME_COMPLEXITY
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Actually functions as an "upsert" since it handles both
    # new items and updates.
    def insert(self, key, value):  # O(1) SPACE_TIME_COMPLEXITY
        # Find the appropriate bucket
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if key is already in the bucket, update it
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        # otherwise, insert the item
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def lookup(self, key):  # O(1) SPACE_TIME_COMPLEXITY
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):  # O(1) SPACE_TIME_COMPLEXITY
        # Find the appropriate bucket
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if the item exists, remove it from the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])