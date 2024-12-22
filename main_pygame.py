import pygame 
import sys 
from src.core.game import Game
import os

os.environ['SDL_AUDIODRIVER'] = 'dummy'

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Higher or Lower")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

STATE_MENU = "menu"
STATE_GAME = "game"
STATE_RANKINGS = "rankings"
STATE_QUIT = "quit"


# Função para desenhar o menu principal
def draw_menu():
    screen.fill(WHITE)
    title = font_large.render("Higher or Lower", True, BLUE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    options = ["1. Play the Game", "2. View Rankings", "3. Quit"]
    for i, option in enumerate(options):
        text = font_small.render(option, True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 250 + i * 80))

# Função para desenhar os rankings
def draw_rankings(rankings):
    screen.fill(WHITE)
    title = font_large.render("Rankings", True, BLUE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    for i, (name, score) in enumerate(rankings):
        text = font_small.render(f"{i + 1}. {name}: {score}", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 150 + i * 40))

    back_text = font_small.render("Press ESC to return to the menu", True, RED)
    screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 50))

# Função principal do jogo (será executada no estado "game")
def play_game(game: Game):
    running = True
    while running:
        # Evento para sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aqui você executa a lógica do jogo
        screen.fill(WHITE)
        game.play()
        running = False  # Termina o jogo depois de uma rodada para retornar ao menu principal

# Função para obter rankings
def get_rankings(game: Game):
    rankings = game.get_player_rankings()
    return sorted(rankings.items(), key=lambda x: x[1], reverse=True)  # Ordena pelo score

# Loop principal
def main():
    current_state = STATE_MENU
    game = Game(
        data_file="data/game_data_with_formatting.csv",
        player_data_file="data/player_data.txt"
    )

    while current_state != STATE_QUIT:
        if current_state == STATE_MENU:
            draw_menu()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_state = STATE_QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # Tecla 1: Jogar
                        current_state = STATE_GAME
                    elif event.key == pygame.K_2:  # Tecla 2: Rankings
                        current_state = STATE_RANKINGS
                    elif event.key == pygame.K_3:  # Tecla 3: Sair
                        current_state = STATE_QUIT

        elif current_state == STATE_GAME:
            play_game(game)
            current_state = STATE_MENU

        elif current_state == STATE_RANKINGS:
            rankings = get_rankings(game)
            draw_rankings(rankings)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_state = STATE_QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Tecla ESC: Voltar ao menu
                        current_state = STATE_MENU

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()