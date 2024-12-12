import os 

def load_player_name(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [name.strip() for name in file.readlines() if name.strip()]
    return []

def save_player_name(file_path, name):
    names = load_player_name(file_path)
    if name in names:
        return False
    with open(file_path, 'a') as file:
        file.write(f'{name}\n')
    return True 

def load_player_score(file_path, player_name):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            # Search for the player's score in the file
            for line in file.readlines():
                name, score = line.strip().split(',')
                if name == player_name:
                    return int(score)
    return 0  # Return 0 if the player does not have a score saved yet

def save_player_score(file_path, player_name, score):
    scores = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            # Load all existing scores
            for line in file.readlines():
                name, score_value = line.strip().split(',')
                scores[name] = int(score_value)
    
    scores[player_name] = score

    with open(file_path, 'w') as file:
        for name, score_value in scores.items():
            file.write(f"{name},{score_value}\n")