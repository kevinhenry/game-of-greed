import sys

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from helper_functions.helpers import dice_to_string, string_to_list


class Game:
    def __init__(self):
        self.round = 1
        self.bank = Banker()
        self.saved_dice = []
        self.remaining_dice = 6
        self.current_dice_options = []

    def print_welcome_message(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

    def display_new_roll(self, roller):
        print(f"Rolling {self.remaining_dice} dice...")
        self.current_dice_options = roller(self.remaining_dice)
        new_dice_string = dice_to_string(self.current_dice_options)
        print(new_dice_string)

    def shelf_the_score(self, score):
        self.bank.shelved = score
        print(f"You have {self.bank.shelved} unbanked points and {self.remaining_dice} dice remaining")

    def bank_the_score(self):
        banked = self.bank.bank()
        print(f"You banked {banked} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")

    def prepare_new_round(self):
        self.bank_the_score()
        self.round += 1
        self.remaining_dice = 6
        self.saved_dice = []
        self.current_dice_options = []

    def print_cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        new_dice_string = dice_to_string(self.current_dice_options)
        print(new_dice_string)

    def zilch(self):
        pass

    def quit_game(self):
        sys.exit(f"Thanks for playing. You earned {self.bank.balance} points")

    def play(self, roller=GameLogic.roll_dice):

        self.print_welcome_message()

        # need to account for other user options that will break this portion
        # maybe add a while loop to keep asking until valid response then move forward
        ask_user_to_play = input("> ")
        if ask_user_to_play == "n" or ask_user_to_play == "no":
            print("OK. Maybe another time")
            return

        playing = True
        while playing:

            print(f"Starting round {self.round}")

            same_round = True
            while same_round:

                self.display_new_roll(roller)

                keep_asking = True
                while keep_asking == True:

                    try:

                        user_answer = input("Enter dice to keep, or (q)uit:\n> ")
                        user_answer = user_answer.replace(" ", "")

                        if user_answer == "q":
                            self.quit_game()

                        print(f"user_answer line 81: {user_answer}")
                        string_version = string_to_list(user_answer)
                        # print("this should run twice")
                        print(f"string_versions line 84: {string_version}")
                    except ValueError as error:
                        print("line 86 got trigggered")
                        self.print_cheater()

                    print("this needs to run twice line 89")

                    result = GameLogic.validate_keepers(
                        roller(self.remaining_dice) or self.current_dice_options, string_version
                    )
                    print(f"result from line 94: {result}")

                    if result == True:
                        # print(f"string_versions line 88: {string_version}")
                        self.saved_dice += string_to_list(user_answer)
                        keep_asking = False
                        print("this is from line 95")
                    else:
                        print(f"string_versions line 97: {string_version}")
                        self.print_cheater()

                    print("does it get to here? line 100")

                self.remaining_dice = 6 - len(self.saved_dice)

                current_score = GameLogic.calculate_score(tuple(self.saved_dice))
                self.shelf_the_score(current_score)

                ask_again = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

                if ask_again == "r":
                    continue

                elif ask_again == "b":
                    self.prepare_new_round()
                    same_round = False

                elif ask_again == "q":
                    self.quit_game()


if __name__ == "__main__":

    # print(GameLogic.validate_keepers((5, 2, 3, 5, 4, 2), (5, 5)))
    try:
        game = Game()
        game.play()
    except KeyboardInterrupt:
        game.quit_game()
