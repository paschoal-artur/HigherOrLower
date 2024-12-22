from src.core.player import Player

def test_increment_score():
    player = Player()
    player.increment_score()
    assert player.score == 1

def test_reset_score():
    player = Player()
    player.increment_score()
    player.reset_score()
    assert player.score == 0
    assert not player.lost

def test_lose():
    player = Player()
    player.lose()
    assert player.lost
