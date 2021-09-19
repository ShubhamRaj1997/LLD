from pprint import pprint

from level_cache import *
from stats import Stats


def inp(msg):
    return int(input(msg + ":\n"))


def inp_list(msg):
    return input(msg).split()


if __name__ == "__main__":
    # cache_levels = inp("Enter the number of levels")
    # capacities = inp_list("Enter space separated integers for capacity of each level")
    # read_times = inp_list("Add read times for each level of cache")
    # write_times = inp_list("Add write times for each level of cache")
    cache_levels = 3
    capacities = [2, 5, 10]
    write_times = [5, 10, 15]
    read_times = [1,3, 9]
    # create levels
    caches = []
    for i in range(0, cache_levels):
        caches.append(LevelCache(i + 1, int(capacities[i]), int(read_times[i]), int(write_times[i])))
    # add next and prev
    stats = Stats(10)
    for i in range(0, cache_levels):
        caches[i].next_level = None if i >= cache_levels - 1 else caches[i + 1]
        caches[i].last_level = None if not i else caches[i - 1]
        pprint(vars(caches[i]))
    while 1:
        command = input("type WRITE KEY VAL for writing\n type READ KEY for reading\n"
                        "type STATS last to see stats")
        command_list = command.split()
        print("*"*10, f"\ncommand was {command_list}\n", "*"*10)
        if command_list[0] == "WRITE":
            key, val = command_list[1], command_list[2]
            w = caches[0].write(key, val)
            print(f"written! : write time was {w}")
            stats.record_write(w)


        elif command_list[0] == "READ":
            key = command_list[1]
            v, r, w = caches[0].read(key)
            print(f"Read! : val:  {v}, read time: {r} and write time: {w}")
            stats.record_read(r + w)

        elif command_list[0] == "STATS":
            last = inp("How many number of average?")
            print(f"Last 10 reads avg {stats.get_last_read_times(last)}\n"
                  f"Last 10 write avg {stats.get_last_write_times(last)}")
