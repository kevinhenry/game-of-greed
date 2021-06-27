from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from helper_functions.helpers import dice_to_string, string_to_list


class Game:
    def __init__(self):
        self.round = 1
        self.bank = Banker()
        self.saved_dice = []
        self.remaining_dice = 6

    def print_welcome_message(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

    def display_new_roll(self, roller):
        print(f"Rolling {self.remaining_dice} dice...")
        new_dice_string = dice_to_string(roller(self.remaining_dice))
        print(new_dice_string)

    def shelf_the_score(self, score):
        self.bank.shelved = score
        print(f"You have {self.bank.shelved} unbanked points and {self.remaining_dice} dice remaining")

    def bank_the_score(self):
        banked = self.bank.bank()
        print(f"You banked {banked} points in round {self.round}")
        print(f"Total score is {self.bank.balance} points")

    def start_new_round(self):
        self.bank_the_score()
        self.round += 1
        self.remaining_dice = 6
        self.saved_dice = []

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

                self.display_new_roll(roller)
                user_answer = input("Enter dice to keep, or (q)uit:\n> ")

                try:

                    if user_answer == "q":
                        print(f"Thanks for playing. You earned {self.bank.balance} points")
                        return

                    self.saved_dice += string_to_list(user_answer)
                    self.remaining_dice = 6 - len(self.saved_dice)
                    current_score = GameLogic.calculate_score(tuple(self.saved_dice))
                    self.shelf_the_score(current_score)

                    ask_again = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

                    if ask_again == "r":
                        continue

                    elif ask_again == "b":
                        self.start_new_round()
                        same_round = False

                    elif ask_again == "q":
                        print(f"Thanks for playing. You earned {self.bank.balance} points")
                        return

                except ValueError as error:
                    print(" ** --------- Error: Please check your entry --------- **")
                    print("Your options are (r)oll again, (b)ank your points or (q)uit")


if __name__ == "__main__":

    game = Game()
    game.play(GameLogic.roll_dice)
