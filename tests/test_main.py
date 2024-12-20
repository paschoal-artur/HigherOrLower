from src.core.game import Game

def test_main_flow(mocker):
    mocker.patch("builtins.input", side_effect=["2", "TestUser", "5"])
    mocker.patch("builtins.print")  # To suppress print outputs during test
    game = Game(data_file="data/mock_data.csv", player_data_file="data/mock_players.txt")
    game.main_menu()
    assert "TestUser" in game.players
