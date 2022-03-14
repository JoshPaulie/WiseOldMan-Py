from wiseoldman_py import wiseoldman
from wiseoldman_py.player import Achievement, Player

wom = wiseoldman.WiseOldMan()
bexlii = wom.get_player(username="bexlii")


def test_get_player():
    """Test for player by username"""
    assert isinstance(bexlii, Player)


def test_player_skill_level():
    """Test for player's skill, which is a custom property that should be checked."""
    assert isinstance(bexlii.latest_snapshot.attack.level, int)


def test_player_get_achievements():
    """Test for getting a player's achievements"""
    bexlii_achievements = bexlii.get_achievements()
    assert isinstance(bexlii_achievements, list)
