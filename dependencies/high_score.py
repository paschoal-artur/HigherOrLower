import os 

class HighScoreManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_high_score(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                score = file.read().strip()
                return int(score) if score else 0
        return 0
    
    def save_high_score(self, score):
        with open(self.file_path, 'w') as file:
            file.write(str(score))