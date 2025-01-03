import random
from typing import Dict, Optional, Set
from src.utils import display_vs, load_game_data, load_players, remove_player, save_new_player, update_player_score
from .player import Player
import pandas as pd

class Game:
    """Class that represents the game core logic and functionality, 
    including game management, player management and data handling."""

    def __init__(self,data_file: str, player_data_file: str) -> None:
        self.df: pd.DataFrame = load_game_data(data_file)
        self.player: Player = Player()
        self.row: Optional[int] = None
        self.row2: Optional[int] = None 
        self.player_data_file: str = player_data_file
        self.players: Dict[str, Dict[str, int]] = load_players(self.player_data_file)
        self.high_score: int = self.get_game_high_score()
        self.used_rows: Set[int] = set()

    def get_game_high_score(self):
        """Returns the highest score among all players."""

        return max((data["high_score"] for data in self.players.values()), default=0)

    def main_menu(self):
        """Main menu of the game, where the player can choose to play, create a new player, 
        remove a player or quit the game."""

        while True:
            try:
                print("\n--- Main Menu ---")
                print(f"Game High Score: {self.high_score}")
                print("1. Choose a player")
                print("2. Create a new player")
                print("3. Remove a player")
                print("4. Quit")

                choice = int(input("\nEnter the number of your choice: ").strip())
                if choice == 1:
                    self.choose_player()
                elif choice == 2:
                    self.create_new_player()
                elif choice == 3:
                    self.remove_player_menu()
                elif choice == 4:
                    print("Thanks for playing, goodbye!")
                    exit()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def choose_player(self):
        """Method to choose a player from the list of players or create a new player."""

        if self.players:
            print("\nChoose your player name:")
            for idx, name in enumerate(self.players.keys(), start=1):
                print(f"{idx}. {name}")
            print(f"{len(self.players) + 1}. Return to main menu")

            choice = input("\nEnter the number of your choice: ").strip()

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.players):
                    self.player.name = list(self.players.keys())[choice - 1]
                    print(f"\nWelcome back, {self.player.name}!")
                    self.player.reset_score()  # Reset the score for the new game
                    self.player_menu()

                elif choice == len(self.players) + 1:
                    print("Returning to main menu. . . .")
                else:
                    print("Invalid choice. Please try again.")
                    self.choose_player()  # Retry if input is invalid
            else:
                print("Invalid input. Please enter a number.")
                self.choose_player()  # Retry if input is invalid
        else:
            print("\nNo players found. Let's create a new player!")
            self.create_new_player()

    def create_new_player(self):
        """Method to create a new player and add it to the list of players."""

        new_name = input("Enter your name: ").strip()
        if new_name:
            if save_new_player(self.player_data_file, new_name):
                print(f"Player {new_name} added successfully!")
                self.players = load_players(self.player_data_file)
            else:
                print("Name already exists. Please choose another one.")

    def remove_player_menu(self):
        """Method to remove a player from the list of players."""

        if self.players:
            print("\nSelect a player to remove:")
            for idx, name in enumerate(self.players.keys(), start=1):
                print(f"{idx}. {name}")
            print(f"{len(self.players) + 1}. Cancel")

            choice = input("\nEnter the number of the player to remove: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.players):
                    player_to_remove = list(self.players.keys())[choice - 1]
                    confirm = input(f"Are you sure you want to remove {player_to_remove}? (Y/N): ").strip().lower()
                    if confirm == "y":
                        if remove_player(self.player_data_file, player_to_remove):
                            print(f"Player '{player_to_remove}' removed successfully.")
                            self.players = load_players(self.player_data_file)  # Atualiza a lista
                        else:
                            print(f"Error: Unable to remove player '{player_to_remove}'.")
                    else:
                        print("Player removal canceled.")
                elif choice == len(self.players) + 1:
                    print("Returning to main menu.")
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("No players available to remove.")


    def player_menu(self):
        """Menu for the player to play the game, return to the main menu or quit the game."""

        while True:
            high_score = self.players[self.player.name]["high_score"]
            previous_score = self.players[self.player.name]["previous_score"]

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

    def remove_player(self):
        """Method to remove the current player from the list of players."""

        if self.player.name:
            if remove_player(self.player_data_file, self.player.name):
                print(f"Player {self.player.name} removed successfully.")
                # Reset the player object
                self.player.name = ""
                self.player.reset_score()
                # Optionally reload players or prompt for a new player
                self.players = load_players(self.player_data_file)
            else:
                print(f"Error: Unable to remove player {self.player.name}.")
        else:
            print("No player to remove.")
        self.main_menu()

    def save_game_state(self):
        """Method to save the current game state, including the player's score and high score."""

        update_player_score(
            self.player_data_file,
            self.player.name,
            self.player.score,  # Current score
            self.high_score  # Update high score if applicable
        )
        self.players = load_players(self.player_data_file)

    def get_random_row(self, exclude = None):
        """Method to get a random row from the data file, excluding the row passed as an argument."""

        if not hasattr(self, 'used_rows'):
            self.used_rows = set()

        available_rows = [row for row in self.df.index if row not in self.used_rows and row != exclude]
        if not available_rows:
            print("No more rows available, you've completed the game!!")
            self.used_rows.clear()
            available_rows = self.df.index.tolist()
        
        chosen_row = random.choice(available_rows)
        self.used_rows.add(chosen_row)
        return chosen_row

    def display_choices(self):
        """Method to display the two choices to the player."""
        
        print(f"{self.df['name'][self.row]} has {self.df['formatted_value'][self.row]} average monthly searches")
        display_vs()

    def get_user_choice(self):
        """Method to get the user's choice of 'higher' or 'lower'."""

        choice = input(f"{self.df['name'][self.row2]} has Higher or Lower searches than {self.df['name'][self.row]} ?\n").lower()
        while choice not in ['h', 'l']:
            print("Invalid choice. Please type 'H' or 'L'")
            choice = input(f"{self.df['name'][self.row2]} has Higher or Lower searches than {self.df['name'][self.row]} ?\n").lower()
        return choice

    def check_answer(self, choice):
        """Method to check if the user's choice is correct."""

        value1 = self.df['value'][self.row]
        value2 = self.df['value'][self.row2]

        if value1 == value2:
            return True
        return (choice == 'h' and value2 > value1) or (choice == 'l' and value2 < value1)

    def update_game_state(self):
        """Method to update the game state after the user's answer."""
        self.row = self.row2
        self.row2 = self.get_random_row(self.row)
    
    def play(self):
        """Method to start the game and manage the game flow."""
        self.used_rows = set()

        self.row = self.get_random_row()
        self.row2 = self.get_random_row(exclude=self.row)

        while not self.player.lost:
            self.display_choices()
            choice = self.get_user_choice()

            if self.check_answer(choice):
                self.player.increment_score()
                print(f"Correct! Current score: {self.player.score}")

                if self.player.score > self.high_score:
                    self.high_score = self.player.score
                    self.save_game_state()
                    print(f"New game high score: {self.high_score}")

                self.update_game_state()
            else:
                print(f"\nWrong! Final score: {self.player.score}")
                self.save_game_state()
                self.player.reset_score()
                self.player.lose()
                break 
        self.player_menu()
