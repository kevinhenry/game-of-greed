import random

class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple):
        """
        INPUTS >>  Tuple - a collection of numbers from 1-6. Length can be 1-6
        OUTPUT >>  Integer - score based on the collection of dice
        
        """
        pass

    @staticmethod
    def roll_dice(num_dice):
        """
        INPUT >> Integer - a number between 1 and 6
        OUTPUT >> Tuple - with length of input with numbers between 1 and 6
        """
        a_list =  []
        for dice in range(num_dice):
            a_list.append(random.randint(1, 6))
        return tuple(a_list)


        