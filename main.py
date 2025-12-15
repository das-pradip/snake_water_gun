import random

class SnakeWaterGun:
    
    def reset_game(self):
       self.user_score = 0
       self.computer_score = 0

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choices = {1: "Snake", -1: "Water", 0: "Gun"}


    def play_round(self, user_choice):
        computer = random.choice([1, -1, 0])

        if user_choice == computer:
            result = "Tie"
        elif (user_choice == 1 and computer == -1) or \
             (user_choice == -1 and computer == 0) or \
             (user_choice == 0 and computer == 1):
            result = "Win"
            self.user_score += 1
        else:
            result = "Lose"
            self.computer_score += 1

        return {
            "user_choice": self.choices[user_choice],
            "computer_choice": self.choices[computer],
            "result": result,
            "user_score": self.user_score,
            "computer_score": self.computer_score
        }

