# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def make_conway (grid, i, j, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
        #premier rectangle
        cases [i] [j] ['s'] = life_status
        cases [i] [j] ['c'] = color
        cases [i] [j + 1]['s']= life_status
        cases [i] [j + 2]['s']= life_status
        cases [i] [j + 3]['s']= life_status
        cases [i] [j + 4]['s']= life_status
        cases [i] [j + 5]['s']= life_status
        cases [i + 1] [j]['s']= life_status
        cases [i + 1] [j + 1]['s']= life_status
        cases [i + 1] [j + 2]['s']= life_status
        cases [i + 1] [j + 3]['s']= life_status
        cases [i + 1] [j + 4]['s']= life_status
        cases [i + 1] [j + 5]['s']= life_status
        cases [i] [j + 1]['c']= color
        cases [i] [j + 2]['c']= color
        cases [i] [j + 3]['c']= color
        cases [i] [j + 4]['c']= color
        cases [i] [j + 5]['c']= color
        cases [i + 1] [j]['c']= color
        cases [i + 1] [j + 1]['c']= color
        cases [i + 1] [j + 2]['c']= color
        cases [i + 1] [j + 3]['c']= color
        cases [i + 1] [j + 4]['c']= color
        cases [i + 1] [j + 5]['c']= color
        #deuxième rectangle
        cases [i + 3] [j]['s']= life_status
        cases [i + 4] [j]['s']= life_status
        cases [i + 5] [j]['s']= life_status
        cases [i + 6] [j]['s']= life_status
        cases [i + 7] [j]['s']= life_status
        cases [i + 8] [j]['s']= life_status
        cases [i + 3] [j + 1]['s']= life_status
        cases [i + 4] [j + 1]['s']= life_status
        cases [i + 5] [j + 1]['s']= life_status
        cases [i + 6] [j + 1]['s']= life_status
        cases [i + 7] [j + 1]['s']= life_status
        cases [i + 8] [j + 1]['s']= life_status
        cases [i + 3] [j]['c']= color
        cases [i + 4] [j]['c'] = color
        cases [i + 5] [j]['c'] = color
        cases [i + 6] [j]['c'] = color
        cases [i + 7] [j]['c'] = color
        cases [i + 8] [j]['c'] = color
        cases [i + 3] [j + 1]['c'] = color
        cases [i + 4] [j + 1]['c'] = color
        cases [i + 5] [j + 1]['c'] = color
        cases [i + 6] [j + 1]['c'] = color
        cases [i + 7] [j + 1]['c'] = color
        cases [i + 8] [j + 1]['c'] = color
        #troisième rectangle
        cases [i + 7] [j + 3]['s']= life_status
        cases [i + 7] [j + 4]['s']= life_status
        cases [i + 7] [j + 5]['s']= life_status
        cases [i + 7] [j + 6]['s']= life_status
        cases [i + 7] [j + 7]['s']= life_status
        cases [i + 7] [j + 8]['s']= life_status
        cases [i + 8] [j + 3]['s']= life_status
        cases [i + 8] [j + 4]['s']= life_status
        cases [i + 8] [j + 5]['s']= life_status
        cases [i + 8] [j + 6]['s']= life_status
        cases [i + 8] [j + 7]['s']= life_status
        cases [i + 8] [j + 8]['s']= life_status
        cases [i + 7] [j + 3]['c']= color
        cases [i + 7] [j + 4]['c']= color
        cases [i + 7] [j + 5]['c']= color
        cases [i + 7] [j + 6]['c']= color
        cases [i + 7] [j + 7]['c']= color
        cases [i + 7] [j + 8]['c']= color
        cases [i + 8] [j + 3]['c']= color
        cases [i + 8] [j + 4]['c']= color
        cases [i + 8] [j + 5]['c']= color
        cases [i + 8] [j + 6]['c']= color
        cases [i + 8] [j + 7]['c']= color
        cases [i + 8] [j + 8]['c']= color
        #quatrième rectangle
        cases [i] [j + 7]['s']= life_status
        cases [i + 1] [j + 7]['s']= life_status
        cases [i + 2] [j + 7]['s']= life_status
        cases [i + 3] [j + 7]['s']= life_status
        cases [i + 4] [j + 7]['s']= life_status
        cases [i + 5] [j + 7]['s']= life_status
        cases [i] [j + 8]['s']= life_status
        cases [i + 1] [j + 8]['s']= life_status
        cases [i + 2] [j + 8]['s']= life_status
        cases [i + 3] [j + 8]['s']= life_status
        cases [i + 4] [j + 8]['s']= life_status
        cases [i + 5] [j + 8]['s']= life_status
        cases [i] [j + 7]['c']= color
        cases [i + 1] [j + 7]['c']= color
        cases [i + 2] [j + 7]['c']= color
        cases [i + 3] [j + 7]['c']= color
        cases [i + 4] [j + 7]['c']= color
        cases [i + 5] [j + 7]['c']= color
        cases [i] [j + 8]['c']= color
        cases [i + 1] [j + 8]['c']= color
        cases [i + 2] [j + 8]['c']= color
        cases [i + 3] [j + 8]['c']= color
        cases [i + 4] [j + 8]['c']= color
        cases [i + 5] [j + 8]['c']= color
    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def apply_rules (grid, compteur):
    next_grid = grid
    next_grid = apply_game_of_life_rules (next_grid)
    if compteur % 12 == 0:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_conway (next_grid, 20, compteur + 20, 'red')
    else:
        print ("COMPTEUR % 11 is NOT 0")
        time.sleep (0.2)
        next_grid = apply_game_of_life_rules (grid)
    return next_grid
