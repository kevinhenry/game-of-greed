import random
from collections import Counter

DIE_POINTS = {1: 100, 5: 50}
TRIPLET_POINTS = {1: 1000 - 3 * DIE_POINTS[1],
                  2: 200,
                  3: 300,
                  4: 400,
                  5: 500 - 3 * DIE_POINTS[5],
                  6: 600}


class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple):
        """
        INPUTS >>  Tuple - a collection of numbers from 1-6. Length can be 1-6
        OUTPUT >>  Integer - score based on the collection of dice
        
        """
        count = Counter(tuple)

        if len(count) == 6:
            return 1500

        if len(count) == 1 and len(tuple) == 6:
            if tuple[0] == 1:
                return 4000

        for property in count:
            print("this is from line 42:", property, count[property])
            if count[property] == 6:
                return property * 100 * 2 * 2


        result = 0
        if len(tuple) <= 6:
            counts = Counter(tuple)
            for number, count in counts.items():
                result += count * DIE_POINTS.get(number, 0)
                if count == 3:
                    result += TRIPLET_POINTS[number]
                    continue
                if count == 4:
                    result += TRIPLET_POINTS[number] * 2
                    continue
                if count == 5:
                    result += TRIPLET_POINTS[number] * 3
                    continue
                
        return result

    @staticmethod
    def roll_dice(num_dice):
        """
        INPUT >> Integer - a number between 1 and 6
        OUTPUT >> Tuple - with length of input with numbers between 1 and 6
        """
        dice_list =  []
        for dice in range(num_dice):
            dice_list.append(random.randint(1, 6))
        return tuple(dice_list)



if __name__ == "__main__":

    input1 = (1, 1, 1, 1, 1, 1)   
    # result1 = Counter(input1)
    result = GameLogic.calculate_score(input1)
    print(result)  
