import random
from collections import Counter

DIE_POINTS = {1: 100, 5: 50}
TRIPLET_POINTS = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple):
        """
        INPUTS >>  Tuple - a collection of numbers from 1-6. Length can be 1-6
        OUTPUT >>  Integer - score based on the collection of dice

        """
        counts = Counter(tuple)

        # Straights
        if len(counts) == 6:
            return 1500

        # 3 Pairs
        if len(counts) == 3:
            if all(value == 2 for value in counts.values()):
                return 1500

        result = 0

        for number, count in counts.items():
            if count < 3:
                result += count * DIE_POINTS.get(number, 0)
            elif count == 3:
                result += TRIPLET_POINTS[number]
            elif count == 4:
                result += TRIPLET_POINTS[number] * 2
            elif count == 5:
                result += TRIPLET_POINTS[number] * 3
            elif count == 6:
                result += TRIPLET_POINTS[number] * 4

        return result

    @staticmethod
    def roll_dice(num_dice):
        """
        INPUT >> Integer - a number between 1 and 6
        OUTPUT >> Tuple - with length of input with numbers between 1 and 6
        """
        dice_list = []
        for dice in range(num_dice):
            dice_list.append(random.randint(1, 6))
        return tuple(dice_list)

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        INPUT >> - Tuple - the actual list of dices
                 - Tuple - The users choice
        OUTPUT >>  Boolean - True/False if user picked from the actual list
        """
        count1 = Counter(roll)
        count2 = Counter(keepers)

        for number, count in count2.items():
            if number not in count1:
                return False
            elif count > count1[number]:
                return False
        return True

    @staticmethod
    def get_scorers(test_input):
        """
        INPUT >> Tuple - The dice list that was rolled
        OUPUT >> Tuple - Only the dices that are worth points
        """
        counts = Counter(test_input)

        # Straights
        if len(counts) == 6:
            return test_input

        # 3 Pairs
        if len(counts) == 3:
            if all(value == 2 for value in counts.values()):
                return test_input

        result = []

        for number, count in counts.items():
            if count >= 3:
                result += [number] * count
            elif number == 1 or number == 5:
                result += [number] * count

        return result


if __name__ == "__main__":
    pass
    # input1 = (1, 1, 1, 1, 1, 1)
    # result1 = Counter(input1)
    # result = GameLogic.calculate_score(input1)
    # print(result)
