import os 
from typing import Dict

def load_players(file_path: str) -> Dict[str, Dict[str, int]]:
    """Method to load the players from a file"""

    players: Dict[str, Dict[str, int]] = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                name, high, prev = line.strip().split(',')
                players[name] = {"high_score": int(high), "previous_score": int(prev)}
    return players

def save_new_player(file_path: str, name: str) -> bool:
    """Method to save a new player to the file"""

    try:
        players = load_players(file_path)
        if name in players:
            return False
        with open(file_path, 'a') as file:
            file.write(f'{name},0,0\n')
        return True
    except Exception as e:
        print(f"Error saving new player: {e}")
        return False 

def remove_player(file_path: str, player_name: str) -> bool:
    """Method to remove a player from the file"""

    try:
        players = load_players(file_path)
        if player_name in players:
            del players[player_name]
            with open(file_path, 'w') as file:
                for name, scores in players.items():
                    file.write(f"{name},{scores['high_score']},{scores['previous_score']}\n")
            return True
    except Exception as e:
        print(f"Error removing player: {e}")
        return False

def update_player_score(file_path: str, player_name: str, current_score: int, high_score: int) -> None:
    """Method to update a player's score in the file"""
    players = load_players(file_path)
    try:
        # Verificar se o jogador já existe
        if player_name in players:
            players[player_name]["high_score"] = max(high_score, players[player_name]["high_score"])
            players[player_name]["previous_score"] = current_score
        else:
            # Se o jogador não existir, criar uma nova entrada
            players[player_name] = {"high_score": high_score, "previous_score": current_score}
        # Salva todos os jogadores novamente
        with open(file_path, 'w') as file:
            for name, scores in players.items():
                file.write(f"{name},{scores['high_score']},{scores['previous_score']}\n")
    except Exception as e:
        print(f"Error updating player score: {e}")


