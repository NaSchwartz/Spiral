# Based on the 3b1b video below:
# https://www.youtube.com/shorts/t3jZ2xGOvYg

from random import randint

def create_clock():
    circle = dict()
    for i in range (12):
        circle[i] = False
    return circle

def take_step(position:int) -> int:
    return (position + 1) % 12 if randint(0,1) else (position - 1) % 12

def end(circle):
    for thing in circle.values():
        if not thing:
            return False
    return True

def simulate():
    circle = create_clock()
    circle[0] = True
    pos = 0

    while not end(circle):
        pos = take_step(pos)
        circle[pos] = True

    return pos

def create_distribution():
    dist = dict()
    for i in range(12):
        dist[i] = 0
    return dist

def distribution(runtime = 1000):
    dist = create_distribution()
    for i in range(runtime):
        dist[simulate()] += 1
    return dist

def print_dist(dist, runtime):
    for key in dist:
        print(f'P({key}) = {dist[key]/runtime}')
    print(f'\nP(6) = {dist[6]/runtime}')

#####################
#       Main        #
#####################

runtime = 100000
print_dist(distribution(runtime), runtime)
print(f'1/11 = {1/11}')