from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


def print_dice(tuple):
    print(tuple)
    string = ""
    for dice in tuple:
        string += f" {dice}"
    string += " "
    return string


class Game:
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6

    def play(self, roller):
        bank = Banker()
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ask_user = input("> ")

        if ask_user == "n" or ask_user == "no":
            print("OK. Maybe another time")
        else:
            running = True  # Possibly change to count rounds
            while running:
                print(f"Starting round {self.round}")
                print("Rolling 6 dice...")
                dice = roller or GameLogic.roll_dice(self.remaining_dice)
                converted = print_dice(dice)
                # print("*** 4 2 6 4 6 5 ***")
                print("***{converted}***")

                print("Enter dice to keep, or (q)uit:")
                user_answer = input("> ")

                if user_answer == "q":
                    running = False
                    print(f"Thanks for playing. You earned {bank.balance} points")

                # elif :


if __name__ == "__main__":

    new_game = Game()
    new_game.play()


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
