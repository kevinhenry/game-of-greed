from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


def print_dice(tuple):
    string = " "
    for dice in tuple:
        string += f"{dice} "
    return string


def split(string):
    return [char for char in string]


class Game:
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6

    def play(self, roller):
        bank = Banker()
        self.roller = roller or GameLogic.roll_dice  # Not sure why it needs this?

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ask_user = input("> ")

        if ask_user == "n" or ask_user == "no":
            print("OK. Maybe another time")
        else:
            running = True
            while running:

                print(f"Starting round {self.round}")
                print("Rolling 6 dice...")
                dice = self.roller(self.remaining_dice)
                # dice = GameLogic.roll_dice(self.remaining_dice)
                converted = print_dice(dice)
                print(f"***{converted}***")

                print("Enter dice to keep, or (q)uit:")
                user_answer = input("> ")

                if user_answer == "q":
                    running = False
                    print(f"Thanks for playing. You earned {bank.balance} points")

                elif user_answer == "b":
                    to_bank = bank.bank()
                    print(f"You banked {to_bank} points in round {self.round}")
                    print(f"Total score is {bank.balance} points")
                    self.round += 1

                elif int(user_answer):

                    split_numbers = split(user_answer)
                    converted = [int(val) for val in split_numbers]
                    converted_tuple = tuple(converted)

                    score = GameLogic.calculate_score(converted_tuple)
                    bank.shelf(score)
                    self.remaining_dice -= len(converted)

                    print(f"You have {score} unbanked points and {self.remaining_dice} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")

                    ask_again = input("> ")

                    if ask_again == "r":
                        # we want to keep rolling
                        # print Rollling {remaining dice} dice...
                        #
                        pass

                    elif ask_again == "b":
                        to_bank = bank.bank()
                        print(f"You banked {to_bank} points in round {self.round}")
                        print(f"Total score is {bank.balance} points")
                        self.round += 1
                        self.remaining_dice = 6
                    elif ask_again == "q":
                        running = False
                        print(f"Thanks for playing. You earned {bank.balance} points")


if __name__ == "__main__":

    # test1 = "1234"
    # print(test1)

    # split_list = split(test1)
    # print(split_list)

    # converted = [int(val) for val in split_list]

    # print(converted)
    # test2 = int("abc")
    # print(test1)
    game = Game()
    game.play(GameLogic.roll_dice)

"""
          Print Welcome Message
          Ask yes or No to play game
            if no
                 print(OK. Maybe another time)
            if yes

                declare continue = true
                while continue is true:
                      print
                          Starting round {self.round}
                          Rolling 6 dice...

                      dice = Call on GameLogic.roll_dice(6)
                      print string based dice 

                      print
                          Enter dice to keep, or (q)uit:

                      userAnswer = input(> )

                      if userAnswer is "q":
                          continue = false
                          print 
                              Thanks for playing. You earned {bank.bank} points

                      elif userAnswer is "b":
                          - bank the unshelved points
                          - print 
                              You banked {bank.shelf} points in round {self.round}
                              Total score is {bank.bank} points
                              increment {self.round}
                      

                      elif userAnswer is "r":
                          continue

                      elif userAnswers are numbers:
                          - grab the users answers
                          - calculate unbanked points 
                          - decrement {self.remaining_dice}
                          - print
                              You have {bank.shelf} unbanked points and {self.remaining_dice} dice remaining
                              (r)oll again, (b)ank your points or (q)uit:

            """
