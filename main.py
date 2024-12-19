from dependencies.art import display_logo
from src.game import Game

def main():
    display_logo()
    # passing the four required class arguments
    game = Game(
        data_file='data/game_data_with_formatting.csv',
        player_data_file = 'dependencies/player_data.txt',
    )
    print(f"Welcome to the game!\nGame High Score: {game.high_score}")
    game.main_menu()

if __name__ == "__main__":
    main()