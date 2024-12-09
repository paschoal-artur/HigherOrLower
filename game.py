import pandas as pd
import random
from dependencies.art import vs
import os 

class Player:
    def __init__(self):
        self.name = ""
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
    def __init__(self,data_file):
        self.df = pd.read_csv(data_file)
        self.player = Player()
        self.row = None
        self.row2 = None 
        self.high_score_file = 'dependencies/high_score_file.txt'
        self.high_score = self.load_high_score()

        self.load_player_name()

    def load_high_score(self):
        #carrega maior pontuação do arquivo
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, 'r') as file:
                    score = file.read().strip()  # Remove espaços ou quebras de linha
                    return int(score) if score else 0  # Converte para int ou retorna 0 se estiver vazio
            except ValueError:
                print("O arquivo de high score contém dados inválidos. Configurando a pontuação inicial como 0.")
                return 0  # Em caso de erro de conversão, retorna 0
        else:
            return 0
 
    def save_high_score(self):
        #salva maior pontuação do arquivo
        with open(self.high_score_file, 'w') as file:
            file.write(str(self.high_score))

    def save_player_name(self):
        with open('dependencies/player_name.txt', 'w') as file:
            file.write(self.player.name)
    
    def load_player_name(self):
        # Verifica se o arquivo de nome do jogador existe
        file_path = 'dependencies/player_name.txt'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                name = file.read().strip()  # Remove espaços ou linhas em branco
                if name:  # Verifica se o nome não está vazio
                    self.player.name = name
                    return
        # Se o arquivo não existir ou estiver vazio, solicita o nome do jogador
        self.player.name = input("Enter your name: ").strip().lower()
        self.save_player_name()  # Salva o nome do jogador no arquivo

    def get_random_row(self, exclude = None):
        row = random.choice(self.df.index)
        while row == exclude:
            row = random.choice(self.df.index)
        return row 

    def display_choices(self):
        print(f"{self.df['name'][self.row]} has {self.df['value'][self.row]} average monthly researches")
        print(vs)
    
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
        print(f'Welcome {self.player.name}!')
        print(f'High Score: {self.high_score}')
        print('\n')
        self.row = self.get_random_row()
        self.row2 = self.get_random_row(self.row)
        while not self.player.lost:
            self.display_choices()
            choice = self.get_user_choice()
            if self.check_answer(choice):
                self.player.increment_score()
                print('\n')
                print(f"Correct! Current score: {self.player.score}")
                print('\n')
                self.update_game_state()
            else:
                print(f"Wrong! Final score: {self.player.score}")
                self.player.lose()

        # Verifica se a pontuação atual do jogador é maior que o high score
        if self.player.score > self.high_score:
            self.high_score = self.player.score
            print(f"New High Score: {self.high_score}")
            self.save_high_score()  # Salva a nova pontuação mais alta

        print(f'Game over! Your final score is {self.player.score}')

