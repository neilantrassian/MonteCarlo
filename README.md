# MonteCarlo
Final Project for DS5100


# Metadata
    Neil Antrassian
    Monte Carlo Simulator

# Synopsis
    Show demo code of how the classes are used
```
from montecarlo import Die, Game, Analyzer
import pandas as pd
import numpy as np

#Die Class
# create dice, change weights, and roll a die
b = Die([1,2,3,4,5,6])
c= Die([1,2,3,4,5,6])
b.change_weight(4, 200)
b.roll_die(5)




#Game Class
# create game objects made up of dice, play games with the dice, show results
dice = Game([b, c])
dice.play(9)
dice.show_play()


# Analyzer Class
# analyze game objects
analysis = Analyzer(dice)
analysis.jackpot()

```


# API description

# Die
    def __init__(self, faces_array):
        '''
    PURPOSE: initialize die objects
    
    INPUTS
    faces_array   a list of strings or ints
    
    OUTPUT
    no return value
    attributes include faces_array, weights, weight_face
    
        '''
        
        
    def change_weight(self, face_value, new_weight):
        '''
    PURPOSE: change the weight of a die face
    
    INPUTS
    face_value    which face to change
    new_weight  new weight to change to
    
    OUTPUT
    no return value
    attributes include face_value, new_weight, 
        '''
    
    def roll_die(self, num_roll = 1):
        '''
    PURPOSE: roll the die n times
    
    INPUTS
    num_rolls    number of times to roll die, default =1 
    
    OUTPUT
    list of faces from the rolls
    attributes: num_roll
        '''
        
    def current_die(self):
        '''
    PURPOSE: return current die
    
    INPUTS
    none

    
    OUTPUT
    weight_face    df of current weights and faces
        '''
# Game
        '''
    PURPOSE: create game objects from a list of dice
    
    INPUTS
    die_list    list of die objects
    
    OUTPUT


        '''
    def __init__(self, die_list):
    '''
    PURPOSE: create game objects from a list of dice
    
    INPUTS
    die_list    list of die objects
    
    OUTPUT
    no return
    attributes include die_list
    '''
    
    def play(self, num_rolls):
        '''
    PURPOSE: rolls each die in die_list num_rolls times
    
    INPUTS
    num_rolls   number of times to roll the dice
    
    OUTPUT
    no return
    attributes include num_rolls, dice_rolls
        '''
        
    def show_play(self, wide = True):
        '''
    PURPOSE: show df of most recent play
    
    INPUTS
    wide    boolean for which rep of df to return (wide or narrow)
    
    OUTPUT
    df of most recent play
        '''
# Analyzer
    class Analyzer:
    '''
    PURPOSE: analyze the game object
    
    INPUTS
    game_object
    
    OUTPUT
    '''
    
    def __init__(self, game_object):
    '''
    PURPOSE: initialize the game object
    
    INPUTS
    game_object
    
    OUTPUT
    no return
    attributes include game_object
    '''
    
    def jackpot(self):
        '''
    PURPOSE: return num timmes that a roll returns the same face for every die
    
    INPUTS
    
    OUTPUT
    count    int for numm timmes jackpot occurs 
        '''
        
    def combo(self):
        '''
    PURPOSE: returns the different combos of die faces and the frequency they appeared
    
    INPUTS
    
    OUTPUT
    combo    die combo frequencies
    '''
    
    def face_counts(self):
        '''
    PURPOSE: roll the die n times
    
    INPUTS
    num_rolls    number of times to roll die, default =1 
    
    OUTPUT
    list of faces from the rolls
    '''
    
# Manifest
LICENSE, Project, README.md, setup.py
