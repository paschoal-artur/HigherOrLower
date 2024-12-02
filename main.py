from dependencies.art import logo
from game import Game

print(logo)

game = Game('dependencies/game_data.csv')
game.play()