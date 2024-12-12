import os 

def load_player_name(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip().split('\n')
        return [name.strip() for name in names if name.strip()]
    return []

def save_player_name(file_path, name):
    names = load_player_name(file_path)
    if name in names:
        return False
    else:
        with open(file_path, 'a') as file:
            file.write(f'{name}\n')
        return True 