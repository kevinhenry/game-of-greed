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

    def display_start_round(self, roller):
        print(f"Starting round {self.round}")
        print("Rolling 6 dice...")
        new_dice = dice_to_string(roller(self.remaining_dice))
        print(new_dice)
        print("Enter dice to keep, or (q)uit:")

    def play(self, roller=GameLogic.roll_dice):

        self.print_welcome_message()
        ask_user = input("> ")

        if ask_user == "n" or ask_user == "no":
            print("OK. Maybe another time")
        else:
            running = True
            while running:

                self.display_start_round(roller)
                user_answer = input("> ")

                if user_answer == "q":
                    running = False
                    print(f"Thanks for playing. You earned {self.bank.balance} points")

                elif int(user_answer):
                    num_string_list = split(user_answer)
                    users_dice_picks = tuple([int(val) for val in num_string_list])
                    score = GameLogic.calculate_score(users_dice_picks)
                    self.bank.shelf(score)
                    self.remaining_dice -= len(users_dice_picks)

                    print(f"You have {score} unbanked points and {self.remaining_dice} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")

                    ask_again = input("> ")

                    if ask_again == "r":
                        # we want to keep rolling
                        # print Rollling {remaining dice} dice...
                        #
                        pass

                    elif ask_again == "b":
                        banked = self.bank.bank()
                        print(f"You banked {banked} points in round {self.round}")
                        print(f"Total score is {self.bank.balance} points")
                        self.round += 1
                        self.remaining_dice = 6
                    elif ask_again == "q":
                        running = False
                        print(f"Thanks for playing. You earned {self.bank.balance} points")


if __name__ == "__main__":

    game = Game()
    game.play(GameLogic.roll_dice)
