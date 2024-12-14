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
            for line in file:
                name, high, prev = line.strip().split(',')
                if name == player_name:
                    return int(high), int(prev)  # Return both scores
    return 0, 0  # Default scores if player not found


def remove_player_name(file_path, player_name):
    names = load_player_name(file_path)
    if player_name in names:
        names.remove(player_name)
        with open(file_path, 'w') as file:
            for name in names:
                file.write(f'{name}\n')
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

def save_player_score(file_path, player_name, current_score, high_score):
    scores = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                name, high, prev = line.strip().split(',')
                scores[name] = {"high_score": int(high), "previous_score": int(prev)}

    # Update or create the player's score entry
    if player_name in scores:
        scores[player_name]["high_score"] = max(high_score, scores[player_name]["high_score"])
        scores[player_name]["previous_score"] = current_score
    else:
        scores[player_name] = {"high_score": high_score, "previous_score": current_score}

    # Write updated scores back to the file
    with open(file_path, 'w') as file:
        for name, score_data in scores.items():
            file.write(f"{name},{score_data['high_score']},{score_data['previous_score']}\n")

