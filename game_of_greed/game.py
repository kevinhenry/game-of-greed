from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


def dice_to_string(tuple):
    string = "*** "
    for dice in tuple:
        string += f"{dice} "
    string += "***"
    return string


def split(string):
    return [char for char in string]


class Game:
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6
        self.bank = Banker()

    def print_welcome_message(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

    def display_roll_dice(self, roller):
        print(f"Rolling {self.remaining_dice} dice...")
        new_dice = dice_to_string(roller(self.remaining_dice))
        print(new_dice)

    def shelf_the_score(self, users_pick):
        num_string_list = split(users_pick)
        users_dice_picks = tuple([int(val) for val in num_string_list])
        score = GameLogic.calculate_score(users_dice_picks)
        self.bank.shelf(score)
        self.remaining_dice -= len(users_dice_picks)
        print(f"You have {score} unbanked points and {self.remaining_dice} dice remaining")

    def bank_the_score(self):
        banked = self.bank.bank()
        print(f"You banked {banked} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")
        self.round += 1
        self.remaining_dice = 6

    def play(self, roller=GameLogic.roll_dice):

        self.print_welcome_message()

        ask_user_to_play = input("> ")
        if ask_user_to_play == "n" or ask_user_to_play == "no":
            print("OK. Maybe another time")
            return

        playing = True
        while playing:

            print(f"Starting round {self.round}")

            same_round = True
            while same_round:

                self.display_roll_dice(roller)
                print("Enter dice to keep, or (q)uit:")
                user_answer = input("> ")

                if user_answer == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    return

                elif int(user_answer):

                    self.shelf_the_score(user_answer)

                    print("(r)oll again, (b)ank your points or (q)uit:")
                    ask_again = input("> ")

                    if ask_again == "r":
                        # we want to keep rolling
                        pass

                    elif ask_again == "b":
                        self.bank_the_score()
                        same_round = False

                    elif ask_again == "q":
                        print(f"Thanks for playing. You earned {self.bank.balance} points")
                        return


if __name__ == "__main__":

    game = Game()
    game.play(GameLogic.roll_dice)
