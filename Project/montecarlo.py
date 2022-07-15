import pandas as pd
import numpy as np
import unittest

class Die:
    def __init__(self, faces_array):
        '''
    PURPOSE: initialize die objects
    
    INPUTS
    faces_array   a list of strings or ints
    
    OUTPUT
    no return value
    attributes include faces_array, weights, weight_face
    
        '''
        
        self.faces_array = faces_array
        if not isinstance(self.faces_array[0], (int, str)):
            raise TypeError("Only integers or string are allowed")
        else:
            self.weights = np.ones(len(faces_array))
            self.weight_face = pd.DataFrame({'face' : faces_array, 'weights' : self.weights})
            self.weight_face.index +=1
    def change_weight(self, face_value, new_weight):
        '''
    PURPOSE: change the weight of a die face
    
    INPUTS
    face_value    which face to change
    new_weight  new weight to change to
    
    OUTPUT
    
        '''
        self.face_value = face_value
        self.new_weight = new_weight
        if self.face_value not in self.faces_array:
            raise ValueError("Only values in faces array can have their weights changed")
        else:
            self.weights[face_value] = new_weight
            self.weight_face['weights'] = self.weights
            
    def roll_die(self, num_roll = 1):
        '''
    PURPOSE: roll the die n times
    
    INPUTS
    num_rolls    number of times to roll die, default =1 
    
    OUTPUT
    list of faces from the rolls
        '''
        if not isinstance(num_roll, int):
            raise TypeError("Only integers are allowed")
        else:
            df = self.weight_face.sample(num_roll, replace =True, weights = 'weights')
            return df['face'].tolist()
    def current_die(self):
        '''
    PURPOSE: return current die
    
    INPUTS

    
    OUTPUT
    weight_face    df of current weights and faces
        '''
        return self.weight_face
    
class Game:
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
        
        self.die_list = die_list
        if not isinstance(self.die_list[0], (Die)):
            raise TypeError("Only die objects are allowed")
        else:
            self.die_list = die_list                       
                       
    def play(self, num_rolls):
        '''
    PURPOSE: rolls each die in die_list num_rolls times
    
    INPUTS
    num_rolls   number of times to roll the dice
    
    OUTPUT
        '''      
        
        self.num_rolls = num_rolls
        self.dice_rolls = [i.roll_die(self.num_rolls) for i in self.die_list]
        self.__play_df = pd.DataFrame(self.dice_rolls)
        self.__play_df.index +=1
        self.__play_df.columns +=1
        return None
    def show_play(self, wide = True):
        '''
    PURPOSE: show df of most recent play
    
    INPUTS
    wide    boolean for which rep of df to return (wide or narrow)
    
    OUTPUT
    df of most recent play
        '''
        self.wide = wide
        if self.wide == False:
            return self.__play_df.T.stack().to_frame()   
        else:
            return self.__play_df
        
class Analyzer:
    '''
    PURPOSE: analyze the game object
    
    INPUTS
    game_object
    
    OUTPUT
    '''
    combo = pd.DataFrame([])
    def __init__(self, game_object):
        '''
    PURPOSE: initialize the game object
    
    INPUTS
    game_object
    
    OUTPUT
    no return
    attributes include game_object
    '''
        
        self.game_object = game_object

    def jackpot(self):
        '''
    PURPOSE: return num timmes that a roll returns the same face for every die
    
    INPUTS
    
    OUTPUT
    count    int for numm timmes jackpot occurs 
        '''
        df = self.game_object.show_play().T
        a = df.values
        b = (a == a[:, [0]]).all(axis=1)
        count = np.count_nonzero(b)
        return count
    def combo(self):
        '''
    PURPOSE: returns the different combos of die faces and the frequency they appeared
    
    INPUTS
    
    OUTPUT
    combo    die combo frequencies
    '''
        self._result = self.game_object.show_play().T
        self.combo = self._result.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')
        return self.combo
    
    def face_counts(self):
        '''
    PURPOSE: roll the die n times
    
    INPUTS
    num_rolls    number of times to roll die, default =1 
    
    OUTPUT
    list of faces from the rolls
    '''
        self._result = self.game_object.show_play().T
        self.face_counts = self._result.apply(pd.Series.value_counts, axis=1).fillna(0)
        return self.face_counts.astype(int)
                    