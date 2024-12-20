import pandas as pd
from src.utils.game_data import load_game_data

def test_load_game_data():
    data = load_game_data("data/mock_data.csv")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "name" in data.columns
    assert "value" in data.columns
