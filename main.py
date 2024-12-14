from dependencies.art import display_logo
from src.game import Game

def main():
    display_logo()
    # passing the four required class arguments
    game = Game(
        data_file='data/game_data_with_formatting.csv',
        high_scores='dependencies/high_scores.txt',
        player_name_file='dependencies/player_name.txt',
        player_scores ='dependencies/player_scores.txt'
    )
    game.main_menu()

if __name__ == "__main__":
    main()