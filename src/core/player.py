class Player:
    """Class to represent a player in the game"""

    def __init__(self, name=""):
        self.name = name
        self.score = 0
        self.lost = False  
    
    def increment_score(self):
        """Increment the player's score by 1"""

        self.score += 1
    
    def lose(self):
        """Set the player's lost status to True"""

        self.lost = True 
    
    def reset_score(self):
        """Reset the player's score to 0"""
        
        self.score = 0
        self.lost = False