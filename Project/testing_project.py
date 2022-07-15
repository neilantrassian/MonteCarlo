import unittest
from montecarlo import Die, Game, Analyzer
import pandas as pd
import numpy as np



class MonteCarloTestSuite(unittest.TestCase):
    def test_1_current_die(self):
        # create a die object
        instance = Die([1,2,3])
        #get current die into dict form
        test_die_dict = instance.current_die().to_dict()
        make_dict = {'face' : {1:1, 2:2, 3:3}, 'weights' :{1: 1.0, 2:1.0, 3: 1.0}}
        message = "assert current die is correct"
        self.assertEqual(test_die_dict, make_dict)
   
    def test_2_change_die_weight(self): 
        # create a die object
        instance = Die([1,2,3])
        # change die weight
        instance.change_weight(2, 200)
        #get current die into dict form
        test_die_dict = instance.current_die().to_dict()
        make_dict = {'face' : {1:1, 2:2, 3:3}, 'weights' :{1: 1.0, 2:1.0, 3: 200.0}}
        message = "assert dict equals change_die method's new weights"
        self.assertEqual(test_die_dict, make_dict)
    
    def test_3_roll_die(self): 
        # create a die object
        instance = Die([1,2,3])
        roll_count = len(instance.roll_die(4))
        #roll die 4 times, make sure it rolled four times
        test_die_roll = 4
        message = "assert rolled four times"
        self.assertEqual(test_die_roll, roll_count)
    
    def test_4_play_shape_wide(self):
        b = Die([1,2])
        c = Die([1,2])
        e = Die([1,2])
        dice = Game([b,c,e])
        dice.play(2)
        play_shape = np.shape(dice.show_play(wide = True))
        test_shape = (3, 2)
        message = "assert wide works"
        self.assertEqual(play_shape, test_shape)
    
    def test_5_play_shape_narrow(self):
        b = Die([1,2])
        c = Die([1,2])
        e = Die([1,2])
        dice = Game([b,c,e])
        dice.play(2)
        play_shape = np.shape(dice.show_play(wide = False))
        test_shape = (6, 1)
        message = "assert wide works"
        self.assertEqual(play_shape, test_shape)
        
    def test_6_jackpot(self):
        b = Die([1])
        c = Die([1])
        e = Die([1])
        dice = Game([b,c,e])
        dice.play(500)
        azr = Analyzer(dice)
        jack_num = azr.jackpot()
        test_num = 500
        message = "assert jackpot for 1 sided die returns number of plays"
        self.assertEqual(test_num, jack_num)

    def test_7_typing_for_die(self):
        message = "assert exception is raised since type is wrong"
        with self.assertRaises(Exception):
            d = Die([1.0,2.0,3.0])
            
    def test_8_value_of_change_weight(self):
        message = "assert exception is raised since value passed is not in faces_array"
        with self.assertRaises(Exception):
            b = Die([1,2,3,4,5,6])
            b.change_weight(8, 200)
            
    def test_9_typing_for_roll_die(self):
        message = "assert exception is raised since type is wrong"
        with self.assertRaises(Exception):
            d = Die([1,2,3])
            d.roll_die(7.5)
            
            
    def test_10_typing_for_game(self):
        message = "assert exception is raised since 7 isn't a die object"
        with self.assertRaises(Exception):
            b = Die([1,2,3]) 
            c = Die([1,2,3])
            dice = Game([7, b, c])
         

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)