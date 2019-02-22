
"""
Question C
Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network
issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU
(Least Recently Used) cache with time expiration.
"""

import time
import random

# uses multiple threads for testing - they act as traffic from Geolocations
from threading import Lock, Thread

# LRU with time expiration
class Cache():

    def __init__(self, size):
        self.MaxSize = size
        self.cacheList = []
        self.cacheDictionary = {}
        self.currentSize = 0

    # Filter before adding to queue
    # Removed expired items
    def put(self, item, valid_time=2):

        if item in self.cacheDictionary:
            insert_time, duration = self.cacheDictionary[item]
            secs = int(time.time())
            if insert_time + duration > secs:
                print("Item {} is already in cache".format(item))
                return
            else:
                print("Item {} has expired".format(item))
                self.remove(self.cacheList.index(item))

        if len(self.cacheDictionary) >= self.MaxSize:
            self.remove()

        self.add(item, valid_time)

    # Add item to list and update dictionary
    def add(self, item, valid_time):
        self.cacheList.append(item)
        secs = int(round(time.time()))
        self.cacheDictionary[item] = [secs, valid_time]
        print("Item {} has been added to cache".format(item))

    # Remove item at desired index form the queue( or start of the list by default). Also update map
    def remove(self, index=0):
        item = self.cacheList.pop(index)
        del self.cacheDictionary[item]
        print("Item {} has been removed from cache".format(item))

    def print(self):
        print("Items in the Cache")
        print("Items", self.cacheList)
        print("Key Value of items: ", self.cacheDictionary)

lock = Lock()
def traffic(cache_object):

    # generate traffic
    while 1:

        # generate random item and valid time
        item = random.randint(1,9)
        valid_time = random.randint(1,3)
        lock.acquire()
        try:
            cache_object.put(item, valid_time)
            cache_object.print()
        finally:
            lock.release()

        time.sleep(1)


if __name__ == '__main__':

    NUM_SOURCES = 1
    CACHE_SIZE = 5
    cache_object = Cache(CACHE_SIZE)

    threads = []
    for i in range(NUM_SOURCES):
         t = Thread(target=traffic, args=(cache_object,))
         threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
         thread.join()
