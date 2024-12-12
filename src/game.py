import random
from dependencies.art import display_vs
from dependencies.game_data import load_game_data
from dependencies.player_functionalities import load_player_name, save_player_name, load_player_score, save_player_score
from dependencies.high_score import HighScoreManager

class Player:
    def __init__(self, name=""):
        self.name = name
        self.score = 0
        self.lost = False  
    
    def increment_score(self):
        self.score += 1
    
    def lose(self):
        self.lost = True 
    
    def reset_score(self):
        self.score = 0
        self.lost = False

class Game:
    def __init__(self,data_file, high_score_file, player_name_file, player_scores):
        self.df = load_game_data(data_file)
        self.player = Player()
        self.row = None
        self.row2 = None 
        self.high_score_manager = HighScoreManager(high_score_file)
        self.high_score = self.high_score_manager.load_high_score()
        self.player_name_file = player_name_file
        self.player_score_file = player_scores
        self.load_player_name()

    def load_player_name(self):
        print("Welcome to the Higher or Lower game!")
        all_names = load_player_name(self.player_name_file)

        # If there are existing player names
        if all_names:
            print("\nChoose your player name:")
            for idx, name in enumerate(all_names, start=1):
                print(f"{idx}. {name}")
            print(f"{len(all_names) + 1}. Create a new name")

            # Prompt the user for their choice
            choice = input("\nEnter the number of your choice: ").strip()

            # Handle user selection
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(all_names):
                    self.player.name = all_names[choice - 1]
                    print(f"\nWelcome back, {self.player.name}!")
                    self.player.score = load_player_score(self.player_score_file, self.player.name)
                    print(f"Your previous score: {self.player.score}")
                elif choice == len(all_names) + 1:
                    self.create_new_player()
                else:
                    print("Invalid choice. Please try again.")
                    self.load_player_name()  # Retry if input is invalid
            else:
                print("Invalid input. Please enter a number.")
                self.load_player_name()  # Retry if input is invalid
        else:
            # If there are no player names, prompt for a new one
            print("\nNo players found. Let's create a new player!")
            self.create_new_player()
    
    def create_new_player(self):
        new_name = input("Enter your name: ").strip()
        if new_name:
            save_success = save_player_name(self.player_name_file, new_name)
            if save_success:
                self.player.name = new_name
                print(f"\nWelcome, {self.player.name}!")
            else:
                print("Name already exists. Please choose another name.")
                self.create_new_player()

    def save_game_state(self):
        save_player_score(self.player_score_file, self.player.name, self.player.score)

    def get_random_row(self, exclude = None):
        row = random.choice(self.df.index)
        while row == exclude:
            row = random.choice(self.df.index)
        return row 

    def display_choices(self):
        print(f"{self.df['name'][self.row]} has {self.df['value'][self.row]} average monthly searches")
        display_vs()

    def get_user_choice(self):
        choice = input(f"{self.df['name'][self.row2]} has Higher or Lower searches than {self.df['name'][self.row]} ?\n").lower()
        while choice not in ['h', 'l']:
            print("Invalid choice. Please type 'H' or 'L'")
            choice = input(f"{self.df['name'][self.row2]} has Higher or Lower searches than {self.df['name'][self.row]} ?\n").lower()
        return choice

    def check_answer(self, choice):
        if choice == 'h':
            return self.df['value'][self.row2] > self.df['value'][self.row]
        elif choice == 'l':
            return self.df['value'][self.row] > self.df['value'][self.row2]
        return False 

    def update_game_state(self):
        self.row = self.row2
        self.row2 = self.get_random_row(self.row)
    
    def play(self):
        print(f"High Score: {self.high_score}\n")
        self.row = self.get_random_row()
        self.row2 = self.get_random_row(exclude=self.row)

        while not self.player.lost:
            self.display_choices()
            choice = self.get_user_choice()
            if self.check_answer(choice):
                self.player.increment_score()
                print(f"Correct! Current score: {self.player.score}")
                self.update_game_state()
            else:
                print(f"\nWrong! Final score: {self.player.score}")
                self.player.lose()

        if self.player.score > self.high_score:
            self.high_score = self.player.score
            print(f"New High Score: {self.high_score}")
            self.high_score_manager.save_high_score(self.high_score)
        
        self.save_game_state()

