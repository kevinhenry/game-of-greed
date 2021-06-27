"""

class Game:
    def __init__(self):
        self.round = 1
        self.remaining_dice = 6


Print Welcome to Game of Greed
Print (y)es to play or (n)o to decline
ask_user for their input
    if user answer is no
        print(OK. Maybe another time)
    if user answer is yes
        declare running = true
        while running is true:
            print
            Starting round {self.round}
            Rolling {self.remaining_dice} dice...

                

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
