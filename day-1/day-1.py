import heapq


def get_elves_calories():
    f = open('./input-1.txt', 'r')
    cur = 0
    for line in f.readlines():
        line = line[:-1] # cut newline
        if line:
            cur += int(line)
        else:
            yield cur
            cur = 0

def get_elf_with_max():
    return max(get_elves_calories())

def get_top_elves(elfCount):
    buffer = []

    for cal in get_elves_calories():
        if len(buffer) >= elfCount:
            heapq.heappushpop(buffer, cal)
        else:
            heapq.heappush(buffer, cal)
    
    return sum(buffer)
