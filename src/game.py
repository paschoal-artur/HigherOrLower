import random
from dependencies.art import display_vs
from dependencies.game_data import load_game_data
from dependencies.player_functionalities import *  
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
    def __init__(self,data_file, high_scores, player_name_file, player_scores):
        self.df = load_game_data(data_file)
        self.player = Player()
        self.row = None
        self.row2 = None 
        self.high_score_manager = HighScoreManager(high_scores)
        self.high_score = self.high_score_manager.load_high_score()
        self.player_name_file = player_name_file
        self.player_score_file = player_scores
        self.all_player_names = load_player_name(self.player_name_file)

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Choose a player")
            print("2. Create a new player")
            print("3. Remove a player")
            print("4. Play the game")
            print("5. Quit")

            choice = int(input("\nEnter the number of your choice: ").strip())
            if choice == 1:
                self.choose_player()
            elif choice == 2:
                self.create_new_player()
            elif choice == 3:
                self.remove_player_menu()
            elif choice == 4:
                if not self.player.name:
                    print("Please choose a player first.")
                    load_player_name(self.player_name_file)
                else:
                    self.play()
            elif choice == 5:
                print("Thanks for playing, goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


    def choose_player(self):
        self.all_player_names = load_player_name(self.player_name_file)
        if self.all_player_names:
            print("\nChoose your player name:")
            for idx, name in enumerate(self.all_player_names, start=1):
                print(f"{idx}. {name}")
            print(f"{len(self.all_player_names) + 1}. Cancel")

            choice = input("\nEnter the number of your choice: ").strip()

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.all_player_names):
                    self.player.name = self.all_player_names[choice - 1]
                    high_score, previous_score = load_player_score(self.player_score_file, self.player.name)
                    print(f"\nWelcome back, {self.player.name}!")
                    print(f"Your high score: {high_score}")
                    print(f"Your previous score: {previous_score}")
                    self.player.reset_score()  # Reset the score for the new game

                    self.player_menu()

                elif choice == len(self.all_player_names) + 1:
                    print("Returning to main menu.")
                else:
                    print("Invalid choice. Please try again.")
                    self.choose_player()  # Retry if input is invalid
            else:
                print("Invalid input. Please enter a number.")
                self.choose_player()  # Retry if input is invalid
        else:
            print("\nNo players found. Let's create a new player!")
            self.create_new_player()

    def load_player_name(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return [name.strip() for name in file.readlines() if name.strip()]
        return []
    
    def remove_player_menu(self):
        # Load the player names correctly by passing the file path
        all_names = load_player_name(self.player_name_file)

        if all_names:
            print("\nSelect a player to remove:")
            for idx, name in enumerate(all_names, start=1):
                print(f"{idx}. {name}")
            print(f"{len(all_names) + 1}. Cancel")

            choice = input("\nEnter the number of the player to remove: ").strip()

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(all_names):
                    player_to_remove = all_names[choice - 1]
                    confirm = input(f"Are you sure you want to remove {player_to_remove}? (Y/N): ").strip().lower()
                    if confirm == "y":
                        remove_name_success = remove_player_name(self.player_name_file, player_to_remove)
                        remove_score_success = remove_player_score(self.player_score_file, player_to_remove)
                        if remove_name_success and remove_score_success:
                            print(f"Player '{player_to_remove}' removed successfully.")
                            # Refresh the player list
                            self.all_player_names = load_player_name(self.player_name_file)
                        elif remove_name_success and not remove_score_success:
                            print(f"Player '{player_to_remove}' removed from names but not found in scores.")
                            self.all_player_names = load_player_name(self.player_name_file)  # Refresh list
                        else:
                            print(f"Error: Unable to remove player '{player_to_remove}'.")
                    else:
                        print("Player removal canceled.")
                elif choice == len(all_names) + 1:
                    print("Returning to main menu.")
                else:
                    print("Invalid choice. Please try again.")
                    self.remove_player_menu()  # Retry if input is invalid
            else:
                print("Invalid input. Please enter a number.")
                self.remove_player_menu()  # Retry if input is invalid
        else:
            print("No players available to remove.")
        
        # Always return to the main menu after execution
        self.main_menu()

    def player_menu(self):
        high_score, previous_score = load_player_score(self.player_score_file, self.player.name)
        while True:
            print(f"\n--- {self.player.name}'s Menu ---")
            print(f"High Score: {high_score}")
            print(f"Previous Score: {previous_score}")
            print("1. Play the game")
            print("2. Return to main menu")
            print("3. Quit game")

            choice = int(input("\nEnter the number of your choice: ").strip())
            if choice == 1:
                self.play()
                break #sair do menu do jogador após o jogo
            elif choice == 2:
                print("Returning to main menu. . . .")
                self.main_menu()
                break 
            elif choice == 3:
                print("Thanks for playing, goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")

    def create_new_player(self):
        new_name = input("Enter your name: ").strip()
        if new_name:
            save_success = save_player_name(self.player_name_file, new_name)
            if save_success:
                print(f"\nPlayer '{new_name} added successfully!!")
                self.all_player_names = load_player_name(self.player_name_file)
                self.player.name = new_name
            else:
                print("Name already exists. Please choose another name.")
                self.create_new_player()

    def remove_player(self):
        if self.player.name:
            remove_name_success = remove_player_name(self.player_name_file, self.player.name)
            remove_score_success = remove_player_score(self.player_score_file, self.player.name)
            
            if remove_name_success and remove_score_success:
                print(f"Player {self.player.name} removed successfully.")
                # Reset the player object
                self.player.name = ""
                self.player.reset_score()
                # Optionally reload players or prompt for a new player
                self.all_player_names = load_player_name(self.player_name_file)
            else:
                print(f"Error: Unable to remove player {self.player.name}.")
        else:
            print("No player to remove.")
        self.main_menu()

    def save_game_state(self):
        save_player_score(self.player_score_file, self.player.name, self.player.score)

    def get_random_row(self, exclude = None):
        row = random.choice(self.df.index)
        while row == exclude:
            row = random.choice(self.df.index)
        return row 

    def display_choices(self):
        print(f"{self.df['name'][self.row]} has {self.df['formatted_value'][self.row]} average monthly searches")
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

        save_player_score(
            self.player_score_file,
            self.player.name,
            self.player.score,  # Current score (previous score)
            max(self.high_score, self.player.score)  # Update high score if applicable
        )

        # Update the high score in memory
        self.high_score = max(self.high_score, self.player.score)

