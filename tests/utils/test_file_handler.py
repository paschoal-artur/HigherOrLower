import os
import pytest
from src.utils.file_handler import load_players, save_new_player, update_player_score, remove_player

@pytest.fixture
def mock_file(tmp_path):
    file_path = tmp_path / "mock_players.txt"
    with open(file_path, "w") as f:
        f.write("Player1,10,5\nPlayer2,20,15\n")
    return file_path

def test_load_players(mock_file):
    players = load_players(mock_file)
    assert len(players) == 2
    assert players["Player1"]["high_score"] == 10

def test_save_new_player(mock_file):
    assert save_new_player(mock_file, "Player3")
    players = load_players(mock_file)
    assert "Player3" in players

def test_update_player_score(mock_file):
    update_player_score(mock_file, "Player1", 25, 30)
    players = load_players(mock_file)
    assert players["Player1"]["high_score"] == 30
    assert players["Player1"]["previous_score"] == 25

def test_remove_player(mock_file):
    assert remove_player(mock_file, "Player1")
    players = load_players(mock_file)
    assert "Player1" not in players
