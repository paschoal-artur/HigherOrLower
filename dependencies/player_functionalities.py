import os 

def load_players(file_path):
    players = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                name, high, prev = line.strip().split(',')
                players[name] = {"high_score": int(high), "previous_score": int(prev)}
    return players

def save_new_player(file_path, name):
    players = load_players(file_path)
    if name in players:
        return False
    with open(file_path, 'a') as file:
        file.write(f'{name},0,0\n')
    return True 

def remove_player(file_path, player_name):
    players = load_players(file_path)
    if player_name in players:
        del players[player_name]
        with open(file_path, 'w') as file:
            for name, scores in players.items():
                file.write(f"{name},{scores['high_score']},{scores['previous_score']}\n")
        return True
    return False

def remove_player_score(file_path, player_name):
    if os.path.exists(file_path):
        try:
            scores = {}
            with open(file_path, 'r') as file:
                for line in file.readlines():
                    name, score_value = line.strip().split(',')
                    scores[name] = int(score_value)
            if player_name in scores:
                del scores[player_name]
                with open(file_path, 'w') as file:
                    for name, score_value in scores.items():
                        file.write(f"{name},{score_value}\n")
                return True 
            else:
                print(f"Player {player_name} not found in scores.")
                return False 
        except Exception as e:
            print(f"Error removing player score: {e}")
            return False
    else:
        print(f"Score file {file_path} does not exist.")
        return False 

def update_player_score(file_path, player_name, current_score, high_score):
    players = load_players(file_path)
    players[player_name] = {
        "high_score": max(high_score, players.get(player_name, {}).get("high_score", 0)),
        "previous_score": current_score,
    }

    # Salva todos os jogadores novamente
    with open(file_path, 'w') as file:
        for name, scores in players.items():
            file.write(f"{name},{scores['high_score']},{scores['previous_score']}\n")


