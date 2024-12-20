import pytest 
from src.core.game import Game

@pytest.fixture
def mock_game():
    return Game(data_file="data/mock_data.csv", player_data_file="data/mock_players.txt")

def test_get_high_score(mock_game):
    mock_game.players = {
        "Player1": {"high_score": 10, "previous_score": 5},
        "Player2": {"high_score": 20, "previous_score": 15},
    }
    assert mock_game.get_game_high_score() == 20

def test_random_row_exclusion(mock_game):
    mock_game.df = mock_game.df.head(10)  # Mock data
    row1 = mock_game.get_random_row()
    row2 = mock_game.get_random_row(exclude=row1)
    assert row1 != row2