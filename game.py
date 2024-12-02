import pandas as pd
import random
from dependencies.art import vs

class Option:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Player:
    def __init__(self):
        self.score = 0
        self.lost = False  
    
    def increment_score(self):
        self.score += 1
    
    def lose(self):
        self.lost = True 

class Game:
    def __init__(self,data_file):
        self.df = pd.read_csv(data_file)
        self.player = Player()
        self.row = None
        self.row2 = None 
    
    def get_random_row(self, exclude = None):
        row = random.choice(self.df.index)
        while row == exclude:
            row = random.choice(self.df.index)
        return row 

    def display_choices(self):
        print(f"Compare A: {self.df['name'][self.row]}")
        print(vs)
        print(f"Against B: {self.df['name'][self.row2]}")
    
    def get_user_choice(self):
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        while choice not in ['a', 'b']:
            print("Invalid choice. Please type 'A' or 'B'")
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        return choice 

    def check_answer(self, choice):
        if choice == 'a':
            return self.df['value'][self.row] > self.df['value'][self.row2]
        elif choice == 'b':
            return self.df['value'][self.row2] > self.df['value'][self.row]
        return False 

    def update_game_state(self):
        self.row = self.row2
        self.row2 = self.get_random_row(self.row)
    
    def play(self):
        while not self.player.lost:
            self.row = self.get_random_row()
            self.row2 = self.get_random_row(self.row)
            self.display_choices()
            choice = self.get_user_choice()
            if self.check_answer(choice):
                self.player.increment_score()
                print(f"Correct! Current score: {self.player.score}")
                self.update_game_state()
            else:
                print(f"Wrong! Final score: {self.player.score}")
                self.player.lose()
        print(f'Game over! Your final score is {self.player.score}')