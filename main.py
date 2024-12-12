from dependencies.art import display_logo
from src.game import Game

def main():
    display_logo()
    # Pass all three required arguments to the Game class
    game = Game(
        data_file='data/game_data.csv',
        high_score_file='dependencies/high_scores.txt',
        player_name_file='dependencies/player_name.txt'
    )
    game.play()

if __name__ == "__main__":
    main()