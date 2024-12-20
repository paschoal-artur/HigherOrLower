from src.core.game import Game
from src.utils.display import display_logo

def main():
    display_logo()
    # passing the four required class arguments
    game = Game(
        data_file='data/game_data_with_formatting.csv',
        player_data_file = 'data/player_data.txt',
    )
    game.main_menu()

if __name__ == "__main__":
    main()