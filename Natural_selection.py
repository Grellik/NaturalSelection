# Made by Danilov Gennady a.k.a. Grellik, 25/12/2019.
# Latest update -21/02/2020, version 0.0.1

# Natural selection simulator.
# It is a simple simulator which provides user several tools to start the
# simulation where several creatures have to compete for limited amount of
# food on the field. It allows user to observe population of species
# in different conditions, and see which species are most adapted
# for specific situations.

# This code requires PyQt5to run correctly!
# You can read about PyQt5 here: https://pypi.org/project/PyQt5/#description
# You can download PyQt5 here: https://pypi.org/project/PyQt5/#files

from PyQt5.QtWidgets import QApplication, QLabel
import start_sim
import random
import math

app = QApplication([])


class Specie:
    def __init__(self, speed, sense, energy, life, hunger, AI, number):
        self.speed = speed
        self.sense = sense
        self.energy = energy
        self.life = life
        self.hunger = hunger
        self.AI = AI
        self.number = None

# Definition of variables required for the start of simulation


def starting_vars():
    day = 0

    return grid_size, num_species, food_gen, day


# Method creator of grid (=field for species)
# Grid [[x0;y1;0],[x1;y1;0]] == [ [[x0;y0;0],[x1;y0;0] , [x0;y1;0],[x1;y1;0] ]
#     [[x0;y0;0],[x1;y0;0]]
# Third coordinate is an indicator for how many food units there are on point of the grid
def grid_creation(grid_size):
    grid = []
    for height in range(grid_size):  # Definition of line coordinates for grid
        line = []
        width = 0
        while width != grid_size:  # Definition of column coordinates for grid
            coord = [width, height, 0]
            line.append(coord)
            width += 1
        grid.append(line)
    return grid

# Stats of any default speciemen : 4 main caracteristics + hunger + "life model"


def default_stats(grid_size):
    speed = 1
    sense = 1
    energy = 10*int(grid_size/2)
    life = 1
    hunger = 0
    AI = "default"
    return speed, sense, energy, life, hunger, AI

# Status list of all species on field
# It is updated each movement of species and at the end of the day


def status(num_species, species_list, grid_size, day):
    if day == 0:  # Definition of parameters for all species created by user on day 0
        for n in range(num_species):
            sp, se, en, li, hu, ai = (default_stats(grid_size))
            species_list.append([n, sp, se, en, li, hu, ai, None, None])
    else:
        for n in range(len(species_list)):
            if species_list[n][4] == 0:
                species_list[n] == [n, 0, 0, 0, -1, 0, "dead", "dead"]
    return species_list


def day_start():
    pass


def day_action(status):
    pass


def day_end():
    pass

# Logic and actions of default specie


def default_AI(speed, sense, energy, hunger, position, grid_size):
    if energy >= 10:
        target = f_sense(sense)
        if target != [None]:
            position = target
        elif target == [None]:
            moveset, moveset_decode = movement_set(position, grid_size)
            move = random.randint(0, len(move)-1)


def f_sense(sense):
    target = [None]
    for x in range(-1*sense, sense+1):
        if position[0]+x >= 0 and position[0]+x < grid_size:
            for y in range(-1*sense, sense+1):
                if position[1]+y >= 0 and position[1]+y < grid_size:
                    if grid[position[1]+y][position[0]+x][2] > 0:
                        if target == [None]:
                            target = [position[0]+x, position[1]+y]
                        elif target != [None]:
                            if target[0] >= position[0]+x and target[1] >= position[1]+y:
                                target = [position[0]+x, position[1]+y]
    return target

# Creation of moveset for species so they can't get out of the defiend field
# It returns the possible directions each time while specie moves while it has energie to move


def movement_set(position, grid_size):
    limit = grid_size-1
    moveset = ["up", "down", "left", "right",
               "upleft", "upright", "downleft", "downright"]
    moveset_decode = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0),
                      "upleft": (-1, 1), "upright": (1, 1), "downleft": (-1, -1), "downright": (1, -1)}
    if position[0] == 0:
        moveset.remove("left")
        moveset.remove("upleft")
        moveset.remove("downleft")
    if posision[0] == limit:
        moveset.remove("right")
        moveset.remove("upright")
        moveset.remove("downright")
    if position[1] == 0:
        moveset.remove("down")
        if "downright" in moveset:
            moveset.remove("donwright")
        if "downleft" in moveset:
            moveset.remove("downleft")
    if position[1] == limit:
        moveset.remove("up")
        if "upright" in moveset:
            moveset.remove("upright")
        if "upleft" in moveset:
            moveset.remove("upleft")
    return moveset, moveset_decode
