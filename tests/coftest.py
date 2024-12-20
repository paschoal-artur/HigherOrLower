def test_get_high_score(mock_game):
    """
    Tests if the Game correctly calculates the highest score among players.
    """
    assert mock_game.get_game_high_score() == 20


def test_choose_player(mock_game):
    """
    Tests if a player can be selected correctly.
    """
    mock_game.choose_player()
    assert mock_game.player.name in mock_game.players


def test_game_play(mock_game_with_data):
    """
    Tests the main game play loop.
    """
    game = mock_game_with_data
    game.player.name = "Player1"  # Simulate choosing a player
    game.play()

    # Ensure score resets after losing
    assert game.player.score == 0
    assert game.players["Player1"]["previous_score"] == 0  # Update logic for your case.
